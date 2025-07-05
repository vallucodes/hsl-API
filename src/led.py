from machine import Pin, PWM
from time import sleep

# Define the GPIO pins for the RGB LED
PIN_RED = 21   # ESP32 pin GPIO23 connected to the LED's red pin
PIN_GREEN = 19 # ESP32 pin GPIO22 connected to the LED's green pin
PIN_BLUE  = 18 # ESP32 pin GPIO21 connected to the LED's blue pin

# Initialize the pins as PWM outputs
red = PWM(Pin(PIN_RED))
green = PWM(Pin(PIN_GREEN))
blue = PWM(Pin(PIN_BLUE))

# Set the PWM frequency to 1000 Hz (you can adjust this as needed)
red.freq(1000)
green.freq(1000)
blue.freq(1000)

def setColor(r, g, b):
	# Set the duty cycle for each color channel
	red.duty_u16(int(r * 65535 / 255))
	green.duty_u16(int(g * 65535 / 255))
	blue.duty_u16(int(b * 65535 / 255))
