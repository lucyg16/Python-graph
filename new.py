import csv
import numpy as np
from matplotlib import pyplot as plt
from collections import OrderedDict

# ask user for input files of data and index
inputFile = 'data.txt'
inputFileNum = 'data2.txt'
index = 0

# create dictionary to add lists of values to
indexValues = {}

#create lists to add data to
data_input =[] #the matrix
data_input2 = [] #the vector

#read the input file data
with open (inputFile, 'rb') as csvfile:
	inputData = csv.reader(csvfile)
	for row in inputData:
		data_input.append(row)

#read the input file data2
with open (inputFileNum, 'rb') as csvfile:
	inputData2 = csv.reader(csvfile)
	for row in inputData2:
			data_input2.append(row)

#remove whitespaces in data
for item in data_input:
	for i in range(len(item)):
		item[i] = item[i].replace(" ","")

#remove whitespaces in data2
for item in data_input2:
	for i in range(len(item)):
		item[i] = item[i].replace(" ","")

data_input  = np.array(data_input, dtype=np.float_)
data_input2 = np.array(data_input2, dtype=np.float_).flatten()

#iterate through list of given data to add to dictionary indexValues
for i in range(len(data_input)):
    if data_input[i][index] in indexValues:
        # append the corresponding value over in the other matrix
        indexValues[data_input[i][index]].append(data_input2[i])
    else:
        #add the value to the list with identifier j[d] in the dictionary
        indexValues[data_input[i][index]] = [data_input2[i]]

# create ordered dictionary to sort indexValues with
sorted_indexValues = OrderedDict()

#sort indexValues
for key in sorted(indexValues.iterkeys()):
    sorted_indexValues[key]= indexValues[key]

#create empty array to store arrays of data to plot
all_data = []

#convert all values in the dictionary from string to int
for key in sorted_indexValues:

    #flat list from list of lists
    flat_list = []
    for item in sorted_indexValues[key]:
       flat_list.append(item)

    all_data.append(flat_list)

#create list for keys
x_values_keys = []
for key in sorted_indexValues:
    x_values_keys.append(int(key))

print (sorted_indexValues)
print (all_data)

# plt.boxplot(all_data)
plt.boxplot(all_data, positions=x_values_keys)

# boxplot title
plt.title('Box plot')

#show graph

plt.show()
