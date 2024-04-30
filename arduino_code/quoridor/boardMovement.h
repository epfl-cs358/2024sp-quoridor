#include <stdint.h>

//https://reprap.org/forum/read.php?219,168722 as stated here
//TODO PUT CORRECT PINS FOR STEPPER AND SERVOS
#define StepperXPin1 54
#define StepperXPin2 55
#define StepperXPin3 38

#define StepperYPin1 60
#define StepperYPin2 61
#define StepperYPin3 56

#define Speed 300
#define Acceleration 1

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

void debugStartMotors();
void motorControlLoop();