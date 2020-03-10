import csv
import random
import math
import numpy as np


def createCustomers():
    customers = []

    # uses the foot traffic file
    with open('Data.csv') as file:
        csv_reader_object = csv.reader(file)

        # in the CSV, this if statement ignores the header
        if csv.Sniffer().has_header:
            next(csv_reader_object)
        for row in csv_reader_object:
            customers.append(int(row[1]))

    # -------------------------create array of Poisson-distributed customer numbers, one per hour---------------------#

    simNumCustomers = []           # this is the number of arrivals in the simulation
    MAX_ARRIVALS = 10000   # upper limit on number of people in an hour
    hour = 0           # keep track of the portions of an hour that have been used
    numCustomers = 0

    # for each hour
    for i in np.arange(1, len(customers)):
        rate = customers[i]     # this many customers observed  walk in to the store this hour

        while hour < 1 and numCustomers < MAX_ARRIVALS:
            rand = random.random()     # probability value to use in inverse CDF

            # use random value to find arrival time between customers using inverse cumulative distribution function
            difTime = -math.log(1.0 - rand)/rate

            # use this to keep track of percent of an hour so as to not exceed the time limit
            hour += difTime
            numCustomers += 1

        simNumCustomers.append(numCustomers)

        numCustomers = 0
        hour = 0

    return simNumCustomers
