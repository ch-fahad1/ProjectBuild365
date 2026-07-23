import numpy as np

arr1 = np.array([10,20,30,40])

arr2 = np.array([
    [1,2,3],
    [4,5,6]
])

arr3 = np.zeros((3,3))

arr4 = np.ones((2,4))

arr5 = np.arange(1,11)

arr6 = np.linspace(0,100,5)

print("Array 1")
print(arr1)
print("Shape:", arr1.shape)
print("Dimension:", arr1.ndim)
print("Size:", arr1.size)
print("Data Type:", arr1.dtype)

print("\nArray 2")
print(arr2)
print("Shape:", arr2.shape)
print("Dimension:", arr2.ndim)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)

print("\nZeros Array")
print(arr3)

print("\nOnes Array")
print(arr4)

print("\nArange Array")
print(arr5)

print("\nLinspace Array")
print(arr6)