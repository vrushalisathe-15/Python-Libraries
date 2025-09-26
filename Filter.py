import numpy as np
arr1=np.array([0,79,9,3,4,5,0])
fa=arr1>3
print(fa)

fa =arr1>35
new=arr1[fa]
print(new)

arr=np.array([2,4,3,5,6])
filter=arr%2==0
new=arr[filter]
print(new)