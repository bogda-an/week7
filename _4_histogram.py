import matplotlib.pyplot as plt
import numpy as np

#plt.hist() generates a histogram graph
# a histogram displays numerical data by grouping data into
# "bins" of equal width

#generate random values

x = np.random.normal(170, 255 , 250)
print(x)
plt.xlabel("Numeric Data")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.hist(x)
plt.show()