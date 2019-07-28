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
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)


GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
number = 0

def increment(channel):
	global number
	number = (0 if number == 7 else (number+1))
	print("Decimal Number: "+str(number))
	bin_arr = list(str(bin(number)))
	print("Binary Number: "+str(bin_arr))
	GPIO.output(17,int(bin_arr[-1]))
	GPIO.output(27,int(0 if bin_arr[-2]== 'b' else bin_arr[-2]))
	GPIO.output(22,int(0 if bin_arr[-3]== 'b' else bin_arr[-3]))
def decrement(channel):
	global number
	
	number = 7 if number == 0 else number-1
	print("Decimal Number: "+str(number))
        bin_arr = list(str(bin(number)))
	print("Binary Number: "+str(bin_arr))
        GPIO.output(17,int(bin_arr[-1]))
        GPIO.output(27,int(0 if bin_arr[-2]== 'b' else bin_arr[-2]))
        GPIO.output(22,int(0 if bin_arr[-3]== 'b' else bin_arr[-3]))
	
GPIO.add_event_detect(23,GPIO.RISING, callback=increment, bouncetime=300)
GPIO.add_event_detect(24,GPIO.RISING, callback=decrement, bouncetime=300)
	
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
