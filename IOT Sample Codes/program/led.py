import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

try:
        while True:
                GPIO.output(21,True)
                time.sleep(5)
                GPIO.output(21,False)
                time.sleep(2)
except:
        KeyboardInterrupt()
        GPIO.cleanup()
