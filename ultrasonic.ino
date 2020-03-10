#include <Servo.h>
int trigger_pin = 2;
int echo_pin = 3;

int time;
int distance; 

Servo myservo;
int pos = 0; 

void setup ( ) {

        Serial.begin (9600); 
        pinMode (trigger_pin, OUTPUT); 
        pinMode (echo_pin, INPUT);
        myservo.attach(9); 
}




void loop ( ) {

    digitalWrite (trigger_pin, HIGH);
    delayMicroseconds (10);
    digitalWrite (trigger_pin, LOW);
    time = pulseIn (echo_pin, HIGH);
    distance = (time * 0.034) / 2;
    Serial.print("Distance: ");  
    Serial.println(distance);   

    for (pos = 0; pos <= 180; pos += 1) { 
     myservo.write(pos);             
     delay(15);                       
    }
    for (pos = 180; pos >= 0; pos -= 1) { 
     myservo.write(pos);              
     delay(15);                       
   }
  
   
}
