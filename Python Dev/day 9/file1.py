import os
# file = open("new.txt","a")
# print(file.read())

# print(file.readline())
# print(file.readline())

# file.write("neww line is added")
# file = open("new.txt","r")
# print(file.read())
# file.close()

with open("new.txt","r") as f:
    print(f.read())