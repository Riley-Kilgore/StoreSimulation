import queue

class EmployeeCheckOutAgent(object):
    def __init__(self):
        self.items_per_step = 5
        self.customers = queue.Queue()
        self.current_customer = None
    
    def process(self):
        self.current_customer = self.current_customer if self.current_customer != None else self.customers.get()
        self.current_customer.process_with(self.items_per_step)