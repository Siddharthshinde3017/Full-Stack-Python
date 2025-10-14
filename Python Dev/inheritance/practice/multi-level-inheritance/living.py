class living:
    def breath(self):
        print("Breath for leaving")
class Animal(living):
    def eat(self):
        print("Eat food living")
class Pets(Animal):
    def sleep(self):
        print("pets are speeping")

p = Pets()
p.sleep()
p.eat()
p.breath()