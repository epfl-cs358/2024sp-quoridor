#include "boardMovement.h"
#include "serialInterpreter.h"

#define NORMAL_RUN 0

//#define DEBUG_MOVE 1

//USE THESE PINS FOR INTERUPT MANAGEMENT
#define NextMovePin 2
#define StopPin 3

//bool isWaitingForResponse = false; TODO SWAP FOR REAL
bool isWaitingForResponse = true;

void stopISR(){
  forceStopMotors();
  while(1){}
} 

void nextMoveISR(){
  if(!isWaitingForResponse){
    Serial.print("Get next move");
    isWaitingForResponse = true;
  }
}

void setupInterrupts(){
  pinMode(StopPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(StopPin), stopISR, RISING);

  pinMode(NextMovePin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(NextMovePin), nextMoveISR, RISING);
}

void setup() {
  setupMotors();
  setupInterpreter();
  //setupInterrupts(); TODO DECOMMENT FOR REAL
}

void loop() {
  #ifdef DEBUG_MOVE 
   motorControlLoop(); 
  #endif

  #ifdef NORMAL_RUN
    while(isWaitingForResponse){
      waitingForResponseLoop();
    }
  #endif
}