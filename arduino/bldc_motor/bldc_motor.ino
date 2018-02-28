/* input */
int speed = A0;

/* output */
int direction = 2;
int enabler = 3;
int _break = 4;
int avi = 5;

int current_speed = 128;
int step = 16;

int analog_min = 0;
int analog_max = 255;
int level_step = 32;


void setup() {
  Serial.begin(9600);

  pinMode(speed, INPUT);

  pinMode(direction, OUTPUT);
  pinMode(enabler, OUTPUT);
  pinMode(_break, OUTPUT);
  pinMode(avi, OUTPUT);
}


void loop() {
  char input;
  if (Serial.available() > 0) {
    input = Serial.read();
    log();

    Serial.print("Input received: ");
    Serial.println(input);
    Serial.println("Applying input");
    Serial.println("");
    bldc(input);

    log();
  }
}


void bldc(char input) {
  switch(input) {

  case 'e':
    digitalWrite(enabler, HIGH);
    break;

  case 'd':
    digitalWrite(enabler, LOW);
    break;

  case 'f':
    digitalWrite(direction, HIGH);
    break;

  case 'r':
    digitalWrite(direction, LOW);
    break;

  case 'b':
    digitalWrite(_break, LOW);
    break;

  case 'm':
    digitalWrite(_break, HIGH);
    break;

  case 'h':
    current_speed += step;
    if (current_speed > analog_max) {
      current_speed = analog_max;
    }
    analogWrite(avi, current_speed);
    break;

  case 'l':
    current_speed -= step;
    if (current_speed < analog_min) {
      current_speed = analog_min;
    }
    analogWrite(avi, current_speed);
    break;

  case 'a':
    current_speed = analog_min;
    analogWrite(avi, current_speed);
    break;

  case 'z':
    current_speed = analog_max;
    analogWrite(avi, current_speed);
    break;

  }
}


void log() {
  Serial.println("Motor status");
  Serial.println("===============");

  Serial.print("Direction: ");
  Serial.print(digitalRead(direction));
  Serial.print(" Enabler: ");
  Serial.print(digitalRead(enabler));
  Serial.print(" Break: ");
  Serial.print(digitalRead(_break));
  Serial.print(" avi: ");
  Serial.print(analogRead(avi));
  Serial.print(" Speed: ");
  Serial.print((speed));
  Serial.print(" Current Speed: ");
  Serial.print(current_speed);

  Serial.println("\n\n\n\n");
}
