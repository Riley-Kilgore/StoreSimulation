"""
The EmployeeCheckOutAgent is used to represent a self checkout line in a market.
The EmployeeCheckOutAgent implements methods to process customers, add them to
  the back of the line, and increment its own internal event clock.
"""
# TODO REMOVE ALL MAGIC NUMBERS, REPLACE WITH CONST NAMES
import queue
from constants import *
import numpy as np


class EmployeeCheckOutAgent(object):


    def __init__(self, x, y, itemsPerMin):
        val = itemsPerMin + np.random.normal(0,3)
        self.itemsPerMin = val if val > 0 else itemsPerMin
        self.secPerItem = int(60/itemsPerMin)
        self.customers = queue.Queue()
        self.currentCustomer = None
        self.eventClock = 0
        self.total_items = 0
        self.x = x
        self.y = y
        self.customersProcessed = 0
        self.totalWaitingTime = 0


    @staticmethod
    def visual_attributes():
        return (0.9, 0.01, 0.01), (4, 2)


    def process(self):
        """
        Processes one step of simTime.
        Pre-Condition: self is set up and is valid.
        Post-Condition: self.currentCustomer is updated and simTime ticks.
        Return: The current customer. None if customer has just paid or if queue is empty.
        """
        #print("Length:", self.customers.qsize())
        
        if self.customers.empty() and not self.currentCustomer:
            return None

        # if there is no customer being processed or the current one is done paying, get a new customer
        if self.currentCustomer is None or self.currentCustomer.finished:
            self.eventClock = 0
            if not self.customers.empty():
                self.currentCustomer = self.customers.get()
                self.totalWaitingTime += self.currentCustomer.timeElapsed
                self.customersProcessed += 1
            else:
                self.currentCustomer = None
                return None

        currItems = self.currentCustomer.cartSize
        self.currentCustomer.process_with(self.eventClock, self.secPerItem)
        self.total_items -= currItems - self.currentCustomer.cartSize

        self.tick()
        for customer in list(self.customers.queue):
            customer.tick()
        return self.currentCustomer

    def tick(self):
        """
        Increment internal clock by 1.
        """
        self.eventClock += 1

    def addToLine(self, customer):
        """
        Add the given customer to the internal queue.
        """
        self.customers.put(customer)
        self.total_items += customer.cartSize

    def get_decision_factors(self):
        # In order of priority:
        # line length, total items across the lime, and type of checkout station
        return self.total_items, self.customers.qsize(), 'employee'

    def display_line(self, grid):
        for y in range(self.customers.qsize()):
            curr = self.customers.get()
            # grid[2 * y][self.x + EMPLOYEE_WIDTH + 1] = curr.visual_attributes()
            self.customers.put(curr)
        return grid