class bird:
    def fly(self):
        print("Bird can fly")

class sparrow(bird):
    def sing(self):
        print("Sparrow sings")

s= sparrow()
s.fly()
s.sing()