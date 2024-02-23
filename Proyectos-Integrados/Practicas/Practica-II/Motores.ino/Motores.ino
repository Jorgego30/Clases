const int DIRA1 = 6;
const int DIRB1 = 7;
const int DIRA2 = 8;
const int DIRB2 = 9;

const int ENABLE1 = 5;
const int ENABLE2 = 10;

void setup() {
  Serial.begin(9600);

  pinMode(ENABLE1, OUTPUT);
  pinMode(DIRA1, OUTPUT);
  pinMode(DIRB1, OUTPUT);

  pinMode(ENABLE2, OUTPUT);
  pinMode(DIRA2, OUTPUT);
  pinMode(DIRB2, OUTPUT);

  digitalWrite(ENABLE1, HIGH);
  digitalWrite(ENABLE2, HIGH);
}

void loop() {
  digitalWrite(DIRA1, HIGH);
  digitalWrite(DIRB1, HIGH);
  digitalWrite(DIRA2, LOW);
  digitalWrite(DIRB2, LOW);
}