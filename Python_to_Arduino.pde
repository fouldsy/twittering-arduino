int serialData;

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  // Check if there is data being to the serial port
  if (Serial.available() > 0)
  {
    
    // Read in the serial data, subtracting 48 to convert the ASCII code
    serialData = (Serial.read() - 48);
    
    // Switch statement (somewhat of a pun, given Python doesn't provide switch)
    switch (serialData) {
      
      // If the number 1 was sent, run function to turn lights on
      case 1:
        turnLightsOn();
        break;
        
      // If the number 2 was sent, run function to turn lights off
      case 2:
        turnLightsOff();
        break;
    }
  }  
}

// These functions can be greatly expanded upon, such as actually turning a light on or off
// This is just the framework. You could actually include this within the switch of if statements

void turnLightsOn() {
  Serial.println("Turn lights on");
}

void turnLightsOff() {
  Serial.println("Turn lights off");
}
