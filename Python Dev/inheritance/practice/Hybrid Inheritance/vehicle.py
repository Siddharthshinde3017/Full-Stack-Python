class vehical:
    def category(self):
        print("I am vehical")

class electric(vehical):
    def fuel(self):
        print("Get charge Electrically")

class bike(vehical):
    def wheels(self):
        print("2 Wheels")

class electricbike(bike, electric):
    def feature(self):
        print("Eco- Friendly")

e = electricbike()
e.category()
e.fuel()
e.wheels()
e.feature()