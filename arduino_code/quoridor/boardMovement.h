#include <stdint.h>

//TODO PUT CORRECT PINS FOR STEPPER AND SERVOS
#define StepperXPin1 1
#define StepperXPin2 1
#define StepperXPin3 1

#define StepperYPin1 1
#define StepperYPin2 1
#define StepperYPin3 1

#define ServoClawPin 1
#define ServoRotationPin 1
#define ServoZPin 1

enum PieceType {WALL, PLAYER};
enum WallOrientation{VERTICAL, HORIZONTAL};
typedef uint8_t BoardPosition;
typedef struct{
  BoardPosition old_position;
  BoardPosition new_position;
  PieceType piece_type;
  WallOrientation old_orientation;
  WallOrientation new_orientation;
}MoveData; 

void setupMotors();
void forceStopMotors();

void playMove(MoveData move_data);
void moveToBoardPosition(BoardPosition pos, PieceType type);
void openClaw();
void closeClaw();
void rotateTo(WallOrientation orientation);
void lowerClaw(PieceType type);
void raiseClaw(PieceType type);

void motorControlLoop();