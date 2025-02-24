#from statistics import LinearRegression
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

# 데이터를 다운로드하고 준비합니다.
ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv/")
#print(type(ls))
#print(ls)
X = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values
#print(y)

# 데이터를 그래프로 나타냅니다.
ls.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction") # grid=True는 격자
plt.axis([23500, 62500, 4, 9]) # asis는 x, y축에대한 사이즈 설정
#plt.show()

# 선형 모델을 선택합니다.
#model = LinearRegression()
model = KNeighborsRegressor(n_neighbors=3) # n_neighbors : hyperparameter 학습하는 동안 적용할 규제의 양

# 모델을 훈련합니다.
model.fit(X, y)

# 키프로스에 대해 예측을 만듭니다.
X_new = [[37655.2]] # 2020년 키프로스 1인당 GDP
print(model.predict(X_new)) # 출력 : [[6.30165767]]
# LinearRegression : 6.30165767
# KNeighborsRegressor : 6.33333333 / k-초근접 이웃 k-nn (k-nearest neighbors)

X_new2 = [[31721.3]]
print(model.predict(X_new2))
# LinearRegression : 5.89940454 -> 실제 값과 더 가까움
# KNeighborsRegressor : 5.7