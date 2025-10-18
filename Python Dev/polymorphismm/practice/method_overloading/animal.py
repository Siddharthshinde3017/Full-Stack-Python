class Animal:
    def sound(self):
        print("make sound")

class dog(Animal):
    def sound(self):
        print("bark")

d=dog()
d.sound()
