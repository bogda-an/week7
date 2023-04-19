import matplotlib.pyplot as plt

#plt.plot(x, y) generates a line graph

#population of bears over years
x = [2017,2019,2022,2026,2030,2040]
y = [100,175,350,450,400,350]

plt.xlabel("Years")
plt.ylabel("# of Bears Over Years")
plt.title("Population of Bears Over Years")


plt.step(x, y)
plt.show()