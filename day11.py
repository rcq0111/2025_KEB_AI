# Series : 1차원 배열 형태의 자류구조로, 인덱스와 값으로 이루어져 있다

# DataFrame : 2차원 태이블 형태의 자류구조로, 여러개에 시리즈 객체가 모여서 열과 행으로 구성

import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

s2 = pd.Series([99, 100, 98, 91, 92])
s2_subject = s2[1:4]
print(s2_subject)
s2_mean = s2.mean()
print(s2_mean, s2.min())