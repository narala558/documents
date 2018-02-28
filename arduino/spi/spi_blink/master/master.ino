#include <SPI.h>


void setup (void) {
  Serial.begin(115200);
  Serial.println();

  digitalWrite(SS, HIGH);  // ensure SS stays high for now
  SPI.begin ();

  // Slow down the master a bit
  SPI.setClockDivider(SPI_CLOCK_DIV8);

  pinMode(LED_BUILTIN, OUTPUT);
}  // end of setup


byte transferAndWait (const byte what) {
  byte a = SPI.transfer (what);
  delayMicroseconds (20);
  return a;
} // end of transferAndWait


void loop (void) {

  byte a, b, c, d;

  // enable Slave Select
  digitalWrite(SS, LOW);

  int i = random(0, 100);
  int r;

  if(i%2==0) {
    r=0;
    digitalWrite(LED_BUILTIN, LOW);
  }else {
    r=1;
    digitalWrite(LED_BUILTIN, HIGH);
  }
  transferAndWait(r);

  digitalWrite(SS, HIGH);

  Serial.println (i);

  delay (2000);  // 1 second delay
}  // end of loop
