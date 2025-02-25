#from sklearn.linear_model import LinearRegression
# from chlearn import LinearRegression # 커스텀 모델 생성
from chlearn import KNeighborsRegressor
import pandas as pd
import matplotlib.pyplot as plt

# 데이터를 다운로드하고 준비합니다.
ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv/")
print(ls)
X = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values
#print(y)

# 데이터를 그래프로 나타냅니다.
ls.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction") # grid=True는 격자
plt.axis([23500, 62500, 4, 9]) # asis는 x, y축에대한 사이즈 설정
#plt.show()

# 선형 모델을 선택합니다.
#model = LinearRegression()
model = KNeighborsRegressor(n_neighbors=3)

# 모델을 훈련합니다.
model.fit(X, y)


X_new = [[31721.3]]
print(model.predict(X_new))
# LinearRegression : 5.89940454 -> 실제 값과 더 가까움
# KNeighborsRegressor : 5.7