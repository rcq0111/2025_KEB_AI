import numpy as np

# zero(), ones() : 주어진 모양(shape)에 대해 모든 요소가 0 또는 1인 배열을 생성하는 함수
ones = np.ones((3,4))
print(ones)
#zeros = np.zeros((3,4))
zeros = np.zeros((3,4), dtype=np.int16)
print(zeros)
zeros2 = np.zeros((2,3,4))
print(zeros2, zeros2.dtype)
