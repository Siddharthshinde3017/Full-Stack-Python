class grandfather:
    def land(self):
        print("Own Land")
class father(grandfather):
    def car(self):
        print("Owns car")
class son(father):
    def bike(self):
        print("Owns Bike")
s = son()
s.bike()
s.car()
s.land()