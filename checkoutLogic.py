import random
import Store
import CustomerAgent

def choose_checkout(numOfLines):
    """
    Returns the index in the line that the customer should go to.
    This is currently stochastic and based upon a uniform distribution.
    """
    return random.randint(0, numOfLines)

def move_towards_location(x1, y1, x2, y2):
    """
    Given the location of a customer and the location of the back
      of the line of a register, get the location for the customemr
      at the next time step.
    """
    delta_x = x2-x1
    delta_y = y2-y1
    delta_l = delta_x**2 + delta_y**2
    delta_l = delta_l if delta_l > 1 else 1
    delta_x = delta_x/delta_l
    delta_y = delta_y/delta_l
    return (x1+delta_x, y1+delta_y, delta_l == 1)