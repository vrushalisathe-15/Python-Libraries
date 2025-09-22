import numpy as np

arr=np.array([1,2,3,4,5])
print(arr.ndim) #returns the dimension of the array
print(arr.size) #returns the size of the array

a=np.arange(0,10)#returns numbers between 0to9
print(a)

arr=np.linspace(0,5,2)  #returns values between given range
print(arr)
print(arr)

arr =np.zeros(10)
print(arr)
arr=np.zeros([2,3]) #returns 2 row * 3 cols matrix full of zeros
print(arr)

arr2=np.ones([2,3]) #arr full of ones
print(arr2)

arr3=np.full([2,3],4)  # arr full of 4
print(arr3)

val=np.random.random(10) # generates random float values
print(val)

n=np.random.randint(1,10,5) #returns random int values
print(n)
