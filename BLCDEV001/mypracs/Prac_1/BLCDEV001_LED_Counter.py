#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Devon Bloch>
Student Number: <BLCDEV001>
Prac: <1>
Date: <27/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
# Logic that you write
def main():
 	for i in range(0,10):	
		GPIO.output(17, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(17, GPIO.LOW)
		time.sleep(0.5)
	GPIO.cleanup()		


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
