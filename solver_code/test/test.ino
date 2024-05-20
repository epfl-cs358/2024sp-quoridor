void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(10000);
  Serial.println("Hello there");
  }

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){
    char* duplicate_of_serial_string = strdup(Serial.readString().c_str());
    delay(5000);
    Serial.println(duplicate_of_serial_string);
  }
}
