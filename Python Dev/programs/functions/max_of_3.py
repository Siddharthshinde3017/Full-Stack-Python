def maximum(a,b,c):
    if a>b and a>c:
        print(a,"a is the maximum number between all")
    elif b>a and b>c:
        print(b," b is greater number between all")
    elif a==b and b==c:
        print("numbers are equal")
    else :
        print(c,"c is greater of all")

a = int(input("Enter the num a : "))
b = int(input("Enter the num b : "))
c = int(input("Enter the num c : "))
maximum(a,b,c)