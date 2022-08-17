import numpy as np

x = np.array([[1, 4], [2, 3]])
y = np.array([[2, 1], [4, 2]])

print(x)
print(y)

print(x[0, 1])
print(x[1, 1])
print(x[0:2, 1])
print(x[0:2, 0])
print(x[1, 0:2])

x = np.array([[1, 2, 3], [5, 2, 1]])
print(x.reshape(3, 2))
print(x.dtype)

x = np.array([["Blue", "Dark Blue"], ["Soft Blue", "Light Blue"]])
print(x)
print(x.dtype)

x = np.array([1, 2, 3], dtype=complex)
print(x)