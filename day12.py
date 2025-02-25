# Assignment
# v1.3) v1.2 파일의 결측치 값을 산술평균으로 채워 넣는 다양한 방법을 적용하시오.

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame(
    {
        'A' : [1, 2, np.nan, 4],
        'B' : [np.nan, 2, 3, 4],
        'C' : [1, 2, 3, 4]
    }
)

i = SimpleImputer(strategy='mean')
df[['A', 'B']] = i.fit_transform(df[['A', 'B']])
print(df)