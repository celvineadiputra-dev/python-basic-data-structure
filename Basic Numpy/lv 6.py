import numpy as np

x = np.array([[1, 4], [2, 3]])
y = np.array([[2, 1], [4, 2]])

print(x)
print(y)

xy = x + y
print(xy)

xy = x.dot(y)
print(xy)

print(xy.max())
print(xy.min())