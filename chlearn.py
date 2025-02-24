import numpy as np

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
        pass

    def fit(self ,X, y):
        """
        learning function
        :param X: independent variable (2d array format)
        :param y: dependent variable (2d array format)
        :return: void
        """

    def predict(self, X) -> np.ndarray:
        """
        predict value for input
        :param X: new independent variable
        :return: predict value for input (2d array format)
        """