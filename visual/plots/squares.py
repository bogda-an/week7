import matplotlib.pyplot as plt

#marker/line/color

def display1 (x, y):
    plt.plot(x, y, "p-b")
    # plt.show()

def display2 (x, y):
    plt.plot(x, y, "s--g")
    plt.show()

def run():
    x_values = list()
    x_values.extend((3, 3, 4, 4, 3))
    y_values = list()
    y_values.extend((3, 4, 4, 3, 3))
    display1(x_values, y_values)

    x_values = list()
    x_values.extend((2,2,5,5,2))
    y_values = list()
    y_values.extend((2,5,5,2,2))
    display2(x_values, y_values)


run()