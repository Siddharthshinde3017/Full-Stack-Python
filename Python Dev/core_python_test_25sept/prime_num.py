num = int(input("enter the number: "))
if num>1:
    for i in range(2,num):
        if num%i==0 :
            print("numer is not primme")
            break
    else:
        print("number is prime")
else:
    print(num, "is not a prime number")