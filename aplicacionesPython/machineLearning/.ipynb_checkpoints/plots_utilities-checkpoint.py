import matplotlib.pyplot as plt
import numpy as np

def plotWithLinearLine(X, y, model):
    w = model.coef_[0]
    a = -w[0] / w[1]
    xmin, xmax = -1, 1
    ymin, ymax = -1, 1
    xx = np.array([xmin, xmax])
    yy = a * xx - model.intercept_[0] / w[1]
    plt.plot(xx, yy, 'k-', lw=1.5, ls='--')
    X1 = X[:, 0]
    X2 = X[:, 1]
    for i in range(len(y)):
        marker = "+" if y[i] == 1 else "."
        color = "blue" if y[i] == 1 else "red"
        plt.scatter(X1[i], X2[i], label="values", c=color, marker=marker, s=20)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Linear Model example')
    plt.show()