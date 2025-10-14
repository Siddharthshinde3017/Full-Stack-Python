class father:
    def __init__(self):
        print("Father Initilized")

class Mother:
    def __init__(self):
        print("Mother Initilized")

class Child(father,Mother):
    def __init__(self):
        super().__init__()
        print("cild initilized")

c = Child()