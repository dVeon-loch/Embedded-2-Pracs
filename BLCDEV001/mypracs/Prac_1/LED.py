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
# Set up the required number of GPIO Pins for LEDs
GPIO.setmode(GPIO.BCM)		#Set pin numbering system to BCM
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)	#Set initial state to LOW to prevent LEDs being on at setup
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

# Set up the required number of pins for the pushbuttons
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)	#Set internal resistors to pull-down
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

number = 0	#Create global number variable to keep track of current number

def increment(channel):	#defining a callback increment function
	global number	#using the 'global' construct to use/change the number variable created above
	number = (0 if number == 7 else (number+1))	#Ternary operator to handle overflow/wrapping or increment
	print("Decimal Number: "+str(number))	#Print out decimal number for viewing or debugging if necessary
	bin_arr = list(str(bin(number)))	#Convert decimal number to binary, then split into an array
	print("Binary Number: "+str(bin_arr))	#Print out binary number array for viewing or debugging if necessary
	GPIO.output(17,int(bin_arr[-1]))
	GPIO.output(27,int(0 if bin_arr[-2]== 'b' else bin_arr[-2]))	#Ternary operator to handle the binary 'b'
	GPIO.output(22,int(0 if bin_arr[-3]== 'b' else bin_arr[-3]))
def decrement(channel):	#defining a callback decrement function
	global number
	
	number = 7 if number == 0 else number-1
	print("Decimal Number: "+str(number))
        bin_arr = list(str(bin(number)))
	print("Binary Number: "+str(bin_arr))
        GPIO.output(17,int(bin_arr[-1]))
        GPIO.output(27,int(0 if bin_arr[-2]== 'b' else bin_arr[-2]))
        GPIO.output(22,int(0 if bin_arr[-3]== 'b' else bin_arr[-3]))
#Adding interrupt functionality for increment and decrement	
GPIO.add_event_detect(23,GPIO.RISING, callback=increment, bouncetime=300)	#Using 'bouncetime' for debounce
GPIO.add_event_detect(24,GPIO.RISING, callback=decrement, bouncetime=300)
	
def main():
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
	GPIO.cleanup()	#Added the cleanup in 'finally' to solve cleanup issues
