import numpy as np

x = np.array([1,2,3,4,5])

print(x)
print(type(x))


y = np.array((1,2,3,4,5))
print(y)
print(type(y))

# creating 2d arrays 

z = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(z)


# how to check Dimension of array 
print("Dimension : ",x.ndim)
print("Dimension : ",z.ndim)