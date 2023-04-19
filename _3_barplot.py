import matplotlib.pyplot as plt

#plt.bar() generates a bar graph for x
# and its corresponding numeric data for y

#bar plots are best used when showing comparsion between categories

x = ["London", "Paris", "Rome", "New Delhi", "BErlin", "Ankara"] # cities
y = [100, 20, 10, 260, 80, 10] # number of Indian restaurants

plt.title("Number of INdian restaurants for Each City - Bar Plot")
plt.xlabel("Cities")
plt.ylabel("Number of Indian restaurans")
plt.barh(x, sorted(y, reverse=True))
# plt.barh(x, y) barh este horizantal
#plt.bar orinzontal
plt.show()