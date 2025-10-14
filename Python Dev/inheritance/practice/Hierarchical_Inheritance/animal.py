class Animal:
    def sound(self):
        print("Animal maakes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class cat(Animal):
    def sound(self):
        print("Cat Meows")

class cow (Animal):
    def sound(self):
        print("COw moos")

for a in [Dog(),cat(),cow()]:
    a.sound()