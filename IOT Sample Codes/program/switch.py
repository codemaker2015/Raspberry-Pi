import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
        while True:
            if (GPIO.input(37))==1:
                GPIO.output(40,True)
                
            else:
                GPIO.output(40,False)
                
except:
        KeyboardInterrupt()
        GPIO.cleanup()
