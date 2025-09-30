from calculator import *
from calculator import add,subs,mult,divi
add(3,5)
subs(45,64)
percent(28,10)

a = int(input("Enter the num1: "))
b = int(input("Enter the num2:" ))

operation = int(input("enter the operetion(plese enter num upto 5): "))
if operation == 1:
    add(a,b)
elif operation==2:
    subs(a,b)