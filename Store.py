from CustomerAgent import CustomerAgent
from EmployeeCheckOutAgent import EmployeeCheckOutAgent
from SelfCheckOutAgent import SelfCheckOutAgent
from random import random

class Store(object):
    def __init__(self, n):
        self.global_time = 0
        self.store = []
        for i in range(n):
            checkout = EmployeeCheckOutAgent() if random() < .5 else SelfCheckOutAgent()
            self.store.append(checkout)

    def run_step(self):
        if self.global_time % 2 == 0:
            customer = CustomerAgent()
            store = customer.choose_checkout(self.store)
            store.add_customer(customer)
        for i, each in enumerate(self.store):
            each.process()
