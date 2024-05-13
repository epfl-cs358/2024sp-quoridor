#include <Servo.h>
//range servo black : 270°
//range command : 0-180°
// 0°   = 0°
// 90°  = 65°
// 180° = 125°


Servo linearServo;
Servo rotationServo;
Servo gripperServo;

int linearPos = 0;
int rotationPos = 0;
int gripperPos = 0;

//Speed
int linearSpeed = 10;
int rotationSpeed = 10;
int gripperSpeed = 10;

//Starting position
int linearStart = 110;
int rotationStart = 0;


//End position
int linearEnd = 15;
int rotationEnd = 125;

//gripper position
int gripperOpen = 130;
int gripperClose = 180;
int gripperWall = 168;
int gripperPawn = 165;

void setup() {
  gripperServo.write(gripperClose);
  delay(100);
  gripperPos = gripperClose;

  linearServo.write(linearStart);
  linearPos = linearStart;
  delay(100);
  rotationServo.write(0);
  rotationPos = 0;
  delay(100);

  linearServo.attach(11);
  rotationServo.attach(5);
  gripperServo.attach(6);

  //Set the gripper to the right starting position
  release();
  up();
  rotate(0);
}

void loop() {
  
  down();
  grabWall();
  up();
  // Put the piece down
  down();
  release();
  // go up
  up();
}



void down(){
  for (linearPos; linearPos >= linearEnd; linearPos -= 1) {
    linearServo.write(linearPos);
    delay(linearSpeed);
  }
  delay(100);
}

void up(){
    for (linearPos; linearPos <= linearStart; linearPos += 1) {
    linearServo.write(linearPos);
    delay(linearSpeed);
  }
  delay(100);
}

void rotate(int angle){
  if(angle > rotationPos){
    for (rotationPos; rotationPos <= angle; rotationPos += 1) {
      rotationServo.write(rotationPos);
      delay(rotationSpeed);
    }
  }else{
    for (rotationPos; rotationPos >= angle; rotationPos -= 1) {
      rotationServo.write(rotationPos);
      delay(rotationSpeed);
    }
  }
  delay(100);
}

void grabWall(){
    for (gripperPos; gripperPos <= gripperWall; gripperPos += 1) {
    gripperServo.write(gripperPos);
    delay(gripperSpeed);
  }
  delay(100);
}

void grabPawn(){
    for (gripperPos; gripperPos <= gripperPawn; gripperPos += 1) {
    gripperServo.write(gripperPos);
    delay(gripperSpeed);
  }
  delay(100);
}

void release(){
  for (gripperPos; gripperPos >= gripperOpen; gripperPos -= 1) {
    gripperServo.write(gripperPos);
    delay(gripperSpeed);
  }
  delay(100);
}