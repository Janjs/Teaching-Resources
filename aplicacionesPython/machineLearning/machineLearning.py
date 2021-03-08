import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [i for i in range(10)]
    y = [2 * i for i in range(10)]

    while True:
        plt.plot(x, y)