from scrape import Measurement
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def updatePlot(i, meas, plotFigure, temps, hums):
        temps.append(meas.get_temp())
        hums.append(meas.get_humidity())

        plotFigure.clear()

        plt.scatter(hums, temps)
        plt.title("Temperature vs Humidity")
        plt.xlabel("Humidity (%)")
        plt.ylabel("Temperature (degrees Celsius)")


def main():
        plotFigure = plt.figure()
        meas = Measurement()
        temps = []
        hums = []
        ani = FuncAnimation(plotFigure, updatePlot, interval=10, fargs=(meas, plotFigure, temps, hums))
        plt.show()


main()
