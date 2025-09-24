# return statment
def hello(a):
    # print(a)
    return a
print(hello(10))
# addition of two numbers using the return keyword
def add(a,b):
    return a+b
print(add(3,4))

# lambda expression
total = lambda m1,m2 : m1+m2
# total(10,12)
print(total(10,30))


mult1 = lambda n1,n2 :n1*n2
total = mult1(2,5)
print(total)

#
# even_num = lambda num : num%2==0
#     if True:
#         print("even")
# even_num1=even_num(2)
# print(even_num1)

# to filter even elements from lists using fiter method

l1= [1,2,3,54,6,]
even_num1 = list(filter(lambda n: n%2==0,l1))
print(even_num1)

sq = list(filter(lambda n:n*n,l1))
print(sq)


