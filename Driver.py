from Store import Store, SelfCheckOutAgent, EmployeeCheckOutAgent
import matplotlib.pyplot as plt
import time
import datetime
from matplotlib.animation import ArtistAnimation
import csv


def get_store_metrics(numRegisters, secPerItemE, secPerItemS,
                      chanceSelfCheckout, customerSpawnRate):
    store = Store(numRegisters, secPerItemE, secPerItemS, chanceSelfCheckout, customerSpawnRate)
    simTime = 86400
    # grids_over_time = []

    # fig = plt.figure()
    # ims = []

    start = time.process_time()

    print("Starting simulation suite")

    for t in range(simTime):
        # ims.append([plt.imshow(store.grid)])
        store.run_step()
    # ims.append([plt.imshow(store.grid)])

    totalProcessed = 0

    # tracks the number actually processed by each register to compare with total analytical number
    for register in store.store:
        totalProcessed += register.customersProcessed

    totalCustomers = store.totalCustomers
    # for i in range(24):
    # totalCustomers += store.simCustomers[i]

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

    # animation = ArtistAnimation(fig, ims, interval=10, blit=True)

    # plt.show()


if __name__ == "__main__":
    numRegisters = 15
    secPerItemE = 25
    secPerItemS = 15
    chanceSelfCheckout = .5
    customerSpawnRate = 1
    # get_store_metrics(numRegisters, secPerItemE, secPerItemS, chanceSelfCheckout, customerSpawnRate)

    # logging how long the simulation suite takes
    startTime = datetime.datetime.now().replace(microsecond=0)

    testingSuite = 0
    print("Finished round ", testingSuite, "of 5")
    register_list = [get_store_metrics(reg_val, secPerItemE, secPerItemS, chanceSelfCheckout, customerSpawnRate)
                     for reg_val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]]
    testingSuite += 1
    print("Finished round ", testingSuite, "of 5")

    employee_speed_list = [
        get_store_metrics(numRegisters, item_speed, secPerItemS, chanceSelfCheckout, customerSpawnRate)
        for item_speed in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                           29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]
    testingSuite += 1
    print("Finished round ", testingSuite, "of 5")

    self_speed_list = [get_store_metrics(numRegisters, secPerItemE, item_speed, chanceSelfCheckout, customerSpawnRate)
                       for item_speed in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]]
    testingSuite += 1
    print("Finished round ", testingSuite, "of 5")

    # chance_self_list = [get_store_metrics(numRegisters, secPerItemE, secPerItemS, indiv_chance, customerSpawnRate)
    #                     for indiv_chance in [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]]
    # testingSuite += 1
    # print("Finished round ", testingSuite, "of 5")

    spawn_rate_list = [get_store_metrics(numRegisters, secPerItemE, secPerItemS, chanceSelfCheckout, indiv_chance)
                       for indiv_chance in [.1, .2, .3, .4, .5]]
    testingSuite += 1
    print("Finished round ", testingSuite, "of 5")

    with open("register_data_expanded.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30], register_list))
    with open("employee_speed_data_expanded.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                              29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], employee_speed_list))
    with open("self_speed_data_expanded.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
                             self_speed_list))
    # with open("self_checkout_chance_data_expanded.csv", "w") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(zip([.1, .2, .3, .4, .5], chance_self_list))
    with open("customer_spawn_rate_data_expanded", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip([.1, .2, .3, .4, .5, .6, .7, .8, .9, 1], spawn_rate_list))

    endTime = datetime.datetime.now().replace(microsecond=0)
    print("The simulation suite took ", endTime - startTime, "to run")
