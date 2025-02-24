import numpy as np


#arange() : 지정된 범위 내에서 일정한 간격으로 숫자가 담긴 배열을 생성하는 함수

# a = np.arange(5)
# print(a, a.ndim, a.shape, a.size)

# a = np.arange(5, 11)
# print(a, a.ndim, a.shape, a.size)

# a = np.arange(2.0, 11.8, 0.2)
# print(a, a.ndim, a.shape, a.size)

a = np.arange(2.0, 11.8, 2.0, dtype=np.int16)
print(a, a.ndim, a.shape, a.size)
