void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(10000);
  Serial.println("Get next move");
  }

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){
    char* duplicate_of_serial_string = strdup(Serial.readString().c_str());
    delay(3000);
    Serial.println("hello ?");
    delay(2000);
    Serial.println("Get next move");
  }
}
