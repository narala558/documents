int command;

void setup() {
  Serial.begin(9600);
  print("start");
}


void loop() {
  exec_serial_commands();
}


int exec_serial_commands() {

  command = 0;

  if (Serial.available()) {
    command = Serial.parseInt();
  }

  if(command != 0) {
    print(String(command));
  }

  return command;
}


void print(String msg) {
  Serial.println(msg);
}
