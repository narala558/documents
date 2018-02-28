int pushButton = 2;
int sleep = 100;

int led1=13;
int led2=8;

int ledOn=13;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(pushButton, INPUT);
}


void loop() {
  
  int buttonState = digitalRead(pushButton);

  digitalWrite(LED_BUILTIN, buttonState);
  digitalWrite(led1, buttonState);
  digitalWrite(led2, !buttonState);

  digitalWrite(ledOn, HIGH);

  Serial.println(buttonState);
  
}
