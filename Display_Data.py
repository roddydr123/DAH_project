#!/usr/bin/python
# Example using a character LCD plate.
import time
import Adafruit_CharLCD as LCD
from scrape.py import Measurement

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# class for scraping data from server
meas = Measurement

# custom button inputs
std = f'Temp stdv: {0}   Humidity stdv: {0}'


# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, std, (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

colors_ls = [(1,0,0), (0,1,0), (0,0,1)]
i = 0

while True:

    # getting temp and humidity data from server
    temp = meas.get_temp()
    humidity = meas.get_humidity()
<<<<<<< Updated upstream
=======
    
    # skip loop initally as theres not enough data to determine std
    if (len(temp_data)==1 or len(humidity_data)==1): continue 
>>>>>>> Stashed changes

    # setting LCD color
    lcd.set_color(colors_ls[i])
    i += 1
    i = i%3

    lcd.message(f'Temp: {temp}   Humidity: {humidity}')
    # setting display time on LCD
    time.sleep(3.0)

    # telling user to press buttons
    lcd.message('Press buttons...')

    # terminal command
    print('Press Ctrl-C to quit.')


    # Loop through each button and check if it is pressed.
    for button in buttons:
            if lcd.is_pressed(button[0]):
                    # Button is pressed, change the message and backlight.
                    lcd.clear()
                    lcd.message(button[1])
                    lcd.set_color(button[2][0], button[2][1], button[2][2])