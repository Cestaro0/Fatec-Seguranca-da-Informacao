```c++
int redLed1 = 7;
int redLed2 = 4;

int orangeLed1 = 6;
int orangeLed2 = 3;

int greenLed1 = 5;
int greenLed2 = 2;




void setup()
{
  pinMode(redLed1, OUTPUT);
  pinMode(redLed2, OUTPUT);
  
  pinMode(orangeLed1, OUTPUT);
  pinMode(orangeLed2, OUTPUT);
  
  pinMode(greenLed1, OUTPUT);
  pinMode(greenLed1, OUTPUT);
}

void loop()
{
 digitalWrite(redLed1, HIGH);
 digitalWrite(greenLed2, HIGH);
  
 delay(1000);
  
  digitalWrite(redLed1, LOW);
 digitalWrite(greenLed2, LOW);
  
  delay(1000);
    
 digitalWrite(orangeLed1, HIGH);
 digitalWrite(orangeLed2, HIGH);
  
  delay(1000);
   digitalWrite(orangeLed1,LOW);
 digitalWrite(orangeLed2, LOW);
  
  delay(1000);
  
  digitalWrite(greenLed1, HIGH);
  digitalWrite(redLed2, HIGH);
 
 delay(1000);
    digitalWrite(greenLed1, LOW);
  digitalWrite(redLed2, LOW);
  
  delay(1000);
}
```
