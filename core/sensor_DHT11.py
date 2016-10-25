#For now only LED blink test
import RPi.GPIO as GPIO
import time

def blink():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    for x in range(2):
        GPIO.output(7, True)
        time.sleep(1)
        GPIO.output(7, False)
        time.sleep(1)
    print("Done")
    GPIO.cleanup()
