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


temp_data = []
humidity_data = []

# terminal command
print('Press Ctrl-C to quit.')

while True:

    # getting temp and humidity data from server
    temp = meas.get_temp()
    humidity = meas.get_humidity()
    


    # skip loop initally as theres not enough data to determine std
    if (len(temp_data)==1 or len(humidity_data)==1): continue 

    # setting LCD color
    lcd.set_color(0,0,1)

    # displaying temp and humidity data to LCD
    lcd.message(f'Temp: {np.round(temp, 2)}C \nHumidity: {np.round(humidity, 2)}%')

    # setting display time on LCD so it doesn't vanish to quickly, i.e. make it readable
    time.sleep(3.0)
    
    # clearing display    
    lcd.clear()

    # telling user to press select button for stdv
    lcd.message('Press select button for data analysis')
    time.sleep(3.0)
    lcd.clear()

    # setting time duration of loop to check if buttons are being pressed
    # checks for 10s then breaks 
    timeout = time.time() + 10

    # checks buttons are being pressed for 10s
    while True:

        # breaks out of loop after 10s
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

