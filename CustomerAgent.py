import random

class CustomerAgent(object):
    def __init__(self):
        self.timeElapsed= 0
        self.cartSize = 0
        self.hasntPaid = True

        pdfNum = random.randint(0,250)
        if(pdfNum <= 50) cartSize = random.randint(1,2)
        elif(pdfNum <= 110) cartSize = random.randint(3,10)
        elif(pdfNum <= 184) cartSize = random.randint(11,20)
        else cartSize = random.randint(21,60)
    
    def choose_checkout(self, lines):
        return lane = random.randint(0, len(lines))

    def process_with(self, secPerItem, timeOffset):
        if self.cartSize == 0:
            if self.hasntPaid == True:
                self.hasntPaid == False
                self.paymentTime = timeOffset
            return self.pay_for_cart(self.paymentTime, timeOffset)
        if timeOffset % secPerItem == 0:
            self.cartSize -= 1
        
    def pay_for_cart(self, startTime, timeOffset):
        if timeOffset - startTime >= 85:
            return None
        return self
        
        