#
# motor.py
# Authors:
#   Sergio Corral
#

import RPi.GPIO as GPIO
from time import sleep


class Motor:
    def __init__(self, a, b, c):
        self.MOTOR1A = a
        self.MOTOR1B = b
        self.MOTOR1C = c
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.MOTOR1A, GPIO.OUT)
        GPIO.setup(self.MOTOR1B, GPIO.OUT)
        GPIO.setup(self.MOTOR1C, GPIO.OUT)
        GPIO.setup(40, GPIO.OUT)

        GPIO.output(40, GPIO.HIGH)

        # GPIO.setmode(GPIO.BOARD)

    def runMotor(self, timeToRun):
        print("Turning motor on")

        GPIO.output(self.MOTOR1A, GPIO.HIGH)
        GPIO.output(self.MOTOR1B, GPIO.LOW)
        GPIO.output(self.MOTOR1C, GPIO.HIGH)

        blinkTime = 1
        i = 0

        while i < timeToRun:
            GPIO.output(40, GPIO.LOW)
            sleep(blinkTime)
            i = i + 1

            if i != timeToRun:
                GPIO.output(40, GPIO.HIGH)
                sleep(blinkTime)
                i = i + 1

        print("Stopping motor")

        GPIO.output(self.MOTOR1C, GPIO.LOW)
        # GPIO2.setmode(GPIO.BCM)
        GPIO.output(40, GPIO.LOW)

        GPIO.cleanup()
