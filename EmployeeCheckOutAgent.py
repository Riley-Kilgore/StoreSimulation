import queue

class EmployeeCheckOutAgent(object):
    def __init__(self):
        self.secPerItem= 2
        self.customers = queue.Queue()
        self.current_customer = None
        eventClock = 0
    
    def process(self):
        self.current_customer = self.current_customer if self.current_customer != None else self.customers.get()
        self.current_customer.process_with(self.secPerItem)

    def tick(self):
        self.eventClock = self.eventClock + 1

    def addToLine(self, customer):
        self.customers.put(customer)
        
