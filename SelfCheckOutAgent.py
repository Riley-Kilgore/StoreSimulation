"""
The SelfCheckOutAgent is used to represent a self checkout line in a market.
The SelfCheckOutAgent implements methods to process customers, add them to
  the back of the line, and increment its own internal event clock.
"""
# TODO REMOVE ALL MAGIC NUMBERS, REPLACE WITH CONST NAMES
import queue
from constants import *


class SelfCheckOutAgent(object):


    def __init__(self, x):
        self.secPerItem = 5
        self.customers = []
        self.currentCustomer = None
        self.eventClock = 0
        self.total_items = 0
        self.x = x
        self.customersProcessed = 0


    @staticmethod
    def visual_attributes():
        return (0.01, 0.1, 0.9), (2, 2)


    def process(self):
        """
        Processes one step of simTime.
        Pre-Condition: self is set up and is valid.
        Post-Condition: self.currentCustomer is updated and simTime ticks.
        Return: The current customer. None if customer has just paid or if queue is empty.
        """
        if len(self.customers) == 0 and not self.currentCustomer:
            return None
        if self.currentCustomer is None:
            self.eventClock = 0

        if self.currentCustomer is None:
            self.eventClock = 0
            self.currentCustomer = self.customers[0]
            del self.customers[0]
            self.customersProcessed += 1

        self.currentCustomer = self.currentCustomer.process_with(self.eventClock, self.secPerItem)
        self.tick()
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
        self.customers.append(customer)

    def get_decision_factors(self):
        # In order of priority: 
        # line length, total items across the lime, and type of checkout station
        return self.total_items, len(self.customers), 'self'

    def display_line(self, grid):
        for y in range(len(self.customers)):
            curr = self.customers[y]
            grid[2 * y][self.x + SELF_WIDTH + 1] = curr.visual_attributes()[0]
        return grid
