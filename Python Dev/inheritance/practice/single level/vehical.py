class vehical:
    def start(self):
        print("Vehical Startedd")

class car(vehical):
    def drive(self):
        print("car is driving")


c = car()
c.drive()
c.start()