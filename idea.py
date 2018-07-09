import csv
import numpy as np
from matplotlib import pyplot as plt

# ask user for input files of data and index
inputFile = 'data.txt'#raw_input("Enter the name of your input file: ")
inputFileNum = 'data2.txt'#raw_input("Enter the name of the file with corresponding values: ")
index = 0#input("Enter the index you would like to graph: ")

# create dictionary to add lists of values to
indexValues = {}

#create list for dictionary values
lst = []

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
for i in data_input:
    if i[index] in indexValues:
        # append the corresponding value over in the other matrix
        indexValues[i[index]] = lst.append(data_input2[index])
    else:
        #add the value to the list with identifier j[d] in the dictionary
        indexValues[i[index]] = [data_input2[index]]

# now you should have the dictionary of identifiers with lists of values
print (indexValues)

# now make a box plot using the code provieded on matplotlib, replacing the input with the dictionary that you have created
fig, axes = plt.subplots()

# generate some random test data
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]

# plot box plot
axes.boxplot(all_data)
axes.set_title('Box plot')

# adding horizontal grid lines
axes.yaxis.grid(True)
axes.set_xticks([y + 1 for y in range(len(all_data))])
axes.set_xlabel('Values with index '+ str(index))
axes.set_ylabel('Values corresponding to index '+ str(index))

# add x-tick labels
plt.setp(axes, xticks=[y + 1 for y in range(len(all_data))],
         xticklabels=['x1', 'x2', 'x3', 'x4'])
plt.show()





