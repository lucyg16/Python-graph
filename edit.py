import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

lst = [1, 2, 3, 4, 2, 3]

# fake up some data
# spread = np.random.rand(5) * 100
# print (spread)
# center = np.ones(2) * 50
# print (center)
# flier_high = np.random.rand(1) * 100 + 100
# print (flier_high)
# flier_low = np.random.rand(1) * -100
# print (flier_low)
# data = np.concatenate((spread, center, flier_high, flier_low), 0)
# print (data)

# spread = np.random.rand(50) * 100
# center = np.ones(25) * 40
# flier_high = np.random.rand(10) * 100 + 100
# flier_low = np.random.rand(10) * -100
# d2 = np.concatenate((spread, center, flier_high, flier_low), 0)


spread = [ 70.03673039,  74.27508094,  70.92800107,  56.67455225,  97.77853328]
center = [ 50,  50]
flier_high = [170.6334846]
flier_low = [-24.79157587]
data = np.concatenate((spread, center, flier_high, flier_low), 0)
print (data)

spread = [ 70.03673039,  74.27508094,  70.92800107,  56.67455225,  97.77853328]
center = [ 50,  50]
flier_high = [170.6334846]
flier_low = [-24.79157587]
d2 = np.concatenate((spread, center, flier_high, flier_low), 0)
# for i in range(len(lst)):

d3= [5, 34 ,5 , 23, 5 ,7 ,5 ,32,3 ,34, 34, 3]
print d3


# data.shape = (-1, 1)
# d2.shape = (-1, 1)
data = [data, d2, d3]
ax7 = plt.subplots()
plt.boxplot(data)

plt.show()
