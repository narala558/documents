int board_led = 13;
char input;

void setup() {
  Serial.begin(9600);

  pinMode(board_led, OUTPUT);
}


void loop() {
  digitalWrite(board_led, HIGH);
  delay(500);
  digitalWrite(board_led, LOW);
  delay(500);

  Serial.write("a");
  Serial.println("");
  delay(500);
}
