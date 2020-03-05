import queue

class EmployeeCheckOutAgent(object):
    def __init__(self):
        self.items_per_step = 5
        self.customers = queue.Queue()
        self.current_customer = None
        self.total_items = 0
    
    def process(self):
        self.current_customer = self.current_customer if self.current_customer != None else self.customers.get()
        self.current_customer.process_with(self.items_per_step)

    # returns the sats of this checkout instance for a customer to see
    def get_decision_factors(self):
        
        # In order of priority: 
        # line length, total items accross the lime, and type of checkout station
        return (self.total_items, self.customers.qsize(), 'employee')

    def enqueue_customer(self, customer):
        self.customers.put(customer)
        self.total_items += customer.items_in_cart
    
    def dequeue_customer(self):
        self.customers.get()