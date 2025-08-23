# core ideas in numpy : vectorization and broadcasting
# Vectorization = doing math on whole arrays in one shot
# Broadcasting = making arrays of different shapes work together

import numpy as np

# vectorized operations
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])

print(a + b)
print(a * b)

# Broadcasting
x = np.array([1,2,3])
y = 5 #scaler gets "broadcased"
print(x + y) #[6,7,8]

M = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
V = np.array([10,20,30])
print(M + V) #row-wise broadcast

# Vectorization = speed, Broadcasting = flexibility