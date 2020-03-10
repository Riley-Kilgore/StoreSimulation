from Store import Store
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

store = Store(1)
time = 100
grids_over_time = []

for t in range(time):
    grids_over_time.append(store.grid)
    store.run_step()

totalProcessed = 0

# tracks the number actually processed by each register to compare with total analytical number
for register in store.store:
    totalProcessed += register.customersProcessed

totalCustomers = 0
for i in range(24):
    totalCustomers += store.simCustomers[i]

print("Total customers:", totalCustomers)
print("Customers Processed: ", totalProcessed)


# fig = plt.figure()
# im = plt.imshow(grids_over_time[2])
#
#
# def updateSimulation(data):
#     store.run_step()
#     im.set_array(data)
#     return [im]
#
#
# # animation = FuncAnimation(fig, updateSimulation, frames=grids_over_time, blit=True)
#
# plt.show()
