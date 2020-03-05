"""
The CustomerAgent is used to represent a customer at a market.
The CustomerAgent implements methods to choose a lane to checkout,
  process its cart, and pay for the items in the cart.
"""
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
    
    def choose_checkout(self, numOfLines):
        """
        Returns the index in the line that the customer should go to.
        This is currently stochastic and based upon a uniform distribution.
        """
        return random.randint(0, numOfLines)

    def process_with(self, secPerItem, timeOffset):
        """
        Processes the items in the cart for the current time step.
        """
        # If the customer is out of items:
        if self.cartSize == 0:
            # We check if they're in payment.
            if self.hasntPaid == True:
                # If so, we set them to paying, and
                self.hasntPaid == False
                # we set the payment start time to the current offset.
                self.paymentTime = timeOffset
            # Now they are in payment mode no matter what, so we call payment.
            return self.pay_for_cart(self.paymentTime, timeOffset)
        # If it's time to move an item from the cart:
        if timeOffset % secPerItem == 0:
            # Do it. Don't let your dreams be dreams.
            self.cartSize -= 1
        
    def pay_for_cart(self, startTime, timeOffset):
        """
        Wait to pay and return None when it's time to leave.
        """
        # Are we done paying? 85 seconds, phew...
        if timeOffset - startTime >= 85:
            # WOOOO, we are released.
            return None
        # Gotta stay in the front of the line, paying, forever...
        return self
        
        