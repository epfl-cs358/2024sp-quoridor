#include <Servo.h>
#include <AccelStepper.h>
#include <MultiStepper.h>
#include "boardMovement.h"

AccelStepper X(
  AccelStepper::FULL2WIRE, 
  StepperXPin1, 
  StepperXPin2
);
AccelStepper Y(
  AccelStepper::FULL2WIRE, 
  StepperYPin1, 
  StepperYPin2 
);
MultiStepper XY;
long pos_xy[2] = {0,0};

Servo claw_ser;
Servo rotation_ser;
Servo Z_ser;

bool isClawHigh = true;
bool isClawClose = true;
WallOrientation clawOrientation = HORIZONTAL;

void setupMotors() {

  X.setMaxSpeed(500.0);
  X.setEnablePin(StepperXPin3);
  Y.setMaxSpeed(500.0);
  Y.setEnablePin(StepperYPin3);
  XY.addStepper(X);
  XY.addStepper(Y);

  Z_ser.attach(ServoZPin);
  claw_ser.attach(ServoClawPin);
  rotation_ser.attach(ServoRotationPin);

  Serial.begin(9600);
  delay(10000); 
}

void forceStopMotors(){
  X.stop();
  Y.stop();
  X.disableOutputs();
  Y.disableOutputs();
}

void moveToXY(long x, long y){
  pos_xy[0] = x;
  pos_xy[1] = y;
  XY.moveTo(pos_xy);
  XY.runSpeedToPosition();
}

void goToOrigin(){
  moveToXY(0, 0);
}

void playMove(MoveData move_data){
  X.enableOutputs();
  Y.enableOutputs();

  moveToBoardPosition(move_data.old_position, move_data.piece_type);
  rotateTo(move_data.old_orientation);
  openClaw();
  lowerClaw(move_data.piece_type);
  closeClaw();
  raiseClaw(move_data.piece_type);

  moveToBoardPosition(move_data.new_position, move_data.piece_type);
  rotateTo(move_data.new_orientation);
  lowerClaw(move_data.piece_type);
  openClaw();
  raiseClaw(move_data.piece_type);
  closeClaw();

  rotateTo(HORIZONTAL);
  goToOrigin();

  X.disableOutputs();
  Y.disableOutputs();
}

void moveToBoardPosition(BoardPosition pos, PieceType type){
  
  long x, y;
  //Translate pos into a x and y coordinate for the motors depending on the piece type
  if(type == PLAYER){
    //TODO//
  }else{
    //TODO//
  }
  moveToXY(x, y);

  Serial.print("move to pos: ");
  Serial.print(pos);
  Serial.print("\n");
}

void openClaw(){
  if(isClawClose){
    /*
    TODO NEED TO FIND PARAMETERS
    for (int pos = Min; pos < Max; pos += 1) { 
      claw_ser.write(pos);           
      delay(16);                      
    }
    */
  delay(250);

  isClawClose = false; 
  
  Serial.print("open claw \n");
  }
}

void closeClaw(){
  if(!isClawClose){
    /*
    TODO NEED TO FIND PARAMETERS
    for (int pos = Max; pos > Min; pos -= 1) { 
      claw_ser.write(pos);           
      delay(16);                      
    }
    */
  delay(250);
  isClawClose = true; 

  Serial.print("close claw \n");
  }
}

void rotateTo(WallOrientation orientation){
  if(clawOrientation != orientation){
    if(orientation == HORIZONTAL){
     /*
      TODO NEED TO FIND PARAMETERS
      for (int pos = Max; pos > Min; pos -= 1) { 
        rotation_ser.write(pos);           
        delay(16);                      
      }
     */
    }else{
      /*
      TODO NEED TO FIND PARAMETERS
      for (int pos = Min; pos < Max; pos += 1) { 
        claw_ser.write(pos);           
        delay(16);                      
      }
      */
    }
    delay(250);
    clawOrientation = orientation; 

    Serial.print("rotate to orientation: ");
    Serial.print(orientation == HORIZONTAL ? "HORIZONTAL" : "VERTICAL");
    Serial.print("\n");
  }
}

void lowerClaw(PieceType type){
  if(isClawHigh){
    /*
    TODO NEED TO FIND PARAMETERS
    for (int pos = Max; pos > Min; pos -= 1) { 
      Z_ser.write(pos);           
      delay(16);                      
    }
    */
    delay(250);
    isClawHigh = false;

    Serial.print("lower the claw \n");
  }
}

void raiseClaw(PieceType type){
  if(!isClawHigh){
    /*
    TODO NEED TO FIND PARAMETERS
    for (int pos = Max; pos > Min; pos -= 1) { 
      Z_ser.write(pos);           
      delay(16);                      
    }
    */
    delay(250);
    isClawHigh = true;

    Serial.print("raise the claw \n"); 
  }
}

//For debug only
void motorControlLoop(){
  if (X.distanceToGo() == 0 && Y.distanceToGo() == 0) {
    while (Serial.available() == 0) {}
    String s;
    pos_xy[0] = Serial.parseInt(); 
    pos_xy[1] = Serial.parseInt();
    s = Serial.readString();
    Serial.print("x = ");
    Serial.print(pos_xy[0]);
    Serial.print(" y = ");
    Serial.print(pos_xy[1]);
    Serial.println(s);
    XY.moveTo(pos_xy);
  }
  XY.runSpeedToPosition();
}