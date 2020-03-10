"""
The Store is used to represent a the physical store in the model.
The Store orchestrates the operations of the other classes.
"""
from CustomerAgent import CustomerAgent, choose_checkout
from EmployeeCheckOutAgent import EmployeeCheckOutAgent
from SelfCheckOutAgent import SelfCheckOutAgent
from random import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from constants import *
import numpy as np

from createCustomers import createCustomers


class Store(object):
    # Constructor
    def __init__(self, n):
        self.time_of_day = 0            # this is number of seconds into the day
        self.time_of_hour = 0           # this is the number of seconds into the hour
        self.remainderTimeSum = 0       # this is to keep track of the remainder time between customers
        self.hour = 0
        self.timeDif = self.timeBetweenCustomers(self.hour)

        self.store = []
        self.fig = plt.figure()
        self.simCustomers = createCustomers()

        for i in range(n):
            checkout = EmployeeCheckOutAgent(
                i * (EMPLOYEE_WIDTH + SPACE_BETWEEN)) if random() < .5 else SelfCheckOutAgent(
                i * (SELF_WIDTH + SPACE_BETWEEN))
            self.store.append(checkout)

        self.grid = self.init_grid()
        self.im = plt.imshow(self.grid, animated=True)
        self.ani = FuncAnimation(self.fig, self.updateSimulation, interval=100, blit=True)
        plt.show()

    def run_step(self):
        """
        run_step increments the internal timer by one tick, as well as calling the methods
          offered by its internal variables in order to advance the simulation.
        Precondition: The store has not been modified by external programs.
        Postcondition: A single tick has occurred in the simulated environment, customers generated, checkouts changed.
        Return: self
        """

        numNewCustomers = 0                         # this is the number of customers added during this tick

        if self.time_of_hour / self.timeDif[0] is 0:    # if the time between customers arriving has elapsed

            numNewCustomers += 1
            self.remainderTimeSum += self.timeDif[1]

        # if the fractional time has added up to one or more, then account for remainder sec/customer generation
        if self.remainderTimeSum >= 1.0:
            numNewCustomers += 1
            self.remainderTimeSum -= 1

        for newCustomer in range(numNewCustomers):      # for the number of customers to be generated
            customer = CustomerAgent()
            lane = choose_checkout(self.store)          # chooses the register number to go to
            self.store[lane].addToLine(customer)        # adds the customer to the register object

        for i, each in enumerate(self.store):
            print(f"Processing line {i} of {len(self.store)}")
            each.process()

        for register in self.store:
            self.grid = register.display_line(self.grid)

        self.time_of_day += 1                               # the time of the day increments by one
        if self.time_of_hour is not SECONDS_IN_HOUR:        # if still in the hour
            self.time_of_hour += 1
        else:                                               # else it is the top of the next hour
            self.hour = self.time_of_day / SECONDS_IN_HOUR  # finds the current hour of the day the simulator is at

            # timeDIf is a tuple, first element is the even ticks between people
            # second element is the remainder time
            self.timeDif = self.timeBetweenCustomers(self.hour)

            self.time_of_hour = 0                           # restarts the hourly clock, which is in seconds

    def timeBetweenCustomers(self, hour):
        exactTime = SECONDS_IN_HOUR / self.simCustomers(hour)  # number of ticks between integer division of customers
        remainderTime = SECONDS_IN_HOUR % self.simCustomers(hour)
        return [exactTime, remainderTime]

    # Initializes the visualization grid 
    def init_grid(self):
        grid = np.ones((WIDTH, LENGTH, 3))
        index = 0
        for station in self.store:

            visuals = station.visual_attributes()
            for y in range(visuals[1][0]):
                for x in range(station.x, station.x + SELF_WIDTH):
                    grid[y][x] = visuals[0]
            index += 1
        return grid

    def updateSimulation(self, *args):
        self.run_step()
        self.im.set_array(self.grid)
