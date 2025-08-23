import numpy

arr = numpy.array([1,2,3,4,5])

print(arr)

# ndarray is a class in numpy module
# It is used to create arrays in numpy
# ndarray.shape is used to get the shape of the array
arr1 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.shape)
print(arr1.size) # product of elements of shape
print(arr1.dtype)
print(type(arr))
print(type(arr1))