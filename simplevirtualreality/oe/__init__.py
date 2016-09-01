import time, socket
import random, math
from socket import gethostname, gethostbyname #getIp
import urllib2, json #getBtc,

#---network---
port=12321
#---/


def getServerTime():
     try:       	  
       tim = urllib2.urlopen("http://www.octopusengine.eu/api/datetime.php").read()
     except:
       tim ="Err.time.url"      
     return tim

def getHostName():
     try: 
       host = socket.gethostname()       
     except:
       host = "socket Err.getHostName"   
     return host

def getHostIp():
     try: 
       hostnm = socket.gethostname()
       hostip =socket.gethostbyname(hostnm)
       host=hostip
     except:
       host = "socket Err.getHostIp"   
     return host

def getBTC():
     try: 
       bcfile = urllib2.urlopen("https://www.bitstamp.net/api/ticker/").read()
       jObj = json.loads(bcfile)
       lastBtc =int(float(jObj["last"]))
     except:
       lastBtc = 333   
     return lastBtc



