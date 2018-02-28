int led1=8;
int led2=13;

int sleep=200;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}


void loop() {
  digitalWrite(led1, HIGH);
  digitalWrite(led2, LOW);
  delay(sleep);

  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  delay(sleep);
}
