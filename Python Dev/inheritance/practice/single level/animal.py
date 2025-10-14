class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("dog barks")

d = Dog()
d.bark()
