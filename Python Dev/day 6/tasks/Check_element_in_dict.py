name = input("Enter enement to search")

mydict ={1: 'a', 2: 'b', 3: 'c'}

if name in mydict.values():
    print("exists")

else:
    print("not exist")