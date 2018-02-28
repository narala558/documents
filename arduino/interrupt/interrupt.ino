const byte interruptPin = A0;


void setup() {
  Serial.begin(9600);

  pinMode(interruptPin, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(interruptPin), blink, HIGH);
}


void loop() {
  delay(1000);
  digitalWrite(interruptPin, HIGH);
  delay(1000);
  digitalWrite(interruptPin, LOW);
}


void blink() {
  Serial.print("interrupt");
}
