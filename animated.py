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

        plt.plot(times, temps)
        plt.title("Temperature vs Time")
        plt.xlabel("Time after start (s)")
        plt.ylabel("Temperature ($\degree$C)")


def main():
        start = datetime.datetime.now()
        plotFigure = plt.figure()
        meas = Measurement()
        temps = []
        times = []
        ani = FuncAnimation(plotFigure, updatePlot, interval=10, fargs=(meas, plotFigure, temps, times, start))
        plt.show()


main()
