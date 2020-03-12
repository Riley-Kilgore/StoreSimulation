import re
import matplotlib.pyplot as plt
import time
import csv
import numpy as np


numre = re.compile(r'(\d+)(\.\d+)*')

def get_table(name):
    table_file = open(name, "r")
    table = []

    for line in table_file:
        row = []
        for pair in numre.findall(line):
            if pair != ('', ''):
                row.append(float(pair[0] + pair[1]))
        if row != []:
            table.append(row)
    return np.array(table)
    


employee_speed = get_table("employee_speed_data.csv")
self_speed = get_table("self_speed_data.csv")
self_checkout = get_table("self_checkout_chance_data.csv")
customer_spawn = get_table("register_data.csv")



def plot(table, xcol, ycol, xlabel, ylabel, title):
    xdata = table[:,xcol]
    ydata = table[:,ycol]

    plt.plot(xdata, ydata)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.title(title)
    plt.savefig(fname="plots/" + title.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "") + ".png")
    plt.cla()


# Table Layout
#
# Column Index | Value
#       0      | independent variable
#       1      | average wait time
#       2      | total customers
#       3      | total processed customers
#       4      | # of employee registers used
#       5      | # of self checkout kiosks used)

plot(employee_speed, 0, 1, \
"Employee Checkout Speed (items/min)", \
"Average Customer Wait Time (sec)", \
"Avg Customer Wait Time vs. Employee Checkout Speed")

plot(employee_speed, 0, 3, \
"Employee Checkout Speed (items/min)", \
"Total Customers Processed", \
"Total Customers Processed vs. Employee Checkout Speed")


