import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, metrics
from sklearn.svm import LinearSVC


def readData():
    df = pd.read_csv("week2dataset.csv", comment="#")
    X1 = df.iloc[: ,0]
    X2 = df.iloc[: ,1]
    X = np.column_stack((X1, X2))
    y = df.iloc[: ,2]
    return [X, y];

def plotData(X, y):
    X1 = X[:, 0]
    X2 = X[:, 1]
    for i in range(len(y)):
        marker = "+" if y[i] == 1 else "."
        color = "blue" if y[i] == 1 else "red"
        plt.scatter(X1[i], X2[i], label="values", c=color, marker=marker, s=20)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Training Data')
    plt.show()

def logRegTraining(X, y):
    model = linear_model.LogisticRegression()
    model.fit(X, y)
    #b = model.intercept_[0]
    #w1, w2 = model.coef_.T
    #print("(ii)", "Intercept: ", b, " Coefficients: ", w1, w2)
    return model

def logRegPredicting(model, X_test, y_test):
    y_pred = pd.Series(model.predict(X_test))
    y_test = y_test.reset_index(drop=True)
    compare = pd.concat([y_test, y_pred], axis=1)
    compare.columns = ['True', 'Prediction']
    print("(iii)", compare.head())
    print("Accuracy ", metrics.accuracy_score(y_test, y_pred))
    print("Precision ", metrics.precision_score(y_test, y_pred))
    print("Recall ", metrics.recall_score(y_test, y_pred))
    return y_pred

def plotDataWithPredictions(model, X, y, y_pred):
    X1 = X[:, 0]
    X2 = X[:, 1]
    for i in range(len(y)):
        if y[i] == 1 and y_pred[i] == 1:
            marker = "+"
            color = "blue"
        elif y[i] == -1 and y_pred[i] == -1:
            marker = "."
            color = "red"
        elif y[i] == -1 and y_pred[i] == 1:
            marker = "+"
            color = "violet"
        elif y[i] == 1 and y_pred[i] == -1:
            marker = "."
            color = "lightsalmon"
        plt.scatter(X1[i], X2[i], label="values", c=color, marker=marker, s=20)

    # Get model parameters
    b = model.intercept_[0]
    w1, w2 = model.coef_.T
    # Calculate the intercept and slope of the decision boundary
    c = -b / w2
    m = -w1 / w2
    # Plot the data and the classification with the decision boundary
    xmin, xmax = -1, 1
    ymin, ymax = -1, 1
    xd = np.array([xmin, xmax])
    yd = m * xd + c
    plt.plot(xd, yd, 'k', lw=1, ls='--')
    plt.fill_between(xd, yd, ymin, color='tab:red', alpha=0.2)
    plt.fill_between(xd, yd, ymax, color='tab:blue', alpha=0.2)
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Comparison predictions / target values with decision boundary')
    plt.show()

def SVMClassifier(X, y):
    # C=0.001
    modelSVM1 = LinearSVC()
    modelSVM1.C = 0.001
    modelSVM1.fit(X, y)
    score = modelSVM1.score(X, y)
    c, m = calculateParametersModel(modelSVM1)
    print("Score for C=0.001: ", score, " Intercept: ", c, " Slope: ", m)
    plotSVMClassifiers(X, y, modelSVM1, 0.001)
    # C=1
    modelSVM2 = LinearSVC()
    modelSVM2.C = 1
    modelSVM2.fit(X, y)
    score = modelSVM2.score(X, y)
    c, m = calculateParametersModel(modelSVM2)
    print("Score for C=1: ", score, " Intercept: ", c, " Slope: ", m)
    plotSVMClassifiers(X, y, modelSVM2, 1)
    # C=1000
    modelSVM3 = LinearSVC()
    modelSVM3.C = 1000
    modelSVM3.fit(X, y)
    score = modelSVM3.score(X, y)
    c, m = calculateParametersModel(modelSVM3)
    print("Score for C=1000: ", score, " Intercept: ", c, " Slope: ", m)
    plotSVMClassifiers(X, y, modelSVM3, 1000)

def calculateParametersModel(model):
    b = model.intercept_[0]
    w1, w2 = model.coef_.T
    # Calculate the intercept and slope of the decision boundary
    c = -b / w2
    m = -w1 / w2
    return c, m

def plotSVMClassifiers(X, y, model, C):
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
    title = 'LinearSVM with C=' + str(C)
    plt.title(title)
    plt.show()

def addSquares(X):
    X1 = X[:, 0]
    X2 = X[:, 1]
    X1squared = []
    for x in X1:
        X1squared.append(x**2)
    X1squared = np.array(X1squared)
    X2squared = []
    for x in X2:
        X2squared.append(x ** 2)
    X2squared = np.array(X2squared)
    X = np.column_stack((X1, X2, X1squared, X2squared))
    return X

def plotPredictionsWithTrueTargets(y, y_pred):
    for i in range(len(y)):
        color = "blue" if y[i] == 1 else "red"
        plt.scatter(y[i], y_pred[i], label="values", c=color, s=20)
    plt.xlabel('True Targets')
    plt.ylabel('Predictions')
    plt.title('Comparation true targets vs predictions')
    plt.show()

def compareWithMostCommonTarget(y, y_pred):
    # calculate the most common target
    numPos = 0
    numNeg = 0
    for i in y:
        if i == 1:
            numPos += 1
        else:
            numNeg += 1

    accuracy = (0+673) / (673+326)
    print("Accuracy ", accuracy)
    precision = 673 / (673+326)
    print("Precision ", precision)
    recall = 673 / (673 + 0)
    print("Recall ", recall)

def plotPredictions(model, X, y, y_pred):
    X1 = X[:, 1]
    for i in range(len(y)):
        color = "blue" if y[i] == 1 else "red"
        plt.scatter(X1[i], y[i], label="values", c=color, marker='+', s=10)
        color = "violet" if y[i] == 1 else "lightsalmon"
        plt.scatter(X1[i], y_pred[i], label="values", c=color, marker='o', s=10)
    plt.xlabel('X1')
    plt.ylabel('y / y predictions')
    plt.title('Comparison of true target vs predicted target')
    plt.show()


if __name__ == "__main__":
    ## comment / uncomment the lines to run each question's result or question step

    #(a)
    X, y = readData()
    #   (i)
    #plotData(X, y)
    #   (ii)
    model = logRegTraining(X, y)
    #   (iii)
    y_pred = logRegPredicting(model, X, y)
    plotDataWithPredictions(model, X, y, y_pred)

    #(b)
    #SVMClassifier(X, y)

    #(c)
    #X = addSquares(X)
    #lrcModel = logRegTraining(X, y)
    #y_pred = logRegPredicting(lrcModel, X, y)
    #plotPredictions(lrcModel, X, y, y_pred)
    #compareWithMostCommonTarget(y, y_pred)
