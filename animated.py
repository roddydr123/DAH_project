from scrape import Measurement
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import sys


def updatePlot(i, meas, plotFigure, data_list, times, start, variable):
        """Refresh the plot with new data pulled from the Arduino webserver."""
        
        # Fetch and store the current time so that the timestamp of the data can
        # be determined.
        now = datetime.datetime.now()

        # Check whether it's supposed to plot temperature or light level over time
        # by referring to the command line argument stored in "variable".
        if variable == "light":
                # meas.get_light_level() returns the light level as an integer between 0
                # and 1024 (bright -> dark). This converts the integer into a percentage
                # of the maximum possible light level.
                data_list.append((1024 - meas.get_light_level()) * 100 / 1024)

                # Make appropriate labels for the plot.
                label = "Light level (% of maximum)"
                title = "Light level vs Time"
        elif variable == "temp":
                # The temperature does not need to be converted.
                data_list.append(meas.get_temp())
                label = "Temperature ($\degree$C)"
                title = "Temperature vs Time"
        else:
                # If an unrecognised command line argument is found, raise an error.
                raise ValueError("didnt understand argv")

        # Find how much time has passed since the script has been running and save
        # it in a list.
        diff = now - start
        times.append(diff.total_seconds())

        # Empty the matplotlib figure so that it can be updated with new data.
        plotFigure.clear()

        # Plot the new data with appropriate labelling.
        plt.plot(times, data_list)
        plt.title(title)
        plt.xlabel("Time after start (s)")
        plt.ylabel(label)


def main():
        # Store the time which the script starts as a reference.
        start = datetime.datetime.now()

        # Plotting the temperature "temp" or light level "light" must be
        # passed as a command line argument.
        variable = sys.argv[1]

        plotFigure = plt.figure()

        # Create an instance of the Measurement object which allows requests to be
        # sent to the Arduino webserver.
        meas = Measurement()

        # Empty lists to store data from the webserver and time stamp.
        data = []
        times = []

        # Repeatedly calls updatePlot() to gather new data from the web server. The
        # new data is plotted on plotFigure.
        ani = FuncAnimation(plotFigure, updatePlot, interval=10, fargs=(meas, plotFigure, data, times, start, variable))
        plt.show()


main()
