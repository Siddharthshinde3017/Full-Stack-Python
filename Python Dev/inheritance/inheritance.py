# single inheritance
class parent:
    def display(self):
        print("Parent class")

class child(parent):
    def show(self):
        print("Child class")
        # super().display()       #used to accecss properties from parent without calling the method
    name = "xyz"
c= child()
# c.display()
c.show()
