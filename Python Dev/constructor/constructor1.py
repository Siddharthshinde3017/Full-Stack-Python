# default constructor
class python:
    def __init__(self):
        print("new function")
p=python()

# parameterise constructor
class python1:
    def __init__(self,name,id):
        self.name = name
        self.id = id
p= python1("asdf",23)
print(p.id)
print(p.name)
