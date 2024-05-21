#include "boardMovement.h"
#include "serialInterpreter.h"
#include "HardwareSerial.h"
#include <math.h>

MoveData getMoveDataFromString(char* string_of_commands){
  int old_position;
  int new_position;
  char piece_type_string[7];
  
  memset(piece_type_string, '\0', 7);
  char old_orientation_string[11];
  memset(old_orientation_string, '\0', 11);
  char new_orientation_string[11];
  memset(new_orientation_string, '\0', 11);

  old_position = atoi(strtok(string_of_commands, "<>"));
  new_position = atoi(strtok(NULL, "<>"));
  strcpy(piece_type_string, strtok(NULL, "<>"));
  if(!strcmp(piece_type_string, "WALL")){
    strcpy(old_orientation_string, strtok(NULL, "<>"));
    strcpy(new_orientation_string, strtok(NULL, "<>"));
  }

  MoveData move_data;
  move_data.old_position = old_position;
  move_data.new_position = new_position;
  move_data.piece_type = (!strcmp(piece_type_string, "WALL")) ? WALL : PLAYER;
  move_data.old_orientation = (!strcmp(old_orientation_string, "VERTICAL")) ? VERTICAL : HORIZONTAL;
  move_data.new_orientation = (!strcmp(new_orientation_string, "VERTICAL")) ? VERTICAL : HORIZONTAL;

  moveDataPrint(move_data);
  
  return move_data;
}

void setupInterpreter(){
  Serial.println("To use the interpreter use commands:");
  Serial.println("<old_position><new_position><WALL><old_orientation><new_orientation>");
  Serial.println("or");
  Serial.println("<old_position><new_position><PLAYER>");
  Serial.println("where old_position and new_positions must be integers,");
  Serial.println("and old_orientation and new_orientation can either be HORIZONTAL or VERTICAL.");
}

void waitingForResponseLoop(){
  while (Serial.available() == 0) {}

  char* duplicate_of_serial_string = strdup(Serial.readString().c_str());
  playMove(getMoveDataFromString(duplicate_of_serial_string));
  free(duplicate_of_serial_string);
}

//For debug
void moveDataPrint(MoveData move_data){
  Serial.print("<");
  Serial.print(move_data.old_position);
  Serial.print(">");
  Serial.print("<");
  Serial.print(move_data.new_position);
  Serial.print(">");
  Serial.print("<");
  Serial.print(move_data.piece_type == PLAYER ? "PLAYER" : "WALL");
  Serial.print(">");
  Serial.print("<");
  Serial.print(move_data.old_orientation == VERTICAL ? "VERTICAL" : "HORIZONTAL");
  Serial.print(">");
  Serial.print("<");
  Serial.print(move_data.new_orientation == VERTICAL ? "VERTICAL" : "HORIZONTAL");
  Serial.print("> \n");
}

