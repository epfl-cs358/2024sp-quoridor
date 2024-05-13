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


//End position
int linearEnd = 0;
int rotationEnd = 125;

//gripper position
int gripperOpen = 120;
int gripperClose = 180;
int gripperWall = 168;
int gripperPawn = 160;

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

  //linearServo.write(linearPos);
  //rotationServo.write(90);
  //gripperServo.write(gripperPos);

  //Set the gripper to the right starting position
  //grabWall();
  up();
  delay(100);
  delay(100);
  rotate(0);
  delay(100);


  //down(linearEnd);

}

void loop() {

  
  down(50);
  release();
  delay(200);
  
  down(0);
  delay(100);
  grabWall();
  delay(200);
  up();
  // Put the piece down
  delay(100);
  down(0);
  delay(200);
  release();
  // go up
  delay(100);
  up();

  //rotate(65);
  //down();
  //grab();
  //delay(100);

  //up();
  //rotate(125);
  //delay(100);

  //down();
  //release();
  //delay(1000);
  //up();
  //rotate(0);
  //delay(1000);

  //up();
  //delay(1000);

  // release();
  // delay(1000);
  // down();
  // grabWall();
  // up();
  // rotate(65);
  // delay(2000);
  // down();
  // release();
  // delay(1000);
  // up();
  // rotate(0);

}



void down(int destination){
  for (linearPos; linearPos >= destination; linearPos -= 1) {
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

void grabWall(){
    for (gripperPos; gripperPos <= gripperWall; gripperPos += 1) {
    gripperServo.write(gripperPos);
    delay(gripperSpeed);
  }
}

void grabPawn(){
    for (gripperPos; gripperPos <= gripperPawn; gripperPos += 1) {
    gripperServo.write(gripperPos);
    delay(gripperSpeed);
  }
}

void release(){
  for (gripperPos; gripperPos >= gripperOpen; gripperPos -= 1) {
    gripperServo.write(gripperPos);
    delay(gripperSpeed);
  }
}