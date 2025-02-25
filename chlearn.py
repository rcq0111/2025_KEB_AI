import numpy as np
import pandas as pd

class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self ,X, y):
        """
        learning function
        :param X: independent variable (2d array format)
        :param y: dependent variable (2d array format)
        :return: void
        """
        X_mean = np.mean(X)
        y_mean = np.mean(y)

        denominator = np.sum(pow(X-X_mean, 2)) # 분모구하는 공식 / 관측값에서 타겟(mean값)을 뺀값 / 제곱을 한 이유 : 음수 방지
        numerate = np.sum((X-X_mean)*(y-y_mean)) # 분자구하는 공식

        self.slope = numerate / denominator # 기울기
        self.intercept = y_mean - (self.slope * X_mean) # 절편

    def predict(self, X) -> np.ndarray:
        """
        predict value for input
        :param X: new independent variable
        :return: predict value for input (2d array format)
        """
        return self.slope * np.array(X) + self.intercept

class KNeighborsRegressor:
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors

    def fit(self ,x, y):
        """
        learning function
        :param X: independent variable (2d array format)
        :param y: dependent variable (2d array format)
        :return: void
        """
        self.x = x
        self.y = y


    def predict(self, X) -> np.ndarray:
        """
        predict value for input
        :param X: new independent variable
        :return: predict value for input (2d array format)
        """
        # new independent variable과 근접한 값을 n_neighbors만큼 뽑는다
        # 뽑은 X값에 해당하는 y값의 평균 -> k-nn

        predictions = []
        for x_test in X:  # loop just one time in this example
            # d(P, Q) = sqrt((x2 - x1)^2 + (y2 - y1)^2)
            distances = np.sqrt(np.sum((x_test - self.x) ** 2, axis=1))
            # print(distances)
            indices = np.argsort(distances)[:self.n_neighbors]
            # print(indices)
            prediction = np.mean(self.y[indices])
            # prediction = (self.y_train[indices[0]]+self.y_train[indices[1]]+self.y_train[indices[2]]) / self.n_neighbors
            predictions.append(prediction)

            return np.array(prediction).reshape(-1, 1)