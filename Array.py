import numpy as np
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(arr)
print(arr.T)       #returns transpose
print(arr.sum(axis=0)) #returns the sum of axis 0
print(arr.sum(axis=1))  #returns the sum of axis 1
print(arr.ndim)  #returns the dimension of an array
print(arr.shape)   #returns shape of an array
print(arr.size)   #returns the size of an array
print(arr.nbytes) #returns total number of bytes are occupied
print(arr.argmax(axis=0))   #returns the index of max arg of axis 0
print(arr.argmin(axis=0))  #returns the index of min  arg of axis 0

arr1=np.array([0,79,9,3,4,5,0])
print(arr1.argmax())   #returns the index of max arg
print(arr1.argmin()) #returns the index of min arg
print(arr1.mean())    #returns mean
print(arr1.argsort()) #returns the sorting index of array
print(np.nonzero(arr1))  #returns the index of nonzero arg