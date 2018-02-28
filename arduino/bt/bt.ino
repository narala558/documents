void setup() {
  Serial.begin(9600);
}


void loop() {
  serial_read();
}


void serial_read()
{
  if(Serial.available() > 0 )
    {
      Serial.println("Reading serial data...");
      char command = Serial.read();
      Serial.println(command);
      Serial.write(command);
    }
}
