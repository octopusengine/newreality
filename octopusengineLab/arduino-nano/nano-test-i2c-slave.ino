#include <Wire.h> 

const int LED13 = 13;
const int OUT12 = 12;
const int D2 = 2;
const int D3 = 3;


char a; 
long cnt=0;
byte mb[2];
byte m[2];
//-----------------------------------
//octopus engine LAB
//Arduino Nano
//2015-03 - v. 1.0.0
//-----------------------------------
//octopusengine.eu | newreality.eu
//-----------------------------------

long analog0;
long analog1;
long analog2;

long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 10;    // the debounce time; increase if the output flickers

int buttonState2;
int buttonState3;
int lastButtonState2 = LOW;
int lastButtonState3 = LOW;
//---------------------------------------------------------------------------------

 
void setup(){ 
   Serial.begin(9600);
   Serial.println("test i2c - slave"); 
   
   Wire.begin(0x33); 
   pinMode(OUT12, OUTPUT); 
   pinMode(LED13, OUTPUT); 
   pinMode(D2, INPUT);
   pinMode(D3, INPUT);

   blink();   

   Wire.onReceive(onRec); 
   Wire.onRequest(sendData); 
   } 
 
void loop()
{ 
   //Serial.println(">");
   delay(10);
   readDigi();
   analog0 = analogRead(A0);
   analog1 = analogRead(A1);
   analog2 = analogRead(A2);  

   //Serial.print(analog0);
    
    
   if(a == 'H'){digitalWrite(LED13, HIGH); cnt++;} 
   else if(a == 'L'){digitalWrite(LED13, LOW);}

   else if(a == '1'){digitalWrite(OUT12, HIGH);} 
   else if(a == '0'){digitalWrite(OUT12, LOW);}
   
   else if(a == 'R'){cnt=0;} //reset counter
  
   
   //else {Serial.println("nic");}    
} 

void blink(){
  //test signal blink
   digitalWrite(LED13, HIGH);
   delay(300);
   digitalWrite(LED13, LOW);
}

void readDigi(){
  int reading2 = digitalRead(D2);
  delay(1);
  int reading2b = digitalRead(D2);
  if (reading2==reading2b) {  lastButtonState2 = reading2;}
  else lastButtonState2=digitalRead(D2);

//---
  int reading3 = digitalRead(D3);
  delay(1);
  int reading3b = digitalRead(D3);
  if (reading3==reading3b) {  lastButtonState3 = reading3;}
  else lastButtonState3=digitalRead(D3);
}

 
 void onRec(int b){ 
   //Serial.println("rec:");
   while(Wire.available() > 0){ 
   a = Wire.read(); 
   //Serial.println(a); 
   }
}

void sendData(){
  mb[0] = analog0%256; //byte low  
  mb[1] = (analog0-(analog0%256))/256; //byte high
  mb[2] = analog1%256; //byte low  
  mb[3] = (analog1-(analog1%256))/256; //byte high
  mb[4] = analog2%256; //byte low  
  mb[5] = (analog2-(analog2%256))/256; //byte high
  mb[6] = lastButtonState2;
  mb[7] = lastButtonState3;
  mb[8] = 0;
  mb[9] = 0;
  mb[10] = 0;
  mb[11] = 0;
  mb[12] = 0;
  mb[13] = 0;
  mb[14] = 123;
  mb[15] = cnt;
  Wire.write(mb, 16);
  
}

