"""
The Store is used to represent a the physical store in the model.
The Store orchestrates the operations of the other classes.
"""
from CustomerAgent import CustomerAgent
from EmployeeCheckOutAgent import EmployeeCheckOutAgent
from SelfCheckOutAgent import SelfCheckOutAgent
from random import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from constants import *
import numpy as np

class Store(object):
    # Constructor
    def __init__(self, n):
        self.global_time = 0
        self.store = []
        self.fig = plt.figure()

        for i in range(n):
            checkout = EmployeeCheckOutAgent(i * (EMPLOYEE_WIDTH + SPACE_BETWEEN)) if random() < .5 else SelfCheckOutAgent(i * (SELF_WIDTH + SPACE_BETWEEN))
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
        Postcondition: A single tick has occurred in the simulated environment.
        Return: self
        """
        if self.global_time % 10 == 0:
            customer = CustomerAgent()
            lane = customer.choose_checkout(self.store) #chosen lane (checkout object)
            self.store[lane].addToLine(customer)
        for i, each in enumerate(self.store):
            print(f"Processing line {i} of {len(self.store)}")
            each.process()
        
        for register in self.store:
            self.grid = register.display_line(self.grid)
        
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
