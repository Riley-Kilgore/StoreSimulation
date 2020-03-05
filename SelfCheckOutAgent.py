import queue
from constants import *

class SelfCheckOutAgent(object):
    def __init__(self):
        self.secPerItem = 5
        self.customers = queue.Queue()
        self.currentCustomer = None
    
    def process(self):
        if self.customers.empty() and not self.currentCustomer:
            return None
        self.currentCustomer = self.currentCustomer if self.currentCustomer != None else self.customers.get()
        self.currentCustomer = self.currentCustomer.process_with(self.secPerItem)
        return self.currentCustomer