class tree:
    def fruit(self):
        print("im fruit method")

class branch(tree):
    def fruit(self):
        super().fruit()
        print("im fruit 2 method")

c = branch()
c.fruit()