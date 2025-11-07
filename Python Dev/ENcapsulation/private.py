class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

p1 = person("sid",25)
print(p1.name)
# print(p1.__age)
# in this above code we get error for the p1.age besause age is the orivate property we dont get the rigt of sowint that we can acces it by "get" method calling from the another method.




