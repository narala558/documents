//these pins can not be changed 2/3 are special pins
int encoderPin1 = 2;
int encoderPin2 = 3;

volatile int lastEncoded = 0;
volatile long encoder0Value = 0;
long cev = 0;

long lastencoderValue = 0;

int lastMSB = 0;
int lastLSB = 0;


long encoder0Value1 = 0;
long encoder0Value2 = 0;
long pev = 0;

int right_hand_pwm = 5;
int right_hand_direction = 8;
int hand_motor_pwm = 40;

void setup() {
  Serial.begin (9600);

  pinMode(encoderPin1, INPUT);
  pinMode(encoderPin2, INPUT);

  digitalWrite(encoderPin1, HIGH); //turn pullup resistor on
  digitalWrite(encoderPin2, HIGH); //turn pullup resistor on

  //call updateEncoder() when any high/low changed seen
  //on interrupt 0 (pin 2), or interrupt 1 (pin 3)
  attachInterrupt(0, updateEncoder, CHANGE);
  attachInterrupt(1, updateEncoder, CHANGE);

  right_hand();
}

void loop(){
}


void updateEncoder(){
  int MSB = digitalRead(encoderPin1); //MSB = most significant bit
  int LSB = digitalRead(encoderPin2); //LSB = least significant bit

  int encoded = (MSB << 1) |LSB; //converting the 2 pin value to single number
  int sum  = (lastEncoded << 2) | encoded; //adding it to the previous encoded value

  if(sum == 0b1101 || sum == 0b0100 || sum == 0b0010 || sum == 0b1011) encoder0Value ++;
  if(sum == 0b1110 || sum == 0b0111 || sum == 0b0001 || sum == 0b1000) encoder0Value --;

  lastEncoded = encoded; //store this value for next time

  cev = encoder0Value;
  // Serial.println("ev: " + String(cev));
}


void right_hand() {
  // print_message("Right hand");

  // encoder0Value = 0;
  pev = encoder0Value;
  encoder0Value1 = 400;
  encoder0Value2 = 0;

  digitalWrite(right_hand_direction, HIGH);
  analogWrite(right_hand_pwm, hand_motor_pwm);

  while(true) {
    Serial.println(encoder0Value);
    if((abs(encoder0Value) < abs(pev) - encoder0Value1) || (abs(encoder0Value) > abs(pev) + encoder0Value1)) {
      break;
    }
  }

  analogWrite(right_hand_pwm, 0);
  Serial.println("reverse");
  delay(2000);

  digitalWrite(right_hand_direction, LOW);
  analogWrite(right_hand_pwm, hand_motor_pwm);

  pev = encoder0Value;

  while(true) {
    Serial.println(encoder0Value);
    if((abs(encoder0Value) < abs(pev) - encoder0Value1) || (abs(encoder0Value) > abs(pev) + encoder0Value1)) {
      break;
    }
  }

  analogWrite(right_hand_pwm, 0);
}
