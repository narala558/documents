int command;


void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  Serial2.begin(9600);
  Serial3.begin(9600);
  print("start");
}


void loop() {
  exec_serial_commands();
  ping();
}


int exec_serial_commands() {

  command = 0;

  if (Serial.available()) {
    command = Serial.parseInt();
  }

  if (Serial1.available()) {
    command = Serial1.parseInt();
  }

  // if (Serial2.available()) {
  //   command = Serial2.parseInt();
  // }

  // if (Serial3.available()) {
  //   command = Serial3.parseInt();
  // }

  // if(command != 0) {
  //   print(String(command));
  // }

  return command;
}


void print(String msg) {
  Serial.println(msg);
  // Serial1.println(msg);
  // Serial2.println(msg);
  // Serial3.println(msg);
}

int counter=0;

void ping() {
  int seconds = millis()/1000;
  if(seconds>counter){
    print("ping " + String(seconds));
    counter= seconds;
  }
}
