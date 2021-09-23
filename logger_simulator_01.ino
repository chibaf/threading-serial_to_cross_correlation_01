const int na=100;
float a[na],b[na];

void setup() {
  // initialize serial comms
  Serial.begin(19200);
// signal 1
  for (int i = 0; i < na; i = i + 1) {
  a[i]=20.0;
 }
  for (int i = 0; i < 10; i = i + 1) {
  a[i]=20.0+(0.5/9)*i;
 }
  for (int i = 0; i < 10; i = i + 1) {
  a[i+10]=20.5-(0.5/9)*i;
 }
// signal 2
  float swap;
  for (int i = 0; i < na; i = i + 1) {  // copy a->b
    b[i]=a[i];
 }
 for (int j=0;j<50;j=j+1){  // shift right 50
  swap=b[na-1];
  for (int i = 1; i < na; i = i + 1) {
    b[na-i]=b[na-i-1] ;
  }
  b[0]=swap;
  }
}

//// print signals
void loop() {
  unsigned mtime;
  // shift right 1
  float temp1 = a[na - 1];   
  float temp2 = b[na - 1];
  for (int i = na - 1; i > 0; i--) 
    {a[i] = a[i - 1];b[i] = b[i - 1];}
  a[0] = temp1;b[0] = temp2;
  // print temps at 2points
  mtime=millis();
  Serial.print(mtime);
  Serial.print(",");
  Serial.print(a[29]);
  Serial.print(",");
  Serial.print(b[29]);
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.println();
  delay(100);
}
