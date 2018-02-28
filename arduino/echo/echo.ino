char data = 'a';

char noData = '........';


void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }
}


void loop() {
  if (Serial.available() > 0) {
    data = Serial.read();
    Serial.write(data);
  }
}
