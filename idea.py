import csv
import numpy as np
from matplotlib import pyplot as plt

# ask user for input files of data and index
inputFile = 'data.txt'#raw_input("Enter the name of your input file: ")
inputFileNum = 'data2.txt'#raw_input("Enter the name of the file with corresponding values: ")
index = 0#input("Enter the index you would like to graph: ")

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

#iterate through list of given data to add to dictionary indexValues
for i in range(len(data_input)):
    if data_input[i][index] in indexValues:
        # append the corresponding value over in the other matrix
        indexValues[data_input[i][index]].append(data_input2[i])
    else:
        #add the value to the list with identifier j[d] in the dictionary
        indexValues[data_input[i][index]] = [data_input2[i]]

###### now you should have the dictionary of identifiers with lists of values
print (indexValues)

#create empty array to store arrays of data to plot
all_data = []

#convert all values in the dictionary from string to int
for key in indexValues:

    #flat list from list of lists
    flat_list = []
    for sublist in indexValues[key]:
       for item in sublist:
           flat_list.append(item)

    testArrays = [int(i) for i in flat_list]
    all_data.append(testArrays)

plt.boxplot(all_data)

plt.title('Box plot for Wissam by me')

plt.grid(True)
plt.xlabel('Values with index '+ str(index))
plt.ylabel('Values corresponding to index '+ str(index))

plt.show()


