import numpy as np

a = np.array([1,2,9,3,4,5,6,7,8])
x= np.where((a%2 == 0))   # it returns the index of the even number occured in array
print(x)

print(np.sort(a))