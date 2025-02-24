import numpy as np

v = np.array([1, 3, -9, 2])
print(v, v.ndim ,v.shape, v.dtype, v.strides) # n 차원을 출력 현재 1차원
print()
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(b, b.ndim, b.shape, b.dtype, b.strides)
print()
#c = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4],[9, 10, 11, 12]]])
c = np.array([[[1, 2, 3, 4, 1], [5, 6, 7, 8, 1]], [[1, 2, 3, 4, 1],[9, 10, 11, 12, 1]]])
print(c, c.ndim, c.shape, c.dtype, c.strides) #shape 배열의 차원과 크기를 나타내는 튜플(tuple) 형태의 속성
# dtype : 배열 요소들의 데이터 타입을 나타내는 속성 (요소들은 해당 데이터 타입으로 일괄적으로 처리)
# strides : 면, 행, 열(원소 간의 간격)의 간격 /