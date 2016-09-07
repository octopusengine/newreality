import time, socket, os
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

#====== get procesor temp ============================
def getProcTemp():  
   try:
	 # Return CPU temperature as a character string
     pytemp = os.popen("vcgencmd measure_temp").readline()
     #value=(res.replace("temp=","").replace("C\n",""))
     #temp1=int(float(getCPUtemperature()))
     
     #pytemp = subprocess.check_output(['vcgencmd', 'measure_temp'], universal_newlines=True)
     #ipoutput = subprocess.check_output(['vcgencmd measure_temp'], universal_newlines=True, 'w'))
     #print pytemp 
     eq_index = pytemp.find('=')+1 
     #if eq_index>0:
     var_name = pytemp[:eq_index].strip()
     value = pytemp[eq_index:eq_index+4]
     numvalue=float(value)
   except:
     numvalue = -1
   return numvalue 

#====== get Bitcoin course ============================
def getBTC():
     try: 
       bcfile = urllib2.urlopen("https://www.bitstamp.net/api/ticker/").read()
       jObj = json.loads(bcfile)
       lastBtc =int(float(jObj["last"]))
     except:
       lastBtc = 333   
     return lastBtc



