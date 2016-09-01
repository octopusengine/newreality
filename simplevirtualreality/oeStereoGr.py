import pygame, random, sys, time, math

global type3d
global sizeX
global sizeY
global lDist
type3d=1
sizeX=1600
sizeY=900
lDist=30

myMatrix={}     # first man big
myMatrixTxt={}     # first man big
myMatrixLive={}

# cube
a=50 #30
nas=300 #70nas500 80nas600
anas=10
mnas=2
alfa=55   #70ok1 45
divAlfa = math.tan(alfa* math.pi/180)
oko=3 #10ok 20+ nesmysl
odstup=300 #stereo display distance

xx0=750
yy0=300
xx=50
yy=500
zz=601

mxc=0
myc=0
mzc=0
hBod=3
hX=30   #pozice
hY=10


#---------------------------------------------------basic
font={}         # mem. for font from extern file
mx=128
my=64
#---------------------------------------------------colors

#colour.r = (colour.r+random.randint(-3,3)) % 255
#colour.g = (colour.g+random.randint(-3,3)) % 255
#colour.b = (colour.b+random.randint(-3,3)) % 255
colour0 = pygame.Color('#555555')
colour1 = pygame.Color('#999999')
colour2 = pygame.Color('#990000')
colourR = pygame.Color('#990000')
colourB = pygame.Color('#0000aa')
colourW = pygame.Color('#ffffff')

global cBLA


cBLA = 0, 0, 0 
cSILL = 120, 120, 120 #light
cSIL = 63, 63, 63  ## silver
cSILD = 33, 33, 33 #dark
cWHI = 255, 255, 255 
cRED = 255, 0, 0 
cBLU = 0, 0, 255 
cGRE = 0, 255, 0 
cGRED = 0, 128, 0
cYEL = 255, 255, 0

# color variables for skin
col0=cBLA
col1=cWHI
col2=cSILL
col3=cSIL
col5=cRED
col6=cGRE
col7=cBLU

x=sizeX/2
y=sizeY/2



window = pygame.display.set_mode([sizeX,sizeY])
##myfont = pygame.font.SysFont("monospace", 15)

def boxStatus(txtS):
        x=lDist
	y=lDist
	a=sizeX-2*lDist
	b=100
	
	pygame.draw.line(window,colour1,(x,y),(x+a,y),2) 
	pygame.draw.line(window,colour1,(x+a,y),(x+a,y+b),2)
	pygame.draw.line(window,colour1,(x+a,y+b),(x,y+b),2)
	pygame.draw.line(window,colour1,(x,y+b),(x,y),2)
	
	#x=50
	#y=220
	#a=200
	#b=sizeY-300
	#pygame.draw.line(window,colour1,(x,y),(x+a,y),2) 
	#pygame.draw.line(window,colour1,(x+a,y),(x+a,y+b),2)
	#pygame.draw.line(window,colour1,(x+a,y+b),(x,y+b),2)
	#pygame.draw.line(window,colour1,(x,y+b),(x,y),2)


def point2D(x0,y0,z0,col):
    d1=z0*divAlfa
    x1=xx0+(x0/d1)*nas
    y1=yy0+(y0/d1)*nas
   
    colour=col
    pygame.draw.line(window,colour,(x1,y1),(x1+2,y1),2) 


def oePoint3D(t3d,x0,y0,z0,col):
    if (t3d==1): #simple perspective   
       d1=z0*divAlfa
       x1=xx0+(x0/d1)*nas
       y1=yy0+(y0/d1)*nas
       
       pygame.draw.line(window,col,(x1,y1),(x1+2,y1),2)
       
    if (t3d==2): #red/blue stereo
       d1=z0*divAlfa+oko
       x1=xx0+(x0/d1)*nas
       y1=yy0+(y0/d1)*nas
          
       pygame.draw.line(window,colourB,(x1,y1),(x1+2,y1),2) 

       d1o=z0*divAlfa-oko
       d1=z0*divAlfa
       x1=xx0+(x0/d1o)*nas
       y1=yy0+(y0/d1)*nas
    
       pygame.draw.line(window,colourR,(x1,y1),(x1+2,y1),2)
       
    if (t3d==3): #stereographics      
       d1=z0*divAlfa+oko
       x1=xx0+(x0/d1)*nas-odstup
       y1=yy0+(y0/d1)*nas
          
       pygame.draw.line(window,col,(x1,y1),(x1+2,y1),2) 

       d1o=z0*divAlfa-oko
       d1=z0*divAlfa
       x1=xx0+(x0/d1o)*nas+odstup
       y1=yy0+(y0/d1)*nas
          
       pygame.draw.line(window,col,(x1,y1),(x1+2,y1),2)
           


def oeLine3D(t3d,x1i,y1i,z1i,x2i,y2i,z2i,col): #x1i = c1 input
   if (t3d==1): #simple perspective   
      d1=z1i*divAlfa
      x1=xx0+(x1i/d1)*nas
      y1=yy0+(y1i/d1)*nas  
    
      d2=z2i*divAlfa
      x2=xx0+(x2i/d2)*nas
      y2=yy0+(y2i/d2)*nas
    
      pygame.draw.line(window,col,(x1,y1),(x2,y2),1)
      
   if (t3d==2): #red/blue stereo
       d1=z1i*divAlfa+oko
       x1=xx0+(x1i/d1)*nas
       y1=yy0+(y1i/d1)*nas
       
       d2=z2i*divAlfa+oko
       x2=xx0+(x2i/d2)*nas
       y2=yy0+(y2i/d2)*nas
       
       pygame.draw.line(window,colourB,(x1,y1),(x2,y2),1)    
       
       d1=z1i*divAlfa-oko
       x1=xx0+(x1i/d1)*nas
       y1=yy0+(y1i/d1)*nas
       
       d2=z2i*divAlfa-oko
       x2=xx0+(x2i/d2)*nas
       y2=yy0+(y2i/d2)*nas
       
       pygame.draw.line(window,colourR,(x1,y1),(x2,y2),1)  
       
   if (t3d==3): #stereographics
       colour=col
       
       d1=z1i*divAlfa+oko
       x1=xx0+(x1i/d1)*nas+odstup
       y1=yy0+(y1i/d1)*nas
       
       d2=z2i*divAlfa+oko
       x2=xx0+(x2i/d2)*nas+odstup
       y2=yy0+(y2i/d2)*nas
       
       pygame.draw.line(window,col,(x1,y1),(x2,y2),1)  #Right
    
       d1=z1i*divAlfa-oko
       x1=xx0+(x1i/d1)*nas-odstup
       y1=yy0+(y1i/d1)*nas
       
       d2=z2i*divAlfa-oko
       x2=xx0+(x2i/d2)*nas-odstup
       y2=yy0+(y2i/d2)*nas
       
       pygame.draw.line(window,col,(x1,y1),(x2,y2),1) #Left
          


def oeCube3D(t3d,x0,y0,z0,a0,col):
   if (t3d==1): #simple perspective
      d1=z0*divAlfa
      x1=xx0+(x0/d1)*nas
      y1=yy0+(y0/d1)*nas
      a1=(a0/d1)*nas*anas
    
      d2=(z0+a0)*divAlfa
      x2=xx0+(x0/d2)*nas
      y2=yy0+(y0/d2)*nas
      a2=(a0/d2)*nas*anas
    
      pygame.draw.line(window,col,(x1,y1),(x1+a1,y1),2) 
      pygame.draw.line(window,col,(x1+a1,y1),(x1+a1,y1+a1),2)
      pygame.draw.line(window,col,(x1+a1,y1+a1),(x1,y1+a1),2)
      pygame.draw.line(window,col,(x1,y1+a1),(x1,y1),2)

      pygame.draw.line(window,col,(x1,y1),(x2,y2),2)
      pygame.draw.line(window,col,(x1+a1,y1),(x2+a2,y2),2)
      pygame.draw.line(window,col,(x1+a1,y1+a1),(x2+a2,y2+a2),2)
      pygame.draw.line(window,col,(x1,y1+a1),(x2,y2+a2),2)

      pygame.draw.line(window,col,(x2,y2),(x2+a2,y2),2) 
      pygame.draw.line(window,col,(x2+a2,y2),(x2+a2,y2+a2),2)
      pygame.draw.line(window,col,(x2+a2,y2+a2),(x2,y2+a2),2)
      pygame.draw.line(window,col,(x2,y2+a2),(x2,y2),2)

   if (t3d==2): #red/blue stereo
    d1=z0*divAlfa+oko
    x1=xx0+(x0/d1)*nas
    y1=yy0+(y0/d1)*nas
    a1=(a0/d1)*nas*10
    
    d2=(z0+a0)*divAlfa+oko
    x2=xx0+(x0/d2)*nas
    y2=yy0+(y0/d2)*nas
    a2=(a0/d2)*nas*10

    colour=colourB 
    pygame.draw.line(window,colour,(x1,y1),(x1+a1,y1),2) 
    pygame.draw.line(window,colour,(x1+a1,y1),(x1+a1,y1+a1),2)
    pygame.draw.line(window,colour,(x1+a1,y1+a1),(x1,y1+a1),2)
    pygame.draw.line(window,colour,(x1,y1+a1),(x1,y1),2)

    pygame.draw.line(window,colour,(x1,y1),(x2,y2),2)
    pygame.draw.line(window,colour,(x1+a1,y1),(x2+a2,y2),2)
    pygame.draw.line(window,colour,(x1+a1,y1+a1),(x2+a2,y2+a2),2)
    pygame.draw.line(window,colour,(x1,y1+a1),(x2,y2+a2),2)

    pygame.draw.line(window,colour,(x2,y2),(x2+a2,y2),2) 
    pygame.draw.line(window,colour,(x2+a2,y2),(x2+a2,y2+a2),2)
    pygame.draw.line(window,colour,(x2+a2,y2+a2),(x2,y2+a2),2)
    pygame.draw.line(window,colour,(x2,y2+a2),(x2,y2),2)

    d1o=z0*divAlfa-oko
    d1=z0*divAlfa
    x1=xx0+(x0/d1o)*nas
    y1=yy0+(y0/d1)*nas
    a1=(a0/d1)*nas*10
    
    d2o=(z0+a0)*divAlfa-oko
    d2=(z0+a0)*divAlfa
    x2=xx0+(x0/d2o)*nas
    y2=yy0+(y0/d2)*nas
    a2=(a0/d2)*nas*10
    
    colour=colourR
    pygame.draw.line(window,colour,(x1,y1),(x1+a1,y1),2) 
    pygame.draw.line(window,colour,(x1+a1,y1),(x1+a1,y1+a1),2)
    pygame.draw.line(window,colour,(x1+a1,y1+a1),(x1,y1+a1),2)
    pygame.draw.line(window,colour,(x1,y1+a1),(x1,y1),2)

    pygame.draw.line(window,colour,(x1,y1),(x2,y2),2)
    pygame.draw.line(window,colour,(x1+a1,y1),(x2+a2,y2),2)
    pygame.draw.line(window,colour,(x1+a1,y1+a1),(x2+a2,y2+a2),2)
    pygame.draw.line(window,colour,(x1,y1+a1),(x2,y2+a2),2)

    pygame.draw.line(window,colour,(x2,y2),(x2+a2,y2),2) 
    pygame.draw.line(window,colour,(x2+a2,y2),(x2+a2,y2+a2),2)
    pygame.draw.line(window,colour,(x2+a2,y2+a2),(x2,y2+a2),2)
    pygame.draw.line(window,colour,(x2,y2+a2),(x2,y2),2)   
      
   if (t3d==3): #stereographics
      d1=z0*divAlfa+oko
      x1=xx0+(x0/d1)*nas+odstup
      y1=yy0+(y0/d1)*nas
      a1=(a0/d1)*nas*10
    
      d2=(z0+a0)*divAlfa+oko
      x2=xx0+(x0/d2)*nas+odstup
      y2=yy0+(y0/d2)*nas
      a2=(a0/d2)*nas*10

      colour=col
      pygame.draw.line(window,colour,(x1,y1),(x1+a1,y1),2) 
      pygame.draw.line(window,colour,(x1+a1,y1),(x1+a1,y1+a1),2)
      pygame.draw.line(window,colour,(x1+a1,y1+a1),(x1,y1+a1),2)
      pygame.draw.line(window,colour,(x1,y1+a1),(x1,y1),2)

      pygame.draw.line(window,colour,(x1,y1),(x2,y2),2)
      pygame.draw.line(window,colour,(x1+a1,y1),(x2+a2,y2),2)
      pygame.draw.line(window,colour,(x1+a1,y1+a1),(x2+a2,y2+a2),2)
      pygame.draw.line(window,colour,(x1,y1+a1),(x2,y2+a2),2)

      pygame.draw.line(window,colour,(x2,y2),(x2+a2,y2),2) 
      pygame.draw.line(window,colour,(x2+a2,y2),(x2+a2,y2+a2),2)
      pygame.draw.line(window,colour,(x2+a2,y2+a2),(x2,y2+a2),2)
      pygame.draw.line(window,colour,(x2,y2+a2),(x2,y2),2)

      d1o=z0*divAlfa
      d1=z0*divAlfa-oko
      x1=xx0+(x0/d1o)*nas-odstup
      y1=yy0+(y0/d1)*nas
      a1=(a0/d1)*nas*10
    
      d2o=(z0+a0)*divAlfa
      d2=(z0+a0)*divAlfa-oko
      x2=xx0+(x0/d2o)*nas-odstup
      y2=yy0+(y0/d2)*nas
      a2=(a0/d2)*nas*10
    
      pygame.draw.line(window,colour,(x1,y1),(x1+a1,y1),2) 
      pygame.draw.line(window,colour,(x1+a1,y1),(x1+a1,y1+a1),2)
      pygame.draw.line(window,colour,(x1+a1,y1+a1),(x1,y1+a1),2)
      pygame.draw.line(window,colour,(x1,y1+a1),(x1,y1),2)

      pygame.draw.line(window,colour,(x1,y1),(x2,y2),2)
      pygame.draw.line(window,colour,(x1+a1,y1),(x2+a2,y2),2)
      pygame.draw.line(window,colour,(x1+a1,y1+a1),(x2+a2,y2+a2),2)
      pygame.draw.line(window,colour,(x1,y1+a1),(x2,y2+a2),2)

      pygame.draw.line(window,colour,(x2,y2),(x2+a2,y2),2) 
      pygame.draw.line(window,colour,(x2+a2,y2),(x2+a2,y2+a2),2)
      pygame.draw.line(window,colour,(x2+a2,y2+a2),(x2,y2+a2),2)
      pygame.draw.line(window,colour,(x2,y2+a2),(x2,y2),2)



def rect2D(x0,y0,z0,a0):
    d1=z0*divAlfa
    x1=xx0+(x0/d1)*nas
    y1=yy0+(y0/d1)*nas
    a1=(a0/d1)*nas*anas
    
    d2=(z0+a0)*divAlfa
    x2=xx0+(x0/d2)*nas
    y2=yy0+(y0/d2)*nas
    a2=(a0/d2)*nas*anas

    colour=cSIL
   
    pygame.draw.line(window,colour,(x1+a1,y1+a1),(x1,y1+a1),2)  
    pygame.draw.line(window,colour,(x1+a1,y1+a1),(x2+a2,y2+a2),2)
    pygame.draw.line(window,colour,(x1,y1+a1),(x2,y2+a2),2)  
    pygame.draw.line(window,colour,(x2+a2,y2+a2),(x2,y2+a2),2)  


def rect2Dfill(x0,y0,z0,a0,col):
    d1=z0*divAlfa
    x1=xx0+(x0/d1)*nas
    y1=yy0+(y0/d1)*nas
    a1=(a0/d1)*nas*anas
    
    d2=(z0+a0)*divAlfa
    x2=xx0+(x0/d2)*nas
    y2=yy0+(y0/d2)*nas
    a2=(a0/d2)*nas*anas
  
    point_list = []
    point_list.append((x1+a1,y1+a1))
    point_list.append((x1,y1+a1))
    point_list.append((x2,y2+a2))
    point_list.append((x2+a2,y2+a2))

    pygame.draw.polygon(window, col, point_list)
    #pygame.draw.polygon(window, cSIL, [[100, 100], [100, 400],[400, 300]])

def drawChessboard(c1,c2):
    iii=0
    jjj=0
    for ii in range(-2000,2000,a*anas):
            iii = iii+1
            for jj in range(-210,300,a):
               jjj=jjj+1     
               rect2D(xx+ii,yy,zz+jj,a)
               if (iii%2==0):
                  if (jjj%2==0):
                     rect2Dfill(xx+ii,yy,zz+jj,a,c2)
               else:
                  if (jjj%2==0):
                     rect2Dfill(xx+ii,yy,zz+jj,a,c2)
                     
               #else:
               #   rect2Dfill(xx+ii,yy,zz+jj,a,cBLA)       
               #rect2D(xx+ii,yy,zz+jj,a)
       #line3D(10,1000,zl,1500,1000,zl,colour0)


#--------------------------------------------------------------basic
def readFont(fileName):
  fontfile=file(fileName,"r")
  adresafontu=0
  for radka in fontfile:
    rozlozeno = radka.split(",")                      # bytes from one line
    for bajt in range(5):
      font[adresafontu] = int(rozlozeno[bajt][-4:],0) # ...save byte to "matrix"
      adresafontu = adresafontu + 1
  fontfile.close()

def simpleChar(t3d,myChar,chx,chy,chz,sizeCh,col):
    global type3d   
    kod=ord(str(myChar))
    adr_fontu = (kod-32) * 5  # pointer to start 5 Bytes

    for f in range(5):       
        adr_fontu = (kod-32) * 5  # pointer to start 5 Bytes
        bajt = font[adr_fontu + f]          
        for b in range(8):
            znx = sizeCh*f       # s = 8bit col (0 az 14) , b = 0 :: 7
            zny = sizeCh*(8-b+8)              
            mask = (1 << (7-b))   
            if ((bajt & mask) != 0):   
              # mem_plot(chx+zx,chy+zy,0) 
              #point3DRB(xx+chx+znx,yy+chy+zny,zz+chz)
              oePoint3D(t3d,chx+znx,chy+zny,chz,col)  
            # else:
            #   mem_plot(chx+zx,chy+zy,1) 
            #   point3DRB(xx+100,yy+100,zp)        


def simpleCharZ(t3d,myChar,chx,chy,chz,sizeCh,col):
    kod=ord(str(myChar))
    #znak(ord(text[zn:zn + 1]), superx, radka, inverze)
    adr_fontu = (kod-32) * 5  # pointer to start 5 Bytes

    for f in range(5):       
        bajt = font[adr_fontu + f]          
        for b in range(8):
            znx = sizeCh*f       # s = 8bit col (0 az 14) , b = 0 :: 7
            zny = sizeCh*(8-b+8)              
            mask = (1 << (7-b))   
            if ((bajt & mask) != 0):   
              # mem_plot(chx+zx,chy+zy,0) 
              #point3DRB(xx+chx+znx,yy+chy+zny,zz+chz)
              oePoint3D(t3d,chx+znx,chy,chz+zny,col)  
            # else:
            #   mem_plot(chx+zx,chy+zy,1) 
            #   point3DRB(xx+100,yy+100,zp)


# print one character on pozition superx (0-119) and row (0-7)
def znak(kod , superx , r , inverze=False):
    adr_fontu = (kod-32) * 5  # pointer

    for f in range(5):       
        if (inverze == False): # 
          bajt = font[adr_fontu + f]          
        else:
          bajt = ~(font[adr_fontu + f])

        for b in range(8):
            zx = superx+f       
            zy = r - b+8              
            maska = (1 << (7-b))   
           
            if ((bajt & maska) != 0):   
              ##myMatrixTxt[zx,zy]= 7 
              mem_plot(zx,zy,1)               
            else:
              ##myMatrixTxt[zx,zy]= 0  
              mem_plot(zx,zy,0)             
    
# chars.. space
def slovo(text, superx , radka, space=1 , inverze=True):
  global stara_lr
  if (isinstance(text, unicode) == False):  # 
    text=  unicode(text, "utf-8")           # UTF-8 > unicode
  
  for zn in range (len(text)):
    if (ord(text[zn:zn + 1]) > 127):   # no ASCII? decode
      try:                    # indefine
        znak(cz[ord(text[zn:zn + 1])], superx, radka, inverze)
      except:                 # ...index scz[].
        znak(177, superx, radka, inverze)  # err. chessboard

    else:
      znak(ord(text[zn:zn + 1]), superx, radka, inverze) # ASCII 32-127 normal

    # space (1 pix)
    for m in range(space):
      if (superx + m + 5 < 120):  # max value
          superx= superx + 5 + space   # next pozition

  ###pygame.display.flip() 

def mem_plot(x,y,co): # one "pixel"
   colCase = cBLA
   if co==0:
       #if pNoise.enable:    
       #   pomR=random.randint(0,30)
       #   if pomR: colCase = col2 #light
       #   else: colCase = col3
       #else:
       colCase = col2     
   if co==3:
       colCase = col5 #light
   if co==7:
       colCase = col0
       #pomR=random.randint(0,100)
       #if pomR: colCase = col3 #light
       #else: colCase = col0
       
   pygame.draw.line(window,colCase,(x*hBod+hX,y*hBod+hY),(x*hBod+1+hX,y*hBod+hY),1) 
   #pygame.draw.line(window,colCase,(x+hX,y+hY),(x+1+hX,y+hY),2) 

def saveImg(sizeX, sizeY):
   timeStamp=datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
   label = myFont.render(timeStamp, 1, (255,255,255))
   window.blit(label, (sizeX-200, sizeY-50))
   fileName = myDir+datetime.now().strftime("%Y%m%d_%H%M%S") +'.gif'
   pygame.image.save(window,fileName)


def doBmp128x128(imgName):
    fileImg=open(imgName, "rb")  # read image to data[]
    data = fileImg.read()  
    fileImg.close()                  

    # http://www.root.cz/clanky/graficky-format-bmp-pouzivany-a-pritom-neoblibeny
    # zacatek obrazovych dat urcuji 4 bajty v souboru na pozicich 10 az 13 (desitkove) od zacatku souboru
    zacatekdat = ord(data[10]) + (ord(data[11]) * 256) + (ord(data[12]) * 65536) + (ord(data[13]) * 16777216)
    bajt=zacatekdat
    for r in range (127,-1,-1): # read data[]
                                # 0 az 127 (128 radku)
        for s in range (16):
          for b in range(8):
            zx = (s*8) + b      # s = osmibodovy sloupec na displeji (0 az 14) , b = bit v kazdem bajtu 0 az 7
            zy = r              # r = mikroradka na displeji 0 az 63
            maska = (1 << (7-b))   
            
            if (ord(data[bajt]) & maska != 0):   
              #myMatrix[zx,zy]= 0 
              mem_plot(zx,zy,0)                 
            else:
              #myMatrix[zx,zy]= 1  
              mem_plot(zx,zy,7)          
          bajt = bajt +1
    pygame.display.flip()


def doBmp128x64(imgName):
    fileImg=open(imgName, "rb")  # read image to data[]
    data = fileImg.read()  
    fileImg.close()    

    # http://www.root.cz/clanky/graficky-format-bmp-pouzivany-a-pritom-neoblibeny
    zacatekdat = ord(data[10]) + (ord(data[11]) * 256) + (ord(data[12]) * 65536) + (ord(data[13]) * 16777216)
    bajt=zacatekdat
    for r in range (127,-1,-1): # read data[]
                                # 0 az 127 (128 radku)
        for s in range (16):
          for b in range(8):
            zx = (s*8) + b      # s = osmibodovy sloupec na displeji (0 az 14) , b = bit v kazdem bajtu 0 az 7
            zy = r              # r = mikroradka na displeji 0 az 63
            maska = (1 << (7-b))   
            
            if (ord(data[bajt]) & maska != 0):  
              #myMatrix[zx,zy]= 0 
              mem_plot(zx,zy,7)                   
            else:
              #myMatrix[zx,zy]= 1  
              mem_plot(zx,zy,0)          
          bajt = bajt +1
    pygame.display.flip()


def doBmp2Mat(imgName,pozx,pozy):
    fileImg=open(imgName, "rb")  # read image to data[]
    data = fileImg.read()  
    fileImg.close()    


    # http://www.root.cz/clanky/graficky-format-bmp-pouzivany-a-pritom-neoblibeny
    # zacatek obrazovych dat urcuji 4 bajty v souboru na pozicich 10 az 13 (desitkove) od zacatku souboru
    zacatekdat = ord(data[10]) + (ord(data[11]) * 256) + (ord(data[12]) * 65536) + (ord(data[13]) * 16777216)
    bajt=zacatekdat
    for r in range (my,-1,-1):     # cteni promenne data[] bajt po bajtu a prevod na souradnice superx,supery
                                # 0 az 127 (128 radku)
        for s in range (16):
          for b in range(8):
            zx = pozx+(s*8) + b      # s = osmibodovy sloupec na displeji (0 az 14) , b = bit v kazdem bajtu 0 az 7
            zy = pozy+r              # r = mikroradka na displeji 0 az 63
            maska = (1 << (7-b))   
            #kazdy bit z grafickych dat se na prislusne pozici na displeji (resp. v promenne mapa[]) bud rozsviti, nebo zhasne
            if (ord(data[bajt]) & maska != 0):   # dvoubarevna windowsovska bitmapa ma opacne nastavene bity nez displej:
              myMatrix[zx,zy]= 0 
               #mem_plot(zx,zy,0)          # jednickove bity jsou bile body             
            else:
              myMatrix[zx,zy]= 7  
               #mem_plot(zx,zy,1)          # nulove bity jsou cerne body
          bajt = bajt +1
     #pygame.display.flip()    

def plotMat(xp,yp):
  for x in range(mx):
    for y in range(my):
      mem_plot(x+xp,y+yp,myMatrix[x,y])
  ##pygame.display.flip()



def rotate_3d_points(points, angle_x, angle_y, angle_z):
        new_points = []
        for point in points:
                x = point[0]
                y = point[1]
                z = point[2]
                new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
                new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
                y = new_y
                # isn't math fun, kids? 
                z = new_z
                new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
                new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
                x = new_x
                z = new_z
                new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
                new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
                x = new_x
                y = new_y
                new_points.append([x, y, z])
        return new_points

def do_line_demo(surface, counter):
        ##print counter
        ##color = (1, 1, 1)  
        cube_points = [
                [-1, -1, 1],
                [-1, 1, 1],
                [1, 1, 1],
                [1, -1, 1],
                [-1, -1, -1],
                [-1, 1, -1],
                [1, 1, -1],
                [1, -1, -1]]
                
        connections = [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 0),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 4),
                (0, 4),
                (1, 5),
                (2, 6),
                (3, 7)
                ]
                
        t = counter * 2 * 3.14159 / 60 # this angle is 1 rotation per second
        
        # rotate about x axis every 2 seconds 
        # rotate about y axis every 4 seconds 
        # rotate about z axis every 6 seconds 
        points = rotate_3d_points(cube_points, t / 2, t / 4, t / 6)
        flattened_points = []
        for point in points:
                flattened_points.append(
                        (point[0] * (1 + 1.0 / (point[2] + 3)),
                         point[1] * (1 + 1.0 / (point[2] + 3))))
        
        for con in connections:
                p1 = flattened_points[con[0]]
                p2 = flattened_points[con[1]]
                x1 = p1[0] * 60 + 200
                y1 = p1[1] * 60 + 150
                x2 = p2[0] * 60 + 200
                y2 = p2[1] * 60 + 150
                
                # This is the only line that really matters 
                pygame.draw.line(surface, col1, (xx0/2+x1, yy0/2+y1), (xx0/2+x2, yy0/2+y2), 3)
                #pygame.draw.line(window,col1,(xx0/2+x1, yy0+y1), (xx0/2+x2, yy0+y2), 3)
      
