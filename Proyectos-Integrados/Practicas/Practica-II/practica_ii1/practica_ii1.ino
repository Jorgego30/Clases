int DIRA1 = 9;
int DIRB1 = 10;

int ENABLE2 = 8;

void setup() {
	Serial.begin(9600);
  	pinMode(DIRA1,OUTPUT);
  	pinMode(DIRB1,OUTPUT);
  	
  	pinMode(ENABLE2,OUTPUT);
  
	digitalWrite(ENABLE2,HIGH);
}

void loop() {
  
  digitalWrite(DIRA1, HIGH);
  digitalWrite(DIRB1, LOW);
}

/*

void setup(){
  
}

void loop(){
  
}*/
