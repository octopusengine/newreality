<b>Raspberry Pi 3 + Arduino Nano</b> (as a i2c slave)<br/>
experimental analog input<br/>

<img src="http://www.newreality.eu/wp-content/uploads/2016/09/oe-lab01_bb.png" width="500">
<hr />
<b>oeLab / Arduino nano (I2C slave) - C</b>
<pre>
void setup(){ 
   Wire.begin(0x33);
   ...
   Wire.onReceive(onRec); 
   Wire.onRequest(sendData); 
   } 
 
void loop()
{ 
   delay(10);
   readDigi();
   analog0 = analogRead(A0);
   analog1 = analogRead(A1);
   if(a == 'H'){digitalWrite(LED13, HIGH); cnt++;} 
   else if(a == 'L'){digitalWrite(LED13, LOW);}
   ...
} 

void readDigi(){
  int reading2 = digitalRead(D2);
  delay(1);
  int reading2b = digitalRead(D2);
  if (reading2==reading2b) {  lastButtonState2 = reading2;}
  else lastButtonState2=digitalRead(D2);
...
}

 void onRec(int b){ 
   while(Wire.available() > 0){ 
   a = Wire.read(); 
   }
}

void sendData(){
  mb[0] = analog0%256; //byte low  
  mb[1] = (analog0-(analog0%256))/256; //byte high
  mb[2] = analog1%256; //byte low  
  mb[3] = (analog1-(analog1%256))/256; //byte high
 ...
  mb[14] = 123;
  mb[15] = cnt;
  Wire.write(mb, 16);
}
</pre>
in loop prepare data (analog A0,A1,A2.. and digital D2,D3) <br/>
on request - send it to I2C master<br />
</hr>



<b>oeLab / RaspberryPi (I2C master) - Python</b>
<pre>
import smbus, time
bus = smbus.SMBus(1)       # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x33      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00

def getLabData(): 
   bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, ord("H"))
   time.sleep(0.05)		
   data=bus.read_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0)
   bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, ord("L"))
   time.sleep(0.01)
   return data
</pre>
return 32Byte vector of values<br/>


<hr/>
green - procesor temperature<br />
red - analog0 value<br />
blue - analog1 value <br />
white - analog2 value<br />

<img src="https://raw.githubusercontent.com/octopusengine/newreality/master/octopusengineLab/images/lab-chart3.png">
<br/ >
<br/ >

<img src="https://raw.githubusercontent.com/octopusengine/newreality/master/octopusengineLab/images/oelab01-600.jpg">
<br/ >
<br/ >


<b>Only start:</b> start-a123.py<br/>
<b>Yes. It works on PC - Win / iOS / Linux (UBUNTU,MINT,Raspbian)</b> <br/> 
basic operation: the keyboard<br/> 
<i>arrows move the first cube<br/>
u - up<br/>
d - down<br/>

n - noise<br/>
b - Bitcoin course - to right list;-)<br/>
s - change skin</i><br/>
...<br/><br/>



<hr/>
<h2>3D visualisation</h2>
F1 perspective (A2)<br/>
F2 red&blue stereogr. (A3)<br/>
F3 stereographics (A3)<br/>

<img src="http://www.newreality.eu/wp-content/uploads/2016/08/visual01-600.jpg">


<h2>2D plugins</h2>
1.0.0 > world map<br/>
1.0.0 matrix / noise - next: live game...<br/>
chart / graph<br/>


<h2>3D plugins</h2>
1.0.1 > import cloud points data from <a href=https://github.com/octopusengine/simple3dscanner>github.com/octopusengine/simple3dscanner</a>
stars (testing)<br/>
"3D performance"<br/>

<h2>inputs</h2>
a1 a2 a3 - only standard keyboard and mouse<br/>
b1 - only for Raspbbery Pi3 new interfaces<br/>
<h2>network</h2>
socket <br/>
test? https://docs.python.org/3.5/library/socketserver.html<br/>

<hr />

