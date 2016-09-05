#-----------------------------------------------------------------------
# www.octopusengine.eu | www.newreality.eu
# yenda.net*napismi.cz
#-----------------------------------------------------------------------
#---2012---python experiment A1
# .01 only ASCI matrix and structure test
#---2013---pygame - edition A2 - simple graphics
# .02 extern init file 
# .03 event-pygame.KEYDOWN
# .05 3D perspective (still default)
#---2015---3D test (ortoGraphics)
# .06 3D simple shapes (cheesboard), colour skin
#---2016---
# .07 stereoGraphic testing F1,F2,F3 
# .08 plugins and info ...F8,F9,F11,F12, wordl map, bitcoin, graph
# .09 network alfa: single / server / client
# 1.0.0 > 30.08.2016 < github/octopusengine/newreality 
# 1.0.1 > 03.09.2016 < test import 3d cloud points from simple3Dscanner
#-----------------------------------------------------------------------
# TODO:
# testing on Raspberry Pi 3, simple OPEN-GL
# new hardware (gyro position), trimers, home sensors (temp..)
# networking cooperation, local net > internet
# display search (for virtual reality glasses)
#-----------------------------------------------------------------------
ver="1.0.1"
#-----------------------------------------------------------------------

import os, sys, time
import pygame, random, math
import subprocess, threading, socket
from threading import Thread

from oeStereoGr import *
import oe #MAIN OCTOPUSE ENGINE LIBRARY
#import oe_incl

nexThread = True #running

scannData="points.xyz" ##xyz cloud points from simple3Dscanner
configFile="config.ini"

pygame.init()
window = pygame.display.set_mode([sizeX,sizeY])
myfont = pygame.font.SysFont("monospace", 15)
myfont12 = pygame.font.SysFont("monospace", 12)

#temp definition
servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#-------------------------------------------------
points2D = []
xyzList = []
cloudPoints = []
xyzList.append((0,0,0))

frames=0

#--------------------------------------------------------------
def parseInit():
   global vars, hwV, hw, ipsV, netV #variables from config
   vars = dict() 
   #if os.path.exists("config.ini"):
   with open(configFile) as f:
      for line in f:
        eq_index = line.find('=') 
        if eq_index>0:
          var_name = line[:eq_index].strip()
          value = (line[eq_index + 1:].strip()) 
          vars[var_name] = value
     
          
   try: hwV = int(vars["hw"])
   except: hwV=0

   try: netV = str(vars["net"])
   except: netV="single?"  

   try: ipsV = str(vars["ips"])
   except: ipsV="0.0.0.0"  


#--------------------------------------------------------------
#-------------------------------------------------
parseInit() #import config.ini parameters

print("network: "+netV)
isClient=False
isServer=False
#if (netV=="single"):
if (netV=="server"): isServer=True
if (netV=="client"): isClient=False

pygame.display.set_caption("octopus engine New reality " + ver)
oeHw=hwV

from oePlugins import BasicSw
from oePlugins import SystemSw

oeB = BasicSw(oeHw)
oeS = SystemSw(oeHw)

from oePlugins import Plugin2D
pLlist = Plugin2D(lDist,110)  # F5
pWorld = Plugin2D(90,60)   # F6
pHist = Plugin2D(0,0)         # F8
pChessB = Plugin2D(0,0)       # F9
pLive = Plugin2D(720,200)   # F10
pGraf = Plugin2D(930,350)   # F11
pRlist = Plugin2D(sizeX-270,110)  # F12
pSkin0 = Plugin2D(0,0) 
pNoise = Plugin2D(0,0,False) 
pScann = Plugin2D(50,50,False) 
pBeeAlfa = Plugin2D(350,250,False) 


global rList
global lList

lList = []
for listApp in range(32):
  lList.append("")
lList[0]=("VISUALISATION:")
lList[1]=("display: "+str(sizeX)+"x"+str(sizeY))
lList[2]=("perspective: "+str(alfa))
#print math.tan(alfa* math.pi/180) #deg>rad
lList[3]=("divAlfa:"+str(divAlfa))

lList[10]="NETWORK:"
lList[11]=netV
lList[12]="hostName: "+ oe.getHostName()
lList[13]="hostIp: "+ oe.getHostIp()
lList[14]="IP server: "+ ipsV

lList[20]="TIMER:"

rList = []
rList.append("System")
rList.append("ver: "+ver)  
rList.append("hw:" + str(hwV))
rList.append("---") 
for listApp in range(20):
  rList.append("")
rList[6]="WORLD POSITION"  

print "test class"
print str(pGraf.getXY())


fGraph = [] #test front graph
fGraph.append(100)
fGraph.append(100)
fGraph.append(300)
fGraph.append(500)
fGraph.append(600)
fGraph.append(700)

#test class
#print oeB.hallo()
#print oeP.hallo()
print oeS.sysInfo()

st=str(oe.getServerTime())
print("serverTime: "+st)
rList.append(st)

bc=str(oe.getBTC())
print("BTC(USD): "+bc)
rList.append(bc)
rList.append("")
rList.append("---") 
     

#--------------------------------------------------------------
def deltaM():
  myMatrix[(mxc+35)*mnas,(mzc+10)*mnas]= 3
  #world longitude and latitude:
  rList[7]="mx:"+str((mxc+6)*6.1) #+7
  rList[8]="mz:"+str((mzc-11)*-4.3)
  
  lList[5]="type3d: "+str(type3d)
  lList[6]="mx:"+str(mxc)
  lList[7]="my:"+str(myc)
  lList[8]="mz:"+str(mzc)
  fGraph[2]=mxc*50
  fGraph[3]=mzc*50
  fGraph[4]=myc*50
  xyzList.append((mxc,myc,mzc))
  lList[22]=str(frames)
  
def rListDraw(x,y):
  if (pRlist.enable):
    i=0
    for rLine in rList:
      label = myfont12.render(rLine, 1, cSILL)    
      window.blit(label, (x, y+lDist+i))
      i=i+20

def lListDraw(x,y):
  if (pLlist.enable):
    i=0
    for lLine in lList:
      label = myfont12.render(lLine, 1, cSILL)    
      window.blit(label, (x, y+lDist+i))
      i=i+20

def line3dlist(list3d):
  if (pHist.enable):
   #simpleChar("A",xx+mxc*a+a*2,yy+myc*a-a,zz-mzc*a,15,cYEL)
   for point3d in list3d: 
        lx=xx+point3d[0]*a
        ly=yy+point3d[1]*a
        lz=zz-point3d[2]*a
        #point2D(lx,ly,lz,cWHI)
        oePoint3D(type3d,lx,ly,lz,col1)

def initCoud3D(scale):
   global cloudPoints
   msg="INIT: Loading cloud poinds from 3dscanner (test)"
   doMsg(msg)
   print(msg)

   cnt=0
   print("load clout points file: "+scannData)
   with open(scannData) as f:
      for line in f:
         try:
           point = line.split(' ')
           xp,zp,yp = float(point[0])*scale,(float(point[1])+300)*scale,float(point[2])*scale-500
           #print xp,yp,zp
           body = ((xx+xp),(yy+yp),(zz+zp+200))
           oePoint3D(type3d,(xx+xp),(yy+yp),(zz+zp),col1)
           cloudPoints.append(body)
           cnt=cnt+1
           if (cnt%10000)==0:
              pygame.display.flip()
         except:
            Err=True
   pygame.display.flip()
   print("number of imported xyz points: "+str(cnt))
   time.sleep(5)      
         
def plotCoud3D(xc,yc,zc):
   if (pScann.enable):
      for pLine in cloudPoints:     
         oePoint3D(type3d,pLine[0]+xc,pLine[1]+yc,pLine[2]+zc,col1)

def plotBeeAlfa():
   if (pBeeAlfa.enable):
      a6=60
      sin60=0.866
      x6=pBeeAlfa.x
      y6=pBeeAlfa.y
      nAngle2D(6,a6, x6,y6, 32)
      nAngle2D(6,a6, x6+a6*sin60*2,y6, 39)
      nAngle2D(6,a6, x6+a6*sin60,y6+a6, 64)
         

def plotFGraf(x,y,dataG):
 if (pGraf.enable):
  i=0
  gWidth=300
  iNext = gWidth/10
  yH=15
  pygame.draw.line(window,cSILL,(x,y),(x+gWidth,y),2)
  for yg in range(10):
      pygame.draw.line(window,cSIL,(x,y-yg*yH),(x+gWidth,y-yg*yH),2)
    
  for num in dataG:
    pygame.draw.line(window,cSILL,(x+i,y),(x+i,y-num/100*yH),2)
    i=i+iNext

def matrixLiveInit():
  global myMatrixLive 
  n=32
  for row in range(n):
     for col in range(n):
        myMatrixLive[row,col]=random.randint(0,1)  
        

def plotLive(x,y): #temp.noise
 global myMatrixLive  
 if (pLive.enable):
  n=32
  nas=5
  for row in range(n):
     for col in range(n):
        pok=random.randint(0,10)
        if (pok==1):
           pygame.draw.line(window,cSIL,(x+col*nas,y+row*nas),(x+col*nas+2,y+row*nas),2)

        if pNoise.enable:
          pok=random.randint(0,1)
          if (pok==8):
             pygame.draw.line(window,cGRED,(x+col*nas,y+row*nas),(x+col*nas+2,y+row*nas),2) 

          pok=random.randint(0,300)
          if (pok==33):
             pygame.draw.line(window,cGRE,(x+col*nas,y+row*nas),(x+col*nas+2,y+row*nas),2)      
           
        if (myMatrixLive[row,col]==1):
           pygame.draw.line(window,cSIL,(x+col*nas,y+row*nas),(x+col*nas+2,y+row*nas),2)
        #next generation
        try:   
          if (myMatrixLive[row,col]==1 + myMatrixLive[row-1,col] + myMatrixLive[row+1,col] + myMatrixLive[row,col-1] + myMatrixLive[row,col+1])>3:
             myMatrixLive[row,col]==0
          else:
             myMatrixLive[row,col]==random.randint(0,1)
        except:
             myMatrixLive[row,col]==0 
    
#-----------------------------------------------------------
def doMsg(statusMsg):
    label1 = myfont.render(statusMsg, 1, col1)    
    window.blit(label1, (560, 130))
    pygame.display.flip()

             
def doPluginsBefore():
    divAlfa = math.tan(alfa* math.pi/180)
    
    statusMsg= "i: "+str(i)+ " alfa:" + str(alfa) + " xx0:" + str(xx0)+ " yy0:" + str(yy0)
    label1 = myfont.render(statusMsg, 1, col1)    
    window.blit(label1, (560, 50))

    statusMsg= "cube: x "+str(mxc)+ " z:" + str(mzc) 
    label2 = myfont.render(statusMsg, 1, (255,255,0))    
    window.blit(label2, (560, 80))

    slovo("newReality 1.0",20,10)

    if pWorld.enable:
       plotMat(pWorld.x,pWorld.y)

    if (pChessB.enable): 
       drawChessboard(cBLA,col2)

    plotLive(pLive.x,pLive.y)
    plotFGraf(930,350,fGraph)
    line3dlist(xyzList)
    
def doPluginsAfter():    
    boxStatus("status")
    rListDraw(pRlist.x,pRlist.y)
    lListDraw(pLlist.x,pLlist.y)

    statusMsgDown= "[F1]3D-perspective [F2]red&blue [F3]stereographic [F4]Bee | [F5]Left List [F6]World map [F7]3Dscann [F8]History points | [F9]Chess board [F10]Live [F11]Graph [F12]Right List"
    label1 = myfont.render(statusMsgDown, 1, col1)    
    window.blit(label1, (lDist*2, sizeY-30))

def doRotateCube(win):
  fps=15
  clock = pygame.time.Clock()
  for cc in range(60):
     win.fill(cBLA) 
     doPluginsBefore()
     do_line_demo(win, cc)
     pygame.display.flip()
     clock.tick(fps)   
  #time.sleep(1)    


#===================/include=============================================



#=============================================================================
#=============================================================================
i=1
nasi=5 
#intro.start
readFont("oeData/pcfont.txt")
doBmp2Mat("oeData/world128x64b.bmp",0,0)
matrixLiveInit()

#nAngle2D(4,30,100,100,cBLU)
#nAngle2D(3,30,100,100,cYEL)

doRotateCube(window)

#startServer()
#------------------------server------------------------------
from time import ctime
port = 12123 #12345          # Reserve a port for your service.
##Server Socket##

if isServer:
 print("---server---")
 s = socket.socket()         # Create a socket object
 #host = socket.gethostname() # Get local machine name
 host = '0.0.0.0'
 
 print("host: "+host + " /"+str(port))

 sADDR = (host, port)
 buff = 1024
 rMessage=""

 try:
  servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  servSock.bind(sADDR)

 except socket.error as e:
  print("old conection - close:") 	
  servSock.close()
  time.sleep(1)	
  servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  servSock.bind(sADDR)
	  
  
 servSock.listen(5)

 msg="SERVER: Waiting for a connection..."
 doMsg(msg)
 print(msg)
 
 cliSock, cADDR = servSock.accept()
 print "...Connection made with {0}".format(cADDR)

 def receive():
    global rMessage
    while True:
        rMessage = cliSock.recv(buff)
        if not rMessage:
            print "Ending connection"
            break
        print "[{0}]: {1}".format(ctime(), rMessage)

 def send():
    while True:
        sMessage = raw_input(">>")
        if not sMessage:
            break
        cliSock.send(sMessage)

 def sendAuto():
    global rMessage
    while True:
       if len(rMessage)>1:
         #sMessage = " >> ok:"+str(int(rMessage)*2)
         sMessage = " >> ok:"+rMessage
         lList[15]=rMessage
         cliSock.send(sMessage)
         rMessage=""

 t1snd = threading.Thread(target=sendAuto, name=3)
 t2rec = threading.Thread(target=receive, name=4)

 t1snd.start()
 t2rec.start()
#------------------------/server------------------------------
 

#startClient()
#------------------------client------------------------------

if isClient:
 print("---client---")

 s = socket.socket()         # Create a socket object
 ##host = 'localhost'
 host = ipsV ##server-ip.ok
 print("host: "+host + " /"+str(port))

 sADDR = (host, port)
 buff = 1024

 cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 cliSock.connect(sADDR)

 def receive():
    while True:
        rMessage = cliSock.recv(buff)
        if len(rMessage)>1:
           lList[15]=str(rMessage)
        if not rMessage:
            print "Ending connection"
            break
        print "[{0}]: {1}".format(ctime(), rMessage)

 def send():
    while True:
        sMessage = raw_input(">>")
        cliSock.send(sMessage)
        
  #t1snd = threading.Thread(target=send, name=1)
 t2rec = threading.Thread(target=receive, name=2)

  #t1snd.start()
 t2rec.start()

def sendAuto(co): #send to server:
   sMessage = str(co)
   cliSock.send(sMessage)
#------------------------/client------------------------------

def nexth(): ##thread timer
 global nexThread 
 cntx=0 
 while nexThread:
   
   time.sleep(5)
   cntx=cntx+1 
   #print cntx
   lList[21]=str(cntx)
   if isClient:
     sendAuto("t"+str(cntx)+"x"+str(mxc)) #test
     
#---thread start
thrTimer1 = Thread(target=nexth)
thrTimer1.start()

#test
initCoud3D(15) #scale=10 ok



#============================================================================= 
#============================================================================= 
## main "do while" process:
while True:
    window.fill(cBLA) 
    doPluginsBefore()

    plotCoud3D(mxc*a*2,myc*a*2,-mzc*a*2)

    oePoint3D(type3d,xx+mxc*a+a/4,yy+myc*a+a/4,zz-mzc*a,col1)   
    oeLine3D(type3d,xx,yy,zz,xx+mxc*a+a/4,yy+myc*a+a/4,zz-mzc*a,col1)   
          
    oeCube3D(type3d,xx,yy,zz,a/2,col1)
    
    simpleChar(type3d,"B",xx+a*2,yy-a,zz,15,col1)
    
    oeCube3D(type3d,xx+mxc*a+a/4,yy+myc*a+a/4,zz-mzc*a,a/2,col1)    
    simpleChar(type3d,"A",xx+mxc*a+a*2,yy+myc*a-a,zz-mzc*a,15,col1)

    simpleCharZ(type3d,"C",xx+mxc*a+a*3,yy+myc*a-a*3,zz-mzc*a,15,col6)
      
    doPluginsAfter()

    plotBeeAlfa()
    
       
    pygame.display.flip()
    frames+=1
    time.sleep(0.05)
   
#=============================================================================
#=============================================================================
# pygame.KEYDOWN events:
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   mxc=mxc-1                   
                if event.key == pygame.K_RIGHT:
                   mxc=mxc+1                   
                if event.key == pygame.K_UP:
                   mzc=mzc-1                   
                if event.key == pygame.K_DOWN:
                   mzc=mzc+1                   

                if event.key == pygame.K_u: #up
                   myc=myc-1                   
                if event.key == pygame.K_d: #down
                   myc=myc+1                   
                if event.key == pygame.K_h: #home
                   mxc=0
                   myc=0
                   mzc=0

                if event.key == pygame.K_n: #add noise on/off
                   pNoise.enable = not pNoise.enable  

                if event.key == pygame.K_s: #colour skin
                   pSkin0.enable = not pSkin0.enable
                   if pSkin0.enable:
                     col0=cBLA
                     col1=cWHI
                     col2=cSIL
                     col3=cSILL
                     col5=cRED
                     col6=cGRE
                     col7=cBLU
                   else:
                     col0=cBLA
                     col1=cYEL
                     col2=cGRED
                     col3=cGRE
                     col5=cYEL
                     col6=cRED
                     col7=cGRED

                if event.key == pygame.K_F1: #
                   type3d=1

                if event.key == pygame.K_F2: #
                   type3d=2

                if event.key == pygame.K_F3: #
                   type3d=3

                if event.key == pygame.K_F4: #
                   pBeeAlfa.enable =  not pBeeAlfa.enable

                                   
                if event.key == pygame.K_F5: #
                   pLlist.enable =  not pLlist.enable

                if event.key == pygame.K_F6: #
                   pWorld.enable =  not pWorld.enable

                if event.key == pygame.K_F7: #
                   pScann.enable =  not pScann.enable                   

                if event.key == pygame.K_F8: #
                   pHist.enable =  not pHist.enable



                if event.key == pygame.K_F9: #
                   pChessB.enable = not pChessB.enable
        
                if event.key == pygame.K_F10: #
                   pLive.enable =  not pLive.enable    

                if event.key == pygame.K_F11: #
                   pGraf.enable =  not pGraf.enable

                if event.key == pygame.K_F12: #
                   pRlist.enable =  not pRlist.enable

                if event.key == pygame.K_b:
                  rList[2]=str(oe.getServerTime())
                  rList[3]=(str(oe.getBTC()))
                  fGraph[0]=int(rList[3])

                if event.key == pygame.K_r:  
                  doRotateCube(window)

                deltaM()
                if isClient:
                    sendAuto("x"+str(mxc)+"y"+str(myc)+"y"+str(mzc)) #test
                   
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    nic=True

                if event.button == 5:
                    nic=True

#=============================================================================E
#=============================================================================N
#=============================================================================D



    

   
