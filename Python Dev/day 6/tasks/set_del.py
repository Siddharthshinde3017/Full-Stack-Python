set1 = {1,2,3,4,8,6,5,4,}
print(set1)
ser = int(input("Enter element to del"))

if ser in set1:
    print("exist")
    set1.remove(ser)
    print(ser,"item removed")
    print(set1)
else:
    print("element not present")
