import matplotlib.pyplot as plt
import numpy as np


class Stats:

    def __init__(self):
        waitTimes = []
        roiTime = 0
        self.generatedCustomers = 0
        self.processedCustomers = 0
        self.totalTime = 0
        self.meanTime = 0
        self.devTime = 0
        self.waitTimes = []

    # keeps track of how many customers have been made from hour 0
    def updateCustomersMade(self):
        self.generatedCustomers += 1

    # this method takes a list of registers, and returns the number of customers processed
    def totalCustomersProcessed(self, listRegisters):
        for register in listRegisters:
            self.processedCustomers += register.customersProcessed

        # returns the total customers that paid and left the store
        return self.processedCustomers

    # this keeps track of all waiting times as a sum
    def totalWaitingTime(self, customerTime):
        self.totalTime += customerTime

    # this keeps track of all waiting times, keeping each customer separate
    def addWaitTime(self, customerTime):
        self.waitTimes.append(customerTime)

    # plots the histogram distribution of the customer wait times in seconds, normalized
    def plotWaitTimes(self):
        maxWaitTime = max(self.waitTimes)
        minWaitTime = min(self.waitTimes)

        numCustomers = len(self.waitTimes)

        # uses maximum and minimum values to find bin width
        numBins = (maxWaitTime - minWaitTime) / numCustomers

        # normalizes it, so probability of customer wait times happening is this probability
        plt.hist(self.waitTimes, normed=True, bins=numBins)

        plt.ylabel('Probability')
        plt.xlabel('Wait Time in Seconds')