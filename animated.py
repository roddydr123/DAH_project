from scrape import Measurement
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime


def updatePlot(i, meas, plotFigure, temps, times, start):
        now = datetime.datetime.now()
        temps.append(meas.get_temp())
        diff = now - start
        times.append(diff.total_seconds())

        plotFigure.clear()

        plt.scatter(times, temps)
        plt.title("Temperature vs time")
        plt.xlabel("Time after start (s)")
        plt.ylabel("Temperature (degrees Celsius)")


def main():
        start = datetime.datetime.now()
        plotFigure = plt.figure()
        meas = Measurement()
        temps = []
        times = []
        ani = FuncAnimation(plotFigure, updatePlot, interval=10, fargs=(meas, plotFigure, temps, times, start))
        plt.show()


main()
