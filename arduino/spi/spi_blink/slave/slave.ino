// what to do with incoming data
volatile byte command = 0;


void setup (void) {

  // have to send on master in, *slave out*
  pinMode(MISO, OUTPUT);

  // turn on SPI in slave mode
  SPCR |= _BV(SPE);

  // turn on interrupts
  SPCR |= _BV(SPIE);

  Serial.begin(115200);
  Serial.println("slave");
  pinMode(LED_BUILTIN, OUTPUT);
}  // end of setup


// SPI interrupt routine
ISR (SPI_STC_vect)
{
  byte c = SPDR;

  Serial.println(c);

  switch (c)
    {
      // no command? then this is the command
    case 0:
      Serial.println("==0");
      digitalWrite(LED_BUILTIN, LOW);
      break;

      // add to incoming byte, return result
    case 1:
      digitalWrite(LED_BUILTIN, HIGH);
      break;

      // subtract from incoming byte, return result
    default:
      Serial.println(c);
      break;

    } // end of switch

}  // end of interrupt service routine (ISR) SPI_STC_vect

void loop (void)
{

  // if SPI not active, clear current command
  if (digitalRead (SS) == HIGH)
    command = 2;
}  // end of loop
