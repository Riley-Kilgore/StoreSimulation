class CustomerAgent(object):
    def __init__(self):
        self.items_per_step = 1
        self.time_elasped = 0
    
    def choose_checkout(self, lines):