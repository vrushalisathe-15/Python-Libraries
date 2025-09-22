import numpy as np
#check datatype of array
arr=np.array([1,2,3])
print(arr.dtype)  #returns int64

#convert float64 dtype into int32 dtype
arr=np.array([2.44,3.2,8.9999],dtype=np.int32)
print(arr.dtype)

#convert int64 dtype into float64 dtype
arr=np.array([1,22,33,23],dtype=np.float64)
print(arr.dtype)

#string datatype
str=np.array(["Hello","Hi","Bye"])
print(str.dtype)

#TYPECASTING
#convert int64 into float64
arr=np.array([1,5,7,8,4,9,3,2])
print(arr.dtype)
new_arr=arr.astype(np.float64)
print(new_arr.dtype)
print(new_arr)

#covert float to int datatype
arr=np.array([6.77,8.9,3.4,4.67,8.65])
print(arr.dtype)
new_arr=arr.astype(np.int64)
print(new_arr.dtype)
print(new_arr)