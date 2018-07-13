from matplotlib import pyplot as pyplot
import numpy as np
from array import array

tree = [1, 3, 4 ,2 ,3 ,4 ,4]
intarray = array(tree)
print intarray

plt.boxplot(intarray)