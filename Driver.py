from Store import Store
import matplotlib.pyplot as plt
import time
from matplotlib.animation import ArtistAnimation

numRegisters = 1

store = Store(numRegisters)
simTime = 86400
# grids_over_time = []

# fig = plt.figure()
# ims = []

start = time.process_time()

for t in range(simTime):
    # ims.append([plt.imshow(store.grid)])
    store.run_step()
# ims.append([plt.imshow(store.grid)])

totalProcessed = 0

# tracks the number actually processed by each register to compare with total analytical number
for register in store.store:
    totalProcessed += register.customersProcessed

totalCustomers = 0
for i in range(24):
    totalCustomers += store.simCustomers[i]


print()
print()
print("Time to run simulation:", time.process_time() - start, "seconds")
print("Total customers:", totalCustomers)
print("Customers Processed: ", totalProcessed)
print("Time per person: ", round(simTime / (totalProcessed / numRegisters), 2), "seconds per customer")

    


# animation = ArtistAnimation(fig, ims, interval=10, blit=True)

plt.show()
