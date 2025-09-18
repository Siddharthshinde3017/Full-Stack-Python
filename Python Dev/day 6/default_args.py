# greet using default parameter
def greet(name,msg = "hello"):
    print(msg,name)
greet("siddharth")

# 2 calculate area of circle
def area(r,pi=3.14):
    print("area of circle is ", 2*pi*r)
area(4)

# 3 welcome with default name
def welcome(name="friend"):
    print("welcome !",name)
welcome()
welcome("bro")

# 4 sub mark report
def report(subject,mark = 100):
    print(subject, "total marks are", mark)
report("math")
report("eng",85)

# 5 discount
def sp(price,discount = 10):
    print(price-(price*discount/100) )
sp(100)