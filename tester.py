import csv
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# ask user for input files of data and index
inputFile = 'data.txt'#raw_input("Enter the name of your input file: ")
inputFileNum = 'data2.txt'#raw_input("Enter the name of the file with corresponding values: ")
index = 0#input("Enter the index you would like to graph: ")

# create dictionary to add lists of values to
indexValues = {}

#create lists to add data to
data_input =[]
data_input2 = []

#read the input file data
with open (inputFile, 'rb') as csvfile:
	inputData = csv.reader(csvfile)#, delimiter=',\n')
	for row in inputData:
		data_input.append(row)

#read the input file data2
with open (inputFileNum, 'rb') as csvfile:
	inputData2 = csv.reader(csvfile)#, delimiter='\n')
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

# print (data_input)
# print (data_input2)

#iterate through list of given data
for i in range(len(data_input)):
	indexValues[data_input[i][index]] = data_input2[i]

# now you should have the dictionary of identifiers with lists of values
print(indexValues)

# Fixing random state for reproducibility

matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
ax.plot(indexValues, indexValues[0])
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()
