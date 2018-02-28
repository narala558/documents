//Motor A
const int motor_a_enabler = 22;
int potPin = 2;    // select the input pin for the potentiometer
int val;
const int motor_a_pin_a = 6;
const int motor_a_pin_b = 7;

const int forward = 1;
const int stop = 0;
const int reverse = -1;

const int analog_high = 255;
const int analog_medium = 127;
const int analog_low = 0;

String line = "==============================";


void setup(){
  Serial.begin(9600);

  pinMode(motor_a_enabler, OUTPUT);
  digitalWrite(motor_a_enabler, HIGH);
}


void loop() {
  rotate(forward);
  rotate(stop);
  rotate(reverse);
}


void log() {
  Serial.println(line);
  Serial.println(digitalRead(motor_a_enabler));
  Serial.println(analogRead(motor_a_pin_a));
  Serial.println(analogRead(motor_a_pin_b));
}


void rotate(int direction) {
  val = analogRead(potPin);
  if(direction==forward){
    analogWrite(motor_a_pin_a, val);
    analogWrite(motor_a_pin_b, analog_low);
  }
  if(direction==reverse){
    analogWrite(motor_a_pin_a, val);
    analogWrite(motor_a_pin_b, analog_low);
  }
  if(direction==stop){
    for (int i=0; i<256; i++) {
      analogWrite(motor_a_pin_a, i);
      analogWrite(motor_a_pin_b, i);
      delay(10);
    }
  }

  log();
  delay(4000);
}
