#include <Arduino.h>
#include <Wire.h>
#include <RoboClaw.h>

const int downPin = 8;
const int upPin = 9;
const int leftPin = 10;
const int rightPin =11;
const int speedPin=A0;
const int leftRoboClawAddress = 0x80;
const int rightRoboClawAddress = 0x81;
const int maxSpeed = 127;


bool controls[5] = {0, 0, 0, 0, 0}; // 0th index for speed, 1-4 for directions

// RoboClaw leftRoboClaw(&Serial1);
// RoboClaw rightRoboClaw(&Serial2);

void setup() {
  Serial.begin(9600);
  // Serial1.begin(38400);
  // Serial2.begin(38400);
  
  pinMode(7, OUTPUT);
  digitalWrite(7, HIGH);
  pinMode(upPin, INPUT);
  pinMode(upPin,LOW);
  pinMode(downPin, INPUT);
  pinMode(leftPin, INPUT);
  pinMode(rightPin, INPUT);
}

void loop() {
  
  controls[1] = digitalRead(downPin); //down
  controls[2] = digitalRead(upPin); //up
  controls[3] = digitalRead(leftPin);//left
  controls[4] = digitalRead(rightPin);//right
  controls[0] = analogRead(speedPin);//speed

  int speed = map(controls[0], 0, 1023, 0, maxSpeed);
  int leftSpeed = speed;
  int rightSpeed = speed;
   String direction="none";
  if (controls[1]==1) {
    leftSpeed = -maxSpeed;
    rightSpeed = -maxSpeed;
    direction="down";
  } else if (controls[2]==1) {
    leftSpeed = maxSpeed;
    rightSpeed = maxSpeed;
    direction="up";
  } else { 
    if (controls[3]==1) {
      leftSpeed = -maxSpeed;
      rightSpeed = maxSpeed;
      direction="left";
    } else if (controls[4]==1) {
      leftSpeed = maxSpeed;
      rightSpeed = -maxSpeed;
      direction="right";
      Serial.println(controls[4]);
    }
    if(direction!="none"){
     Serial.println(direction);
    }
    delay(1000);
  }}

  // leftRoboClaw.ForwardM1(leftRoboClawAddress, leftSpeed);
  // rightRoboClaw.ForwardM2(rightRoboClawAddress, rightSpeed);

  // You can also add code to read encoder values, set PID constants, etc. here

