const int analog_in = A0;
const int analog_out = A1;

int board_led = 13;

long randn;
int ri;
int ro;


void setup() {
  Serial.begin(9600);

  pinMode(analog_in, INPUT);
  pinMode(analog_out, OUTPUT);
}


void loop() {
  randn = random(0, 255);

  Serial.print("Random: ");
  Serial.println(randn);

  analogWrite(analog_in, randn);
  analogWrite(analog_out, randn);

  delay(10);

  ri = analogRead(analog_in);
  ro = analogRead(analog_out);

  Serial.print("Analog: ");
  Serial.print(ri);
  Serial.print(" ");
  Serial.print(ro);


  ri = digitalRead(analog_in);
  ro = digitalRead(analog_out);

  Serial.print("Digital: ");
  Serial.print(ri);
  Serial.print(" ");
  Serial.print(ro);
  Serial.print(" ");

  Serial.println("");

  /* blink_led(); */

  delay(1000);

}


void blink_led() {
  digitalWrite(board_led, HIGH);
  delay(1000);

  digitalWrite(board_led, LOW);
  delay(1000);

}
