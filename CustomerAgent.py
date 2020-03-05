from constants import *
import numpy as np

class CustomerAgent(object):
    def __init__(self):
        self.items_per_step = 1
        self.time_elasped = 0
        self.items_in_cart = np.random.randint(1, 50) # to be changed to normal distribution
    
    # Picks which checkout line to enter
    # Returns the chosen line (checkout object)
    def choose_checkout(self, lines):
        curr_choice = 0
        best_stats = lines[0].get_decision_factors()
        index = 0

        for line in lines:
            stats = line.get_decision_factors()

            # if carts in the new line have visibly fewer items than the current best line
            if stats[0] + (VISIBLE_ITEM_FRAC * stats[1]) <= best_stats[0]:
                curr_choice = index
                best_stats = stats
            
            # if the new line is shorter than the current best line
            elif stats[1] < best_stats[1]:
                curr_choice = index
                best_stats = stats

            # if the new line is a self checkout and the current best is an employee
            elif stats[2] == 'self' and best_stats[2] == 'employee':   
                curr_choice = index
                best_stats = stats
            
            index += 1
        
        return lines[curr_choice]



