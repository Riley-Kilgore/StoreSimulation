import random
import Store
import CustomerAgent
from constants import *


def choose_checkout(lines):
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

    return curr_choice


def move_towards_location(x1, y1, x2, y2):
    """
    Given the location of a customer and the location of the back
      of the line of a register, get the location for the customemr
      at the next simTime step.
    """
    delta_x = x2 - x1
    delta_y = y2 - y1
    delta_l = delta_x ** 2 + delta_y ** 2
    delta_l = delta_l if delta_l > 1 else 1
    delta_x = delta_x / delta_l
    delta_y = delta_y / delta_l
    return x1 + delta_x, y1 + delta_y, delta_l == 1
