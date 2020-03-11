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
        self.remainderTimeSum = 0       # this is to keep track of the remainder simTime between customers
        self.hour = 0

        
        self.simCustomers, self.totalCustomers = createCustomers()
        self.timeDif = self.timeBetweenCustomers(self.hour)

        self.store = []
        # self.fig = plt.figure()

        for i in range(n):
            checkout = EmployeeCheckOutAgent(i * (EMPLOYEE_WIDTH + SPACE_BETWEEN), 0)
            # if random() < .5 else SelfCheckOutAgent(i * (SELF_WIDTH + SPACE_BETWEEN))
            self.store.append(checkout)

        self.grid = self.init_grid()

    def run_step(self):
        """
        run_step increments the internal timer by one tick, as well as calling the methods
          offered by its internal variables in order to advance the simulation.
        Precondition: The store has not been modified by external programs.
        Postcondition: A single tick has occurred in the simulated environment, customers generated, checkouts changed.
        Return: self
        """

        numNewCustomers = 0                         # this is the number of customers added during this tick

        if self.time_of_hour % self.timeDif[0] == 0:    # if the simTime between customers arriving has elapsed

            numNewCustomers += 1
            self.remainderTimeSum += self.timeDif[1]

        # if the fractional simTime has added up to one or more, then account for remainder sec/customer generation
        if self.remainderTimeSum >= 1.0:

            # add a new customer due to the fractional customers adding up to 1, similar to leap day
            numNewCustomers += 1

            # reduces the remainder by 1 instead of setting to zero, to account for some leftover simTime that could add up
            self.remainderTimeSum -= 1

        # for the number of customers to be generated
        for newCustomer in range(numNewCustomers):
            # the customers spawn opposite the registers, and randomly spaced along that border
            rowPosition = np.random.randint(0, LENGTH)

            # generates the customer along the bottom row, randomly placed
            customer = CustomerAgent(rowPosition, WIDTH - 1)

            # chooses the register number to go to
            lane = choose_checkout(self.store)

            # adds the customer to the register object
            self.store[lane].addToLine(customer)

        for i, each in enumerate(self.store):
            print(f"Register {i + 1} at {self.time_of_day} seconds has processed {each.customersProcessed} people")
            each.process()
        print("="*50)
            
        # for register in self.store:
        #     self.grid = register.display_line(self.grid)

        self.time_of_day += 1                               # the simTime of the day increments by one
        if self.time_of_hour != SECONDS_IN_HOUR:        # if still in the hour
            self.time_of_hour += 1
        else:                                               # else it is the top of the next hour
            self.hour = self.time_of_day // SECONDS_IN_HOUR  # finds the current hour of the day the simulator is at

            # timeDIf is a tuple, first element is the even ticks between people
            # second element is the remainder simTime
            self.timeDif = self.timeBetweenCustomers(self.hour)

            self.time_of_hour = 0                           # restarts the hourly clock, which is in seconds

    def timeBetweenCustomers(self, hour):
        # number of ticks between integer division of customers to track the simTime between customers arriving
        exactTime = SECONDS_IN_HOUR // self.simCustomers[hour]

        # the remainderTime is the fractional number of seconds between customers
        remainderTime = SECONDS_IN_HOUR % self.simCustomers[hour]

        # divide the remainder simTime by the total customers to find the fraction of seconds that need to be summed
        fractionalTime = remainderTime / self.simCustomers[hour]

        # round to ease computational complexity
        roundedFractionTime = round(fractionalTime, 3)
        return [exactTime, roundedFractionTime]

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

