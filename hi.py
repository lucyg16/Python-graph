# import csv
# import numpy as np
# from matplotlib import pyplot as plt

# cars = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 2]
# planes = [5, 34 ,5 , 23, 5 ,7 ,5 ,32,3 ,34, 34, 3]

# ####################################################################
# # generate some random test data
# all_data = cars

# all_data, planes = plt.subplots()
# # plot box plot
# # plt.boxplot(all_data, planes)
# plt.boxplot()



# #####################################################################
# plt.title("Box plot for Wissam")

# # adding horizontal grid lines

# plt.xlabel('Values with index ')
# plt.ylabel('Values corresponding to index ')

# plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

# fake up some data
spread = np.random.rand(5) * 100
print (spread)
center = np.ones(2) * 50
print (center)
flier_high = np.random.rand(1) * 100 + 100
print (flier_high)
flier_low = np.random.rand(1) * -100
print (flier_low)
data = np.concatenate((spread, center, flier_high, flier_low), 0)
print (data)
spread = np.random.rand(50) * 100
center = np.ones(25) * 40
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
d2 = np.concatenate((spread, center, flier_high, flier_low), 0)
data.shape = (-1, 1)
d2.shape = (-1, 1)
data = [data, d2, d2[::2,0]]
fig7, ax7 = plt.subplots()
ax7.set_title('Multiple Samples with Different sizes')
ax7.boxplot(data)

plt.show()
