// Define the pin numbers for each component
const int ledPin = 11;
const int pirPin = 7;
const int ldrPin = 8; // Digital pin for the LDR's DO pin

// The setup function runs once when the Arduino is powered on.
void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);
  
  // Set the LED pin as an OUTPUT
  pinMode(ledPin, OUTPUT);
  // Set both sensor pins as INPUT
  pinMode(pirPin, INPUT);
  pinMode(ldrPin, INPUT);
}

// The loop function runs over and over again forever.
void loop() {
  // Read the current values from the sensors
  int ldrValue = digitalRead(ldrPin);
  int pirValue = digitalRead(pirPin);

  // Print the sensor values to the Serial Monitor for debugging
  Serial.print("Light (LDR): ");
  Serial.print(ldrValue);
  Serial.print(" | Motion (PIR): ");
  Serial.println(pirValue);

  // The core logic: check if it's dark AND if motion is detected
  // For most modules, LOW = DARK. If yours is opposite, change ldrValue == LOW to ldrValue == HIGH
  if (ldrValue == HIGH && pirValue == HIGH) {
    // If both conditions are true, turn the LED ON
    digitalWrite(ledPin, HIGH);
    Serial.println("Street Light: ON");
  } else {
    // If either condition is false, turn the LED OFF
    digitalWrite(ledPin, LOW);
    Serial.println("Street Light: OFF");
  }

  // A small delay to keep the Serial Monitor from cluttering up
  delay(1000);
}
