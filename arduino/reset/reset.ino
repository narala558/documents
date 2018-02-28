#include <avr/wdt.h>

void setup()
{
   wdt_enable(WDTO_8S);

}


void loop()
{
   wdt_reset();// make sure this gets called at least once every 8 seconds!
}
