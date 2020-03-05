import queue

class EmployeeCheckOutAgent(object):
    def __init__(self):
        self.items_per_step = 5
        self.customers = queue.Queue()
        self.current_customer = None
        self.
    
    def process(self):
        if self.customers.empty() and not self.current_customer:
            break
        self.current_customer = self.current_customer if self.current_customer != None else self.customers.get()
        self.current_customer.process_with(self.items_per_step)