"""
The CustomerAgent is used to represent a customer at a market.
The CustomerAgent implements methods to choose a lane to checkout,
  process its cart, and pay for the items in the cart.
"""
import random
from checkoutLogic import move_towards_location, choose_checkout

def visual_attributes():
    return 0.01, 0.9, 0.1


class CustomerAgent(object):
    def __init__(self, x, y):
        self.timeElapsed = 0
        self.cartSize = 0
        self.hasntPaid = True
        self.paymentTime = 0
        self.movingToLine = False
        self.inLine = False
        self.line = None
        self.processing = False
        self.x = x
        self.y = y

        # Initialize the values for the customers cart stochastically.
        pdfNum = random.randint(0, 250)
        self.cartSize = None
        if pdfNum <= 50:
            self.cartSize = random.randint(1, 2)
        elif pdfNum <= 110:
            self.cartSize = random.randint(3, 10)
        elif pdfNum <= 184:
            self.cartSize = random.randint(11, 20)
        else:
            self.cartSize = random.randint(21, 60)
    
    def process_step(self, store):
        """
        Given the store, a customer can process a single unit of time for themselves.
        """
        self.timeElapsed += 1
        event_occured = False
        if not self.movingToLine:
            self.line = store.store[choose_checkout(len(store.store))]
            self.movingToLine = True
            event_occured = True
        if not self.processing and not event_occured:
            location = move_towards_location(self.x, self.y, self.line.x, self.line.y)
            self.x = location[0]
            self.y = location[1]
            self.processing = location[2]
            event_occured = True
        if self.hasntPaid and not event_occured:
            self.process_with(self.timeElapsed, self.line.secPerItem)
            event_occured = True
        


    def process_with(self, timeOffset, secPerItem):
        """
        Processes the items in the cart for the current time step.
        """
        # If the customer is out of items:
        if self.cartSize == 0:
            # We check if they're in payment.
            if self.hasntPaid:
                # If so, we set them to paying, and
                self.hasntPaid = False
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
