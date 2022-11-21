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

# stores all data in one row, order --> temp, humidity, light data
temp_data = []
humidity_data = []
light_data = []


def buttonPress(lcd):

     # create sun custom characters
    lcd.create_char(1, [5,3,7,31,7,3,5])
    lcd.create_char(2, [18,28,24,31,24,28,18])

    lcd.create_char(3, [0, 14, 21, 23, 17, 14, 0, 0])
    lcd.create_char(4, [31, 17, 10, 4, 10, 17, 31, 0])
    lcd.create_char(5, [8, 12, 10, 9, 10, 12, 8, 0])
    lcd.create_char(6, [2, 6, 10, 18, 10, 6, 2, 0])
    lcd.create_char(7, [31, 17, 21, 21, 21, 21, 17, 31])

    # setting buttons
    # Make list of button value, text, and backlight color.
    buttons = ( (LCD.SELECT, '\x01\x02', (1,1,1)),
              (LCD.LEFT,   'Left'  , (1,0,0)),
              (LCD.UP,     'Up'    , (0,0,1)),
              (LCD.DOWN,   'Down'  , (0,1,0)),
              (LCD.RIGHT,  'Right' , (1,0,1)) )

    # setting time period to loop over to check buttons
    seconds = 2
    timeout = time.time() + seconds

    while time.time() <= timeout:
    
   # Loop through each button and check if it is pressed.
        for button in buttons:
            if lcd.is_pressed(button[0]):
                # Button is pressed, change the message and backlight.
                lcd.clear()
                lcd.message(button[1])
                lcd.set_color(button[2][0], button[2][1], button[2][2])



while True:

    # clear screen every iteration
    lcd.clear()    

    # getting temp and humidity data from server
    temp = meas.get_temp()
    humidity = meas.get_humidity()
    light = meas.get_light_level()

    # adding all data to list
    temp_data.append(temp)
    humidity_data.append(humidity)
    light_data.append(light)

    # skip loop initally as theres not enough data to determine std
    if (len(temp_data)==1 or len(humidity_data)==1): continue 

    # setting LCD color
    lcd.set_color(1,0,0)

    # Display Temp Data to LCD screen for 3s
    lcd.message(f'Temp: {np.round(temp, 2)}C \nStdv: {np.r(temp)}%')
    buttonPress(lcd)
    time.sleep(3.0)  
    lcd.clear()

    # Display humidity Data to LCD screen for 3s
    lcd.message(f'Humidity: {np.round(humidity, 2)}C')
    buttonPress(lcd)
    time.sleep(3.0)  
    lcd.clear()

    # Display current light level Data to LCD screen for 3s
    if (light[-1] < 280):
        light_statment = "It is bright"
    else:
        light_statment = "It is dark"

    lcd.message(f'Light Level: {np.round(light, 2)} \n{light_statment}')
    buttonPress(lcd)
    time.sleep(3.0)  
    lcd.clear()


    # terminal command
    print('Press Ctrl-C to quit.')
