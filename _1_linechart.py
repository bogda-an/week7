import matplotlib.pyplot as plt

#plt.plot(x, y) generates a line graph

#population of bears over years
x = [2017,2018,2019,2020,2021,2022]
y = [100,175,350,450,400,350]

plt.xlabel("Years")
plt.ylabel("# of Bears Over Years")
plt.title("Population of Bears Over Years")
plt.plot(x, y)
plt.show()