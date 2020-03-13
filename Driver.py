# The Driver Module
# The Driver Module is a single function module that is used
#   to tie together the model for our simulation.
# In order to use the program, the user must tweak the settings
#   below. All program functionality is handled through the settings
#   here.

from Store import Store, SelfCheckOutAgent, EmployeeCheckOutAgent
import matplotlib.pyplot as plt
import time
import datetime
from matplotlib.animation import ArtistAnimation
import csv
import itertools

# ****************** Settings *********************************
NUM_REGISTERS = 15
ITEM_M_E = 25
ITEM_M_S = 15
CHANCE_SELF_CHECK = .5
SPAWN_CHANCE = 1

REG_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
ITEM_E_LIST = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
               19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
               32, 33, 34, 35, 36, 37, 38, 39, 40]
ITEM_S_LIST = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
SELF_CHECK_SPAWN = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
CUSTOMER_SPAWN = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]



def get_store_metrics(numRegisters, itemPerMinE, itemPerMinS,
                      chanceSelfCheckout, customerSpawnRate):
    """
    get_store_metrics takes in 5 parameters and returns metrics
    on how the business has done given the parameters.
    :param: numRegisters: The number of registers in the store.
    :param: itemPerMinE: The average number of items processed by
      employees.
    :param: itemPerMinS: The average number of items processed by
      customers in self-checkout.
    :param: checkSelfCheckout: The chance that given a new CheckOut location,
      the CheckOut location is a self-checkout kiosk.
    :param: customerSpawnRate: The chance on a customer-spawn-tick that the
      customer actually spawns, alternatively no customer will be generated on that
      tick.
    :return: Average Wait, Total Customers, Total Customers Processed,
      Num of Employee Registers, Num of Self-Checkout Kiosks.
    """
    # Get all store
    store = Store(numRegisters, itemPerMinE, itemPerMinS, chanceSelfCheckout, customerSpawnRate)
    simTime = 86400
    
    start = time.process_time()

    print("Starting simulation suite")

    for t in range(simTime):
        store.run_step()

    totalProcessed = 0

    # tracks the number actually processed by each register to compare with total analytical number
    for register in store.store:
        totalProcessed += register.customersProcessed

    totalCustomers = store.totalCustomers

    totalWaitTime = 0
    self_kiosks = 0
    emp_regs = 0
    self_type = type(SelfCheckOutAgent(0, 0, 15))
    emp_type = type(EmployeeCheckOutAgent(0, 0, 25))
    for each in store.store:
        totalWaitTime += each.totalWaitingTime
        val = 1 if type(each) == self_type else 0
        self_kiosks += val
        val = 1 if type(each) == emp_type else 0
        emp_regs += val

    # print(f"Avg Waiting Time: {totalWaitTime / (60 * store.temp_total)}")
    # print(f"Total waiting time: {totalWaitTime / 60} minutes.")
    # print("Time to run simulation:", time.process_time() - start, "seconds")
    # print("Total customers:", totalCustomers)
    # print(f"Actual Total Customers: {store.temp_total}")
    # print("Customers Processed: ", totalProcessed)
    # print("Time per person: ", round(simTime / (totalProcessed / numRegisters), 2), "seconds per customer")
    return totalWaitTime / (60 * store.temp_total), store.temp_total, totalProcessed, emp_regs, self_kiosks


if __name__ == "__main__":
    # DEFAULT VALUES
    numRegisters = NUM_REGISTERS
    itemPerMinE = ITEM_M_E
    itemPerMinS = ITEM_M_S
    chanceSelfCheckout = CHANCE_SELF_CHECK
    customerSpawnRate = SPAWN_CHANCE
    # get_store_metrics(numRegisters, itemPerMinE, itemPerMinS, chanceSelfCheckout, customerSpawnRate)

    # logging how long the simulation suite takes
    startTime = datetime.datetime.now().replace(microsecond=0)

    testingSuite = 0
    print("Finished round ", testingSuite, "of 5")
    register_list = [get_store_metrics(reg_val, itemPerMinE, itemPerMinS, chanceSelfCheckout, customerSpawnRate)
                     for reg_val in REG_LIST]
    testingSuite += 1
    print("Finished round ", testingSuite, "of 5")

    employee_speed_list = [
        get_store_metrics(numRegisters, item_speed, itemPerMinS, chanceSelfCheckout, customerSpawnRate)
        for item_speed in ITEM_E_LIST]
    testingSuite += 1
    print("Finished round ", testingSuite, "of 5")

    employee_speed_self_chance_list = [
        get_store_metrics(numRegisters, item_speed, itemPerMinS, chance, customerSpawnRate)\
            for item_speed in ITEM_E_LIST for chance in SELF_CHECK_SPAWN
    ]

    self_speed_list = [get_store_metrics(numRegisters, itemPerMinE, item_speed, chanceSelfCheckout, customerSpawnRate)
                       for item_speed in ITEM_S_LIST]
    testingSuite += 1
    print("Finished round ", testingSuite, "of 5")

    chance_self_list = [get_store_metrics(numRegisters, itemPerMinE, itemPerMinS, indiv_chance, customerSpawnRate)
                         for indiv_chance in SELF_CHECK_SPAWN]
    testingSuite += 1
    print("Finished round ", testingSuite, "of 5")

    spawn_rate_list = [get_store_metrics(numRegisters, itemPerMinE, itemPerMinS, chanceSelfCheckout, indiv_chance)
                       for indiv_chance in CUSTOMER_SPAWN]
    testingSuite += 1
    print("Finished round ", testingSuite, "of 5")

    # This block runs too many simulations at once.
    # with open("employee_sp_chance_self.csv", "w") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(zip(list(itertools.product([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
    #                           29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],[.1, .2, .3, .4, .5, .6, .7, .8, .9, 1])), employee_speed_self_chance_list))

    with open("register_data_expanded.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip(REG_LIST, register_list))
    with open("employee_speed_data_expanded.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip(ITEM_E_LIST, employee_speed_list))
    with open("self_speed_data_expanded.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip(ITEM_S_LIST,
                             self_speed_list))
    with open("self_checkout_chance_data_expanded.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip(SELF_CHECK_SPAWN, chance_self_list))
    with open("customer_spawn_rate_data_expanded", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip(CUSTOMER_SPAWN, spawn_rate_list))

    endTime = datetime.datetime.now().replace(microsecond=0)
    print("The simulation suite took ", endTime - startTime, "to run")
