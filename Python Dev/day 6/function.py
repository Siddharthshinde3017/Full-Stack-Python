#required argument

def add(a,b):
    c= a+b
    print(c)

add(5,6)

# keyword argument
def hello (name, age,city):
    print(name,
         age,
          city
        )

hello("sid",20,"satara")

hello(name="prem",age=23,city="pune")

# default argument
def fortune(a,b = 2,c=3):
    print(a)
    print(b)
    print(c)

fortune(40,56)


# variable length argument
def students(name,*marks):
    print("name=",name)
    print("mark = ",marks)

students("abc",56,54,60,58)

def students2(name, **markss):
    print("name = ", name)
    print("marks", markss)

students2("dfs", h=12,s=34,n = 54)



