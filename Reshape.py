import numpy as np
#RESHAPE
# changing the shape of an array
arr=np.array([1,2,3,4,5,6])
reshaped=arr.reshape(2,3)
print(reshaped)

#RAVEL --returns view
#convert multi-dimensional array into 1D array
arr=np.array([[4,5,6],
              [9,8,7]])
print(arr.ravel())
arr[0]=1
print(arr.ravel())

#FLATTEN --returns copy
#returns the copy of the array
arr=np.array([[4,5,6],
              [9,8,7]])
print(arr.ravel())

