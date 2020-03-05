import random

class CustomerAgent(object):
    def __init__(self):
        self.secPerItem = 5
        self.timeElapsed= 0
        self.cartSize = 0

        pdfNum = random.randint(0,250)
        if(pdfNum <= 50) cartSize = random.randint(1,2)
        elif(pdfNum <= 110) cartSize = random.randint(3,10)
        elif(pdfNum <= 184) cartSize = random.randint(11,20)
        else cartSize = random.randint(21,60)
    
    def choose_checkout(self, lines):
        return lane = random.randint(0, len(store))
