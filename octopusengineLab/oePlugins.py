#!/usr/bin/env python
# yenda - octopusengine.eu - 2013-16 

import random, sys, os, time, datetime
import pygame
from time import sleep

import urllib2, json #getBtc, 
import zipfile
import shutil

from socket import gethostname, gethostbyname #getIp
import subprocess
import string

##import RPi.GPIO as GPIO

#global device_file
import glob 

#---ftp
import ftplib
from ftplib import FTP
from sys import argv


#-----------------------------------------------------
#-----------------------------------------------------
class BasicSw:
  def __init__(self,hw=3):
    self.hw = hw
 
  def hallo(self):
      return "HI! (basic)"

#-----------------------------------------------------
#-----------------------------------------------------
class Plugin2D:
  def __init__(self,x,y,enable=True,glob=False):
    self.x = x
    self.y = y
    self.enable = enable # = visible
    self.glob = glob     # for network -> glob = all users the same

  def setEnable(self,enable):
    self.enable = enable

  def setGlobal(self,enable):
    self.glob = glob

  def getXY(self):
    return ((self.x,self.y))

#-----------------------------------------------------
#-----------------------------------------------------
class SystemSw:
  def __init__(self,hw=3):
    self.hw = hw
   
 
  def sysInfo(self):
   ret_list = []
   ret_list.append("sysInfo")
    
   try:
     import platform, sys
     ret_list.append('[INFO] --- MAIN SYSTEM')
     ret_list.append("machine: "+platform.machine())
     #self.hhh.sysRep("architecture: "+platform.architecture())
     ret_list.append("system: "+platform.system())
     ret_list.append("version: "+platform.version())
     ret_list.append("platform: "+platform.platform())
     ret_list.append("node: "+platform.node())
     ret_list.append("release: "+platform.release())   
     #self.hhh.sysRep("processor: "+platform.processor())
     ret_list.append("Python: "+platform.python_version())
     ret_list.append("Py.compliler: "+platform.python_compiler())
     #self.hhh.sysRep("Py.build: "+platform.python_build())
     #import linux_sysinfo as sysinfo
     #print 'Memory available:', sysinfo.memory_available()
  
     now = time.time()
     means = time.ctime(now)
     try: 
       ret_list.append("User number: "+str(os.getuid()))
       ret_list.append("Process ID: "+str(os.getpid()))
       ret_list.append("Current Directory: "+os.getcwd())
       #print "System information: ",what
     except:
       ret_list.append('[ERROR] Usr / Process')
       
     ret_list.append("System os.times: "+str(os.times()))
     ret_list.append("Time is now: "+str(now))
     ret_list.append("Which interprets as: "+means)
     
     ret_list.append('[INFO] --- PROCESSOR')
     try:  
      procLine=[]
      with open('/proc/cpuinfo') as f:
       for line in f:
        procLine.append(line.rstrip('\n'))

      ret_list.append(procLine[0])
      ret_list.append(procLine[1])
      ret_list.append(procLine[2])
      ret_list.append(procLine[3])

     except:
       ret_list.append('[ERROR] Processor')
       
     ret_list.append('[INFO] --- MEMORY')
     from collections import OrderedDict
     meminfo=OrderedDict()
     with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
     ret_list.append("MemTotal: "+str( meminfo['MemTotal']))
     ret_list.append("MemAvailable: "+str( meminfo['MemAvailable']))  
     ret_list.append("MemFree: "+str( meminfo['MemFree']))
   except:
     ret_list.append('[ERROR] Sys. info') 
   return ret_list

  def wifiOn(self):
    os.system("sudo ifup wlan0") #halt after
  
  def wifiOff(self):
    os.system("sudo ifdown wlan0") #halt after  

  def shutDown(self,shutDownOk):
    if shutDownOk:    
      
      os.system("sudo shutdown -h now") #halt after
      sys.exit()
    else:  
     
      pygame.guit()
      sys.exit()

  def getFileInfo(self,file,path):
     fsize=0 
     fdate=0
     try:
       fsize=os.path.getsize(path+file) 
     except:
       fsize=0      
     try:
       fdatetime=os.path.getmtime(path+file)
       #fdate=datetime.fromtimestamp(fdatetime)
       #fdate=str(datetime.fromtimestamp(fdatetime).strftime("%Y/%m/%d-%H:%M:%S"))
       fdate=datetime.datetime.fromtimestamp(int(fdatetime)).strftime("%Y/%m/%d-%H:%M:%S")
     except:
       fdate=0
     return str(fsize)+"B ..... "+str(fdate),str(fsize),str(fdate)

  def getFileInfoSize(self,file,path):
     fsize=self.getFileInfo(file,path)[1] 
     return str(fsize)
 
  def getFileInfoDate(self,file,path):
     fdate=self.getFileInfo(file,path)[2] 
     return str(fdate)

  def iSRAddSysFileInfo(self):
     global swPath,iPath
     #self.hhh.iSRAdd("<br />")
     ret_list.append("[INFO] --- MAIN FILE SYSTEM")
     ret_list.append("-main: "+str(self.getFileInfo("oePlugins.py",swPath)[0]))
   
    
     self.hhh.sysRep("<b>Last update:</b>")
     with open(iPath+"netupdate.php") as f:
      for line in f:
         self.hhh.sysRep(line)

     self.hhh.iSRAdd("<hr />")
     
  def sysIni(self): 
       with open(sysIniPath+dwConfig, 'r') as si:
          return si.read()
          #... sysWiFiConfig
          
  def sysRead(self): 
      with open(sysIniPath+dwConfig, 'r') as si:
          return si.read()     

  def sysWrite(self,co): 
      filename="dwarfconfig.txt"
      with open(sysIniPath+filename, 'a') as si:
          si.write(co)


#------------------/oePlugins.py------------------------
        
