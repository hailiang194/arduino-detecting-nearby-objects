#include <Servo.h>
#define MAX_DIS 100
#define INFINITY 10000
#define TRIG 8
#define ECHO 7
#define SERVO 3
#define TIME_DELAY 100
Servo servo;

void write_data_at(int angle)
{
    servo.write(angle);
    Serial.print(angle);
    Serial.print(":");
    int distance = get_distance();
    if((distance == 0) || (distance > MAX_DIS))
      distance = INFINITY;
    Serial.println(distance);
    
}

int get_distance()
{
  long duration;
  int distanceCm;
       
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
      
  duration = pulseIn(ECHO, HIGH, 5000);
     
  // convert to distance
  distanceCm = duration / 29.1 / 2;
      
  return distanceCm;
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  servo.attach(SERVO);
  servo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
 
    for(int i = 0; i <= 180; i += 2)
  {
    write_data_at(i);
    delay(TIME_DELAY);
  }

  for(int i = 178; i >= 2; i -= 2)
  {
    write_data_at(i);
    delay(TIME_DELAY);
  }

}
