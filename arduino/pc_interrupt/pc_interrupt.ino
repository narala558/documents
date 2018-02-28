#include <PinChangeInterrupt.h>


const byte interruptPin = 53;
const byte interruptPin2 = 2;

const byte ledPin = 13;
volatile byte state = LOW;


void setup() {
  pinMode(ledPin, OUTPUT);

  pinMode(interruptPin, INPUT_PULLUP);
  pinMode(interruptPin2, INPUT_PULLUP);

  attachPinChangeInterrupt(digitalPinToPinChangeInterrupt(interruptPin), blink, CHANGE);
  attachInterrupt(digitalPinToInterrupt(interruptPin2), blink, CHANGE);
}


void loop() {
  digitalWrite(ledPin, state);
}


void blink() {
  state = !state;
}
