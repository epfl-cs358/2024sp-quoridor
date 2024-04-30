#include <AccelStepper.h>
#include <MultiStepper.h>
// Voor de Arduino Uno + CNC shield V3
#define MOTOR_X_ENABLE_PIN 38
#define MOTOR_X_STEP_PIN 54
#define MOTOR_X_DIR_PIN 55


#define MOTOR_Y_ENABLE_PIN 56
#define MOTOR_Y_STEP_PIN 60
#define MOTOR_Y_DIR_PIN 61
#define SPEED 200
#define ACCELERATION 1
#define SIZE 400
AccelStepper motorX(1, MOTOR_X_STEP_PIN, MOTOR_X_DIR_PIN);
AccelStepper motorY(1, MOTOR_Y_STEP_PIN, MOTOR_Y_DIR_PIN);
MultiStepper steppers;

void setup()
{
   pinMode(MOTOR_X_ENABLE_PIN, OUTPUT);
   pinMode(MOTOR_Y_ENABLE_PIN, OUTPUT);

   motorX.setEnablePin(MOTOR_X_ENABLE_PIN);
   motorX.setPinsInverted(false, false, true);
   motorX.setAcceleration(ACCELERATION);
   motorX.setMaxSpeed(SPEED);
   motorX.setSpeed(SPEED);
   motorX.enableOutputs();

   motorY.setEnablePin(MOTOR_Y_ENABLE_PIN);
   motorY.setPinsInverted(false, false, true);
   motorY.setAcceleration(ACCELERATION);
   motorY.setMaxSpeed(SPEED);
   motorY.setSpeed(SPEED);
   motorY.enableOutputs();

  steppers.addStepper(motorX);
  steppers.addStepper(motorY);
   
   long positions[2]; 

  positions[0] = 3*SIZE;
  positions[1] = 2*SIZE;
  delay(3000);
  steppers.moveTo(positions);
  steppers.runSpeedToPosition();
  delay(3000);
}

void loop()
{
}