#include <math.h>

#define boardSquaresLengthMM 24
#define boardSquaresSpacingMM 6
#define boardFullLengthMM (8 * boardSquaresSpacingMM + 9 * boardSquaresLengthMM)
#define wallOffsetOnSideMM (boardSquaresLengthMM + boardSquaresSpacingMM)

//RECALCULATE WHEN ADDING THE HEAD
#define boardCornerLowerXStep -475
#define boardCornerHigherXStep -3075
#define boardCornerLowerYStep 25
#define boardCornerHigherYStep (abs(boardCornerLowerXStep - boardCornerHigherXStep) + boardCornerLowerYStep)
#define boardFullLengthStep (boardCornerHigherYStep - boardCornerLowerYStep)

#define turnMMtoStep(mm) (long)((boardFullLengthStep * (mm)) / boardFullLengthMM)

#define getMMPlayer(pos) (long)((pos) * (boardSquaresLengthMM + boardSquaresSpacingMM) + (boardSquaresLengthMM)/2)

//X IS NEGATIVE DIRECTION
#define getStepXPlayer(posX) (long)(-1 * turnMMtoStep(getMMPlayer(posX)) + boardCornerLowerXStep)
#define getStepYPlayer(posY) (long)(turnMMtoStep(getMMPlayer(posY)) + boardCornerLowerYStep)

#define getMMWall(pos) (long)(pos * (boardSquaresLengthMM + boardSquaresSpacingMM) + boardSquaresLengthMM + (boardSquaresSpacingMM)/2)

#define getStepXWall(posX) (long)(-1 * turnMMtoStep(getMMWall(posX) + (((posX) == 8) ? wallOffsetOnSideMM : 0)) + boardCornerLowerXStep) 
#define getStepYWall(posY) (long)(turnMMtoStep(getMMWall(posY)) + boardCornerLowerYStep)
