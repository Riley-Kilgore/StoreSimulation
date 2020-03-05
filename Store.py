"""
The Store is used to represent a the physical store in the model.
The Store orchestrates the operations of the other classes.
"""
from CustomerAgent import CustomerAgent
from EmployeeCheckOutAgent import EmployeeCheckOutAgent
from SelfCheckOutAgent import SelfCheckOutAgent
from random import random

class Store(object):
    # Constructor
    def __init__(self, n):
        self.global_time = 0
        self.store = []
        # Creates either an employee checkout line or self checkout line n times and
        #   keeps the values in a list.
        for i in range(n):
            checkout = EmployeeCheckOutAgent() if random() < .5 else SelfCheckOutAgent()
            self.store.append(checkout)

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
            lane = customer.choose_checkout(len(self.store))
            self.store[lane].addToLine(customer)
        for i, each in enumerate(self.store):
            print(f"Processing line {i} of {len(self.store)}")
            each.process()
        return self