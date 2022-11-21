#!/usr/bin/python
# Example using a character LCD plate.
import time
import Adafruit_CharLCD as LCD

from scrape import Measurement
import numpy as np


# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# class for scraping data from server
meas = Measurement()

# custom button inputs
std = f'Temp stdv: {0} \nHumidity stdv: {0}'


# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, std, (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

while True:

    # getting temp and humidity data from server
    temp = meas.get_temp()
    humidity = meas.get_humidity()

    # skip loop initally as theres not enough data to determine std
    if (len(temp_data)==1 or len(humidity_data)==1): continue 


    # setting LCD color
    lcd.set_color(1,0,0)

    # Display Data to LCD screen for 3s
    lcd.message(f'Temp: {np.round(temp, 2)}C \nHumidity: {np.round(humidity, 2)}%')
    time.sleep(3.0)  
    lcd.clear()

    # telling user to press buttons for 3s
    lcd.message('Press buttons...')
    time.sleep(3.0)
    lcd.clear()
    
    # terminal command
    print('Press Ctrl-C to quit.')

    # setting time period to loop over to check buttons
    timeout = time.time() + 10

    while True:
        test = 0
    if time.time() > timeout:
	    break
    test = test - 1
	# Loop through each button and check if it is pressed.
    for button in buttons:
        if lcd.is_pressed(button[0]):
            # Button is pressed, change the message and backlight.
            lcd.clear()
            lcd.message(button[1])
            lcd.set_color(button[2][0], button[2][1], button[2][2])
