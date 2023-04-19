import matplotlib.pyplot as plt

def display(x, y):
    plt.plot(x, y)
    plt.show()



def run():
    x_values = list()
    x_values.extend((1,2,3,4,5))
    y_values = list()
    y_values.extend((1, 4, 9, 16, 25))
    display(x_values, y_values)
run()
