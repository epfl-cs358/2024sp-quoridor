
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
int linearStart = 90;
int rotationStart = 0;
int gripperStart = 0;

//End position
int linearEnd = 0;
int rotationEnd = 125;
int gripperEnd = 90;

void setup() {
  linearServo.attach(9);
  rotationServo.attach(10);
  gripperServo.attach(11);

  //linearServo.write(linearPos);
  //rotationServo.write(90);
  //gripperServo.write(gripperPos);

  //Set the gripper to the right starting position
  up();
  delay(100);
  release();
  delay(100);
  rotate(0);
  delay(100);
}

void loop() {
  rotate(65);
  down();
  //grab();
  //delay(100);

  //up();
  //rotate(125);
  //delay(100);

  //down();
  //release();
  delay(1000);
  up();
  rotate(0);
  delay(1000);

  //up();
  //delay(1000);



}


void down(){
  for (linearPos; linearPos >= linearEnd; linearPos -= 1) {
    linearServo.write(linearPos);
    delay(linearSpeed);
  }

}

void up(){
    for (linearPos; linearPos <= linearStart; linearPos += 1) {
    linearServo.write(linearPos);
    delay(linearSpeed);
  }
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
}

void grab(){
  for (gripperPos; gripperPos <= gripperEnd; gripperPos += 1) {
    gripperServo.write(gripperPos);
    delay(gripperSpeed);
  }
}

void release(){
  for (gripperPos; gripperPos >= gripperStart; gripperPos -= 1) {
    gripperServo.write(gripperPos);
    delay(gripperSpeed);
  }
}

