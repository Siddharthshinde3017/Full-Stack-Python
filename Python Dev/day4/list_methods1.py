from operator import index

from cytoolz import remove

list1 = ["apple", "banana", "cherry"]
# append() - adds element at the end of list
list1.append("mango")
print(list1)

# clear - delets all elements in the list but list exist with null
# list1.clear()
print(list1)

# copy()
list2 = list1.copy()
print(list2)

# count()
print(list1.count("banana"))

# extend()
list3 = ["guvaua", "stroberry"]
list1.extend(list3)
print(list1)

# index()
print(list1.index("cherry"))

# insert()
list1.insert(1,"Dragon Fruit")
print(list1)

# pop()
list1.pop(1)
print(list1)

# remove()

list1.remove("cherry")
print(list1)

# reverse()
list1.reverse()
print(list1)

# sort()
list1.sort()
print(list1)
list1.sort(reverse= True)
print(list1)