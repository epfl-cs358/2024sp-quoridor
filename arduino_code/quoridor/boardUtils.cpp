#include <math.h>

#define boardSquaresLengthMM 24
#define boardSquaresSpacingMM 6
#define boardFullLengthMM (8 * boardSquaresSpacingMM + 9 * boardSquaresLengthMM)
#define wallOffsetOnSideMM (boardSquaresLengthMM + boardSquaresSpacingMM)

//RECALCULATE WHEN ADDING THE HEAD
#define boardCornerLowerXStep -400
#define boardCornerHigherXStep -3050
#define boardCornerLowerYStep 225
#define boardCornerHigherYStep (abs(boardCornerLowerXStep - boardCornerHigherXStep) + boardCornerLowerYStep)
#define boardFullLengthStep (boardCornerHigherYStep - boardCornerLowerYStep)

#define turnMMtoStep(mm) (long)((boardFullLengthStep * (mm)) / boardFullLengthMM)

#define getMMPlayer(pos) (long)((pos) * (boardSquaresLengthMM + boardSquaresSpacingMM) + (boardSquaresLengthMM)/2)

//X IS NEGATIVE DIRECTION
#define getStepXPlayer(posX) (long)(-1 * turnMMtoStep(getMMPlayer(posX)) + boardCornerLowerXStep)
#define getStepYPlayer(posY) (long)(turnMMtoStep(getMMPlayer(posY)) + boardCornerLowerYStep)

#define getMMWall(pos) (long)(pos * (boardSquaresLengthMM + boardSquaresSpacingMM) + boardSquaresLengthMM + (boardSquaresSpacingMM)/2)

#define getMMFreeWallX() (long)(-1 * (boardSquaresLengthMM + boardSquaresSpacingMM + (boardSquaresSpacingMM)/2))
#define getMMFreeWallY(posY) (long)((posY) * (boardSquaresLengthMM + boardSquaresSpacingMM) - (boardSquaresSpacingMM)/2)

#define getStepXWall(posX, posY) (long)(-1 * turnMMtoStep((posX == 8) ? getMMFreeWallX() : getMMWall(posX)) + boardCornerLowerXStep) 
#define getStepYWall(posX, posY) (long)(turnMMtoStep((posX == 8) ? getMMFreeWallY(posY) : getMMWall(posY)) + boardCornerLowerYStep)
