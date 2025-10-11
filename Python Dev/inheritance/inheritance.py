# single inheritance
class parent:
    def display(self):
        print("Parent class")

class child(parent):
    def show(self):
        print("Child class")
    name = "xyz"
c= child()
c.display()
c.show()
