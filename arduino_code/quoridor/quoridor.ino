#include "boardMovement.h"
#include "serialInterpreter.h"


#define NORMAL_RUN 0

//#define DEBUG_MOVE 1

//USE THESE PINS FOR INTERUPT MANAGEMENT
#define NextMovePin 18
#define StopPin 19

bool isWaitingForResponse = true; // false;

void stopISR(){
  forceStopMotors();
  while(1){}
} 

void nextMoveISR(){
  Serial.print("Interrupt triggered");
  if(!isWaitingForResponse){
    Serial.print("Get next move");
    isWaitingForResponse = true;
  }
}

void setupInterrupts(){
  //pinMode(StopPin, INPUT_PULLUP);
  //attachInterrupt(digitalPinToInterrupt(StopPin), stopISR, RISING);

  //pinMode(NextMovePin, INPUT_PULLUP);
  //attachInterrupt(digitalPinToInterrupt(NextMovePin), nextMoveISR, RISING);
}

void setup() {
  setupMotors();
  // Calibration sequence
  calibrateMotors();
  #ifdef NORMAL_RUN
   //setupInterpreter();
   setupInterrupts(); 
  #endif
  #ifdef DEBUG_MOVE
   debugStartMotors();
  #endif
}


void loop() {
  #ifdef DEBUG_MOVE 
   motorControlLoop(); 
  #endif

  #ifdef NORMAL_RUN
    if(isWaitingForResponse){
      waitingForResponseLoop();
      //isWaitingForResponse = false;
    }
  #endif
}