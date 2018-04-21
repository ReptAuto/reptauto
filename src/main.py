from motor import Motor

# Numbers are pins on the breadboard
test = Motor(16,18,22)

#Parameter is in seconds
test.runMotor(10)
