from scrape import Measurement
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import sys


def updatePlot(i, meas, plotFigure, data_list, times, start, variable):
        now = datetime.datetime.now()
        if variable == "light":
                data_list.append((1024 - meas.get_light_level()) * 100 / 1024)
                label = "Light level (% of maximum)"
                title = "Light level vs Time"
        elif variable == "temp":
                data_list.append(meas.get_temp())
                label = "Temperature ($\degree$C)"
                title = "Temperature vs Time"
        else:
                raise InputError("didnt understand argv")
        diff = now - start
        times.append(diff.total_seconds())

        plotFigure.clear()

        plt.plot(times, data_list)
        plt.title(title)
        plt.xlabel("Time after start (s)")
        plt.ylabel(label)


def main():
        start = datetime.datetime.now()
        variable = sys.argv[1]
        plotFigure = plt.figure()
        meas = Measurement()
        data = []
        times = []
        ani = FuncAnimation(plotFigure, updatePlot, interval=10, fargs=(meas, plotFigure, data, times, start, variable))
        plt.show()


main()
