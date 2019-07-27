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
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def toggle_on(channel):
	GPIO.output(17, 1)
def toggle_off(channel):
	GPIO.output(17,0)
GPIO.add_event_detect(18,GPIO.RISING, callback=toggle_on, bouncetime=300)

	
# Logic that you write
def main():
	state = 0
	
 	message = input("Press enter to quit\n\n") # Run until someone presses enter
	GPIO.cleanup() # Clean up		


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
    finally:
	GPIO.cleanup()	
