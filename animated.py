from scrape import Measurement
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import sys


def updatePlot(i, meas, plotFigure, data_list, times, start, variable):
        now = datetime.datetime.now()
        if variable == "light":
                data_list.append(meas.get_light_level())
        elif variable == "temp":
                data_list.append(meas.get_temp())
        else:
                raise InputError("didnt understand argv")
        diff = now - start
        times.append(diff.total_seconds())

        plotFigure.clear()

        plt.plot(times, data_list)
        plt.title(f"{variable} vs Time")
        plt.xlabel("Time after start (s)")
        plt.ylabel(f"{variable}")


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
