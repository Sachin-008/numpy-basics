import numpy as np

# Basic array creation
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:")
print(arr)

# Shape, size, itemsize, nbytes
print("\nArray properties:")
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Itemsize:", arr.itemsize)
print("Nbytes:", arr.nbytes)

# 1D, 2D, 3D arrays
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("\n1D array:", a)
print("2D array:\n", b)
print("3D array:\n", c)

# Special arrays
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
full = np.full((2, 2), 7)
identity = np.eye(3)
range_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

print("\nZeros:\n", zeros)
print("Ones:\n", ones)
print("Full:\n", full)
print("Identity:\n", identity)
print("Range:", range_arr)
print("Linspace:", linspace_arr)

# Reshaping
num_arr = np.arange(1, 13)
reshaped = num_arr.reshape(3, 4)
print("\nReshaped array:\n", reshaped)
print("Flattened:", reshaped.ravel())
print("Transpose:\n", reshaped.T)

# Indexing and slicing
print("\nSlicing examples:")
print("arr[0] =", arr[0])
print("arr[-1] =", arr[-1])
print("arr[1:3, 0:2]:\n", arr[1:3, 0:2])
print("arr[:, 1] =", arr[:, 1])

# Boolean indexing
values = np.array([10, 20, 30, 40, 50])
mask = values > 25
print("\nBoolean mask:", mask)
print("Filtered values:", values[mask])

# Fancy indexing
print("Fancy indexing:", values[[0, 2, 4]])

# Arithmetic operations
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("\nAddition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Power:", x ** 2)
print("Square root:", np.sqrt(x))

# Aggregation
print("\nAggregation:")
print("Sum:", np.sum(values))
print("Mean:", np.mean(values))
print("Median:", np.median(values))
print("Min:", np.min(values))
print("Max:", np.max(values))
print("Std:", np.std(values))
print("Var:", np.var(values))

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
print("A + B:\n", A + B)
print("A * B:\n", A * B)
print("A @ B:\n", A @ B)
print("np.dot(A, B):\n", np.dot(A, B))
print("A transpose:\n", A.T)
print("Determinant:", np.linalg.det(A))
print("Inverse:\n", np.linalg.inv(A))

# Broadcasting
M = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([10, 20, 30])
print("\nBroadcasting result:\n", M + v)

# Sorting and searching
sort_arr = np.array([5, 2, 9, 1, 7])
print("\nSorted:", np.sort(sort_arr))
print("Argsort:", np.argsort(sort_arr))
print("Where > 5:", np.where(sort_arr > 5))

# Copy vs view
a_copy = np.array([1, 2, 3, 4])
a_view = a_copy.view()
a_copy2 = a_copy.copy()

a_view[0] = 100
print("\nAfter view change:", a_copy)
a_copy2[0] = 200
print("After copy change:", a_copy)

# Concatenation and splitting
p = np.array([1, 2, 3])
q = np.array([4, 5, 6])
print("\nConcatenate:", np.concatenate([p, q]))

x1 = np.array([[1, 2], [3, 4]])
x2 = np.array([[5, 6]])
print("Vertical concat:\n", np.concatenate([x1, x2], axis=0))
print("Horizontal concat:\n", np.concatenate([x1, x2.T], axis=1))

spl = np.arange(9)
print("Split:", np.split(spl, 3))

# Stacking
print("\nVStack:\n", np.vstack([p, q]))
print("HStack:", np.hstack([p, q]))
print("Column stack:\n", np.column_stack([p, q]))

# Random numbers
print("\nRandom ints:", np.random.randint(0, 10, size=5))
print("Random floats:\n", np.random.rand(3, 2))
print("Normal distribution:\n", np.random.randn(3, 2))
print("Random choice:", np.random.choice([10, 20, 30], size=5))

# Statistical functions
matrix = np.array([[1, 2], [3, 4]])
print("\nMatrix sum by axis 0:", np.sum(matrix, axis=0))
print("Matrix sum by axis 1:", np.sum(matrix, axis=1))
print("Matrix mean:", np.mean(matrix))

# Linear algebra
A2 = np.array([[1, 2], [3, 4]])
b2 = np.array([5, 6])
print("\nSolve A2 x = b2:", np.linalg.solve(A2, b2))
print("Norm:", np.linalg.norm(A2))

# Unique values
unique_arr = np.array([1, 2, 2, 3, 3, 4])
print("\nUnique:", np.unique(unique_arr))
print("Unique with counts:", np.unique(unique_arr, return_counts=True))

# File I/O
np.save("my_array.npy", matrix)
loaded = np.load("my_array.npy")
print("\nLoaded array from .npy file:\n", loaded)

np.savetxt("data.txt", matrix, delimiter=",")
saved_data = np.loadtxt("data.txt", delimiter=",")
print("Loaded text data:\n", saved_data)

# NumPy constants
print("\nPI:", np.pi)
print("E:", np.e)
print("Inf:", np.inf)
print("NaN:", np.nan)

# Example: normalization
scores = np.array([10, 20, 30, 40])
normalized = (scores - scores.mean()) / scores.std()
print("\nNormalized scores:", normalized)

# Example: nearest value
numbers = np.array([10, 20, 30, 40, 50])
target = 33
idx = np.abs(numbers - target).argmin()
print("Nearest value to 33:", numbers[idx])

# Example: image-like array
img = np.array([
    [0, 255, 0],
    [255, 0, 255],
    [0, 255, 0]
], dtype=np.uint8)
print("\nImage array:\n", img)
