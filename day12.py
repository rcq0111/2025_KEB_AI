# Assignment

from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

titanic = sns.load_dataset('titanic')
i = SimpleImputer(strategy='mean')
titanic_num = titanic.select_dtypes(include=[np.number])
T = i.fit_transform(titanic_num)
titanic2 = pd.DataFrame(T, columns=titanic_num.columns, index=titanic_num.index)


X = titanic2[['age']]  # 독립 변수 설정
y = titanic2[['survived']]  # 종속 변수 설정

# 훈련/검증 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 선택
model = KNeighborsRegressor(n_neighbors=5)

# K 최근접 이웃 회귀 모델 훈련
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)  # 검증 셋트를 인수로 예측

# 시각화
plt.figure(figsize=(5, 2))
plt.scatter(X_test, y_test, color='blue', label='Real')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.title('KNeighborsRegressor: Real vs Predicted')
plt.xlabel('Age')
plt.ylabel('Survivied')
plt.show()



