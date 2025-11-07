import numpy as np
#
b= np.array([[[1,2,3],[1,2,3],[1,2,3]]])
# for i in b:
#     print(i)

for i in np.nditer(b): # nditer is mathod to print item one b one iteratively
    print(i)

#
a =np.array([1,2,3,4,5,4,6,4,7,8,4,9])
# c = np.where(a==4)
# print(c)  # it returns the index of the element where 4 is present

c = b.flatten()
print(c)

d = a.reshape(4,3)
print(d)

# e = d.reshape/    ()