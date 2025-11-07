import numpy as np


# # zero D array
# arr0d = np.array(45)
# print(arr0d)
#
# # 1 dimentional array
#
# arr = np.array([1,2,3,4,5,6])
# print(arr)


# c = np.arange(1,51)
#
# d = c.reshape(2,25)
# print(d)

arr2d = np.array([[[1,2,3],[4,5,6]],

                  [[7,8,9],[10,11,12]]])
# print(arr2d)

for i in arr2d:
    for j in i:
        print(j,end=" ")
        # print()
    print()

print(arr2d.ndim)
print('\n',arr2d)