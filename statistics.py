

class Stats:


    def __init__(self):
        waitTimes = []
        roiTime = 0
        self.generatedCustomers = 0
        self.processedCustomers = 0
        self.totalTime = 0
        self.meanTime = 0
        self.devTime = 0


    def updateCustomersMade(self):
        self.generatedCustomers += 1

    # this method takes a list of registers, and returns the number of customers processed
    def totalCustomersProcessed(self, listRegisters):
        for register in listRegisters:
            self.processedCustomers += register.customersProcessed

        # returns the total customers that paid and left the store
        return self.processedCustomers

    def totalWaitingTime(self, customerTime):
        self.totalTime += customerTime

