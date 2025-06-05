# NumPy Examples — pages 6 to 18

import numpy as np
import sys
from numpy import pi, newaxis

# ===== 1. Array Basics =====
a = np.arange(15).reshape(3, 5)
print("Array a:\n", a)
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Data type:", a.dtype.name)
print("Item size:", a.itemsize)
print("Total size:", a.size)
print("Type:", type(a))

b = np.array([6, 7, 8])
print("Array b:\n", b)

# ===== 2. Creating arrays =====
a = np.array([2, 3, 4])
print("Array dtype:", a.dtype)

b = np.array([1.2, 3.5, 5.1])
print("Array b dtype:", b.dtype)

# Multidimensional arrays
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print("Multidimensional array b:\n", b)

c = np.array([[1, 2], [3, 4]], dtype=complex)
print("Complex array c:\n", c)

# Placeholder arrays
print("Zeros:\n", np.zeros((3, 4)))
print("Ones:\n", np.ones((2, 3, 4), dtype=np.int16))
print("Empty:\n", np.empty((2, 3)))

# Sequence creation
print("arange:\n", np.arange(10, 30, 5))
print("arange float:\n", np.arange(0, 2, 0.3))
print("linspace:\n", np.linspace(0, 2, 9))

x = np.linspace(0, 2 * pi, 100)
f = np.sin(x)

# ===== 3. Printing arrays =====
print("1D array:\n", np.arange(6))

b = np.arange(12).reshape(4, 3)
print("2D array:\n", b)

c = np.arange(24).reshape(2, 3, 4)
print("3D array:\n", c)

np.set_printoptions(threshold=sys.maxsize)

# ===== 4. Basic operations =====
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print("a - b:", a - b)
print("b squared:", b ** 2)
print("10 * sin(a):", 10 * np.sin(a))
print("a < 35:", a < 35)

# Matrix product
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print("Element-wise A*B:\n", A * B)
print("Matrix product A @ B:\n", A @ B)
print("Matrix product A.dot(B):\n", A.dot(B))

# In-place operations
rg = np.random.default_rng(1)
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
b += a
print("In-place multiplication a:\n", a)
print("In-place addition b:\n", b)

# Universal functions
B = np.arange(3)
print("exp(B):", np.exp(B))
print("sqrt(B):", np.sqrt(B))

C = np.array([2., -1., 4.])
print("add(B, C):", np.add(B, C))

# ===== 5. Indexing and slicing =====
a = np.arange(10) ** 3
print("a[2]:", a[2])
print("a[2:5]:", a[2:5])

a[:6:2] = 1000
print("Modified a:", a)

print("Reversed a:", a[::-1])

for i in a:
    print("Cubic root of", i, ":", i ** (1 / 3.0))

# Multidimensional indexing
def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
print("fromfunction b:\n", b)

print("b[2,3]:", b[2, 3])
print("b[:,1]:", b[:, 1])
print("b[1:3,:]:\n", b[1:3, :])
print("b[-1]:", b[-1])

# ===== 6. Shape manipulation =====
a = np.floor(10 * rg.random((3, 4)))
print("Original a:\n", a)
print("Flattened:", a.ravel())
print("Reshaped (6,2):\n", a.reshape(6, 2))
print("Transposed:\n", a.T)

a.resize((2, 6))
print("Resized a:\n", a)

print("Reshape with -1:\n", a.reshape(3, -1))

# Stacking arrays
a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))
print("vstack:\n", np.vstack((a, b)))
print("hstack:\n", np.hstack((a, b)))

a = np.array([4., 2.])
b = np.array([3., 8.])
print("column_stack:\n", np.column_stack((a, b)))

# Splitting arrays
a = np.floor(10 * rg.random((2, 12)))
print("hsplit in 3:\n", np.hsplit(a, 3))
print("hsplit at (3,4):\n", np.hsplit(a, (3, 4)))

# ===== 7. Copies and views =====
a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
b = a
print("b is a:", b is a)

c = a.view()
print("c is a:", c is a)
print("c.base is a:", c.base is a)

c = c.reshape((2, 6))
print("Reshaped c:\n", c)

c[0, 4] = 1234
print("Modified a after c:\n", a)

s = a[:, 1:3]
s[:] = 10
print("Modified a after slice s:\n", a)

# Deep copy
d = a.copy()
print("d is a:", d is a)

d[0, 0] = 9999
print("a after d modification:\n", a)

# Large array slicing
a = np.arange(int(1e8))
b = a[:100].copy()
del a

print("b after deleting a:\n", b)
