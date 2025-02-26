import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

mpg = sns.load_dataset('mpg')
#print(mpg.info())
#print(mpg.tail())

mpg.dropna(subset=["horsepower"], inplace=True) # horsepower=None 인 6행 삭제 / p102
#print(mpg.info())

# 방법 1) origin drop
# mpg.drop("origin", axis=1, inplace=True)
# print(mpg.info())

# 방법 1) origin encoded


mpg.drop("name", axis=1, inplace=True) # 연비와 전혀 관련 없는 이름은 drop
print(mpg.info())



