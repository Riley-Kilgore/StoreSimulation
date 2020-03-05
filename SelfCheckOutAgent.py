import queue
from constants import *

class SelfCheckOutAgent(object):
    def __init__(self):
        self.secPerItem = 5
        self.customers = queue.Queue()
        self.currentCustomer = None
        self.eventClock = 0
    
    def process(self):
        if self.customers.empty() and not self.currentCustomer:
            return None
        if self.currentCustomer is None:
            self.eventClock = 0
        self.currentCustomer = self.currentCustomer if self.currentCustomer != None else self.customers.get()
        self.currentCustomer = self.currentCustomer.process_with(self.eventClock, self.secPerItem)
        return self.currentCustomer
    
    def tick(self):
        self.eventClock = self.eventClock + 1

    def addToLine(self, customer):
        self.customers.put(customer)