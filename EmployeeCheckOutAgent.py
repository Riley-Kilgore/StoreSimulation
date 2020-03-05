"""
The EmployeeCheckOutAgent is used to represent a self checkout line in a market.
The EmployeeCheckOutAgent implements methods to process customers, add them to
  the back of the line, and increment its own internal event clock.
"""
#TODO REMOVE ALL MAGIC NUMBERS, REPLACE WITH CONST NAMES
import queue

class EmployeeCheckOutAgent(object):
    def __init__(self):
        self.secPerItem= 2
        self.customers = queue.Queue()
        self.currentCustomer = None
        self.eventClock = 0
    
    def process(self):
        """
        Processes one step of time.
        Pre-Condition: self is set up and is valid.
        Post-Condition: self.currentCustomer is updated and time ticks.
        Return: The current customer. None if customer has just paid or if queue is empty.
        """
        if self.customers.empty() and not self.currentCustomer:
            return None
        if self.currentCustomer is None:
            self.eventClock = 0
        self.currentCustomer = self.currentCustomer if self.currentCustomer != None else self.customers.get()
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
        self.customers.put(customer)
        
