const int Echo1 = 5;
const int Trigger1 = 6;
const int Echo2 = 11;
const int Trigger2 = 3;
int distanciaPrimer;
int distanciaSegundo;
int DIRA1 = 9;
int DIRB1 = 10;
int DIRA2 = 12;
int DIRB2 = 13;

int ENABLE1 = 7;
int ENABLE2 = 8;

void setup() {
	Serial.begin(9600);
	pinMode(Trigger1,OUTPUT);
	pinMode(Echo1,INPUT);
 	pinMode(Trigger2,OUTPUT);
	pinMode(Echo2,INPUT);
	
  	digitalWrite(Trigger1,LOW);
	digitalWrite(Trigger2,LOW);
  	
  	pinMode(ENABLE1,OUTPUT);
  	pinMode(DIRA1,OUTPUT);
  	pinMode(DIRB1,OUTPUT);
  	
  	pinMode(ENABLE1,OUTPUT);
  	pinMode(DIRA1,OUTPUT);
  	pinMode(DIRB1,OUTPUT);
  
  	digitalWrite(ENABLE1,HIGH);
	digitalWrite(ENABLE2,HIGH);
}

int detecta_primerSensor() {
	long t;
  	long d;
 	digitalWrite(Trigger1,LOW);
 	delayMicroseconds(5);
 	digitalWrite(Trigger1,HIGH);
 	delayMicroseconds(15);
 	digitalWrite(Trigger1,LOW);
 	t=pulseIn(Echo1,HIGH);
 	d=t*0.01657;
 	return (d);
}

int detecta_segundoSensor() {
	long t;
  	long d;
 	digitalWrite(Trigger2,LOW);
 	delayMicroseconds(5);
 	digitalWrite(Trigger2,HIGH);
 	delayMicroseconds(15);
 	digitalWrite(Trigger2,LOW);
 	t=pulseIn(Echo2,HIGH);
 	d=t*0.01657;
 	return (d);
}

void loop() {
	distanciaPrimer=detecta_primerSensor();
  	distanciaSegundo=detecta_segundoSensor();
 	Serial.print("Distancia primer ultrasonido: ");
 	Serial.print(distanciaPrimer);
 	Serial.println ("cm");
	Serial.print("Distancia segundo ultrasonido: ");
 	Serial.print(distanciaSegundo);
 	Serial.println ("cm");
  
  if(distanciaPrimer>distanciaSegundo && distanciaPrimer>30){
    digitalWrite(DIRA1, LOW);
  	digitalWrite(DIRB1, HIGH);
    digitalWrite(DIRA2, HIGH);
  	digitalWrite(DIRB2, LOW);
  }else if (distanciaPrimer<distanciaSegundo && distanciaSegundo>30){
    digitalWrite(DIRA1, HIGH);
  	digitalWrite(DIRB1, LOW);
    digitalWrite(DIRA2, LOW);
  	digitalWrite(DIRB2, HIGH);
  }else {
    digitalWrite(DIRA1, LOW);
  	digitalWrite(DIRB1, LOW);
    digitalWrite(DIRA2, LOW);
  	digitalWrite(DIRB2, LOW);
  }
  
 	delay(1000);
}

/*

void setup(){
  
}

void loop(){
  
}*/