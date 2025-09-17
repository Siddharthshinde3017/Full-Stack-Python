
list1 =(1, 2, 3, 4)
list2 =(3, 5, 2, 1)
list3 =(2, 2, 3, 1)

def add(a,b,c):
    return a+b+c

result1=map(add,list1,list2,list3)
print(list(result1))
