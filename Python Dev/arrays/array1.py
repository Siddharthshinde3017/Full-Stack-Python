from array import *
import array as arr
a = array('i',[1,2,3,4,5,6])
print(a)

print(type(a))

a[2:4]= array('i',[8,9])
print(a)

c = arr.array('d',[1.0,2.0,3.0,4.0,5.0])
d = arr.array('d',[2.1,3.1])
e = arr.array('d')
e = c+d
print(e)