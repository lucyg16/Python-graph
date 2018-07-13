
# this piece of code sorts the dictionary keys from least to greatest

myDict = {'11': [['5'], ['8'], ['5'], ['4']], '10': [['1'], ['2'], ['6'], ['4']], '13': [['7'], ['3']], '12': [['2'], ['3']], '15': [['4'], ['9'], ['8'], ['4'], ['2']], '14': [['2'], ['4']]}

sorted_myDict = {}

for key in sorted(myDict.iterkeys()):
	print "%s: %s" % (key, myDict[key])
	# sorted_myDict.append("%s: %s" % (key, myDict[key]))


print (myDict)
