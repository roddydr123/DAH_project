# Arduino remote weather station

An arduino set up with light and temperature sensors which updates a local web server allowing data to be read remotely. A raspberry Pi accessed the data and displayed it on an LCD screen.

* `animated.py` creates and updates a plot of temperature or light level over time depending on the command line argument passed.
* `Display_Data_prime.py` reads weather data and displays it on the LCD.
* `scrape.py` contains a class for requesting weather data from the web server.
* `wifi.ino` arduino code for collecting sensor data and making it available on an embedded web server. Only lightly modified from the original cited in the report.
