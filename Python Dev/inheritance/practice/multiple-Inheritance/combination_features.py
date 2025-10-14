class engine :
    def start(self):
        print("engine started ")

class musisystem:
    def play_music(self):
        print("Playing music")

class car(engine,musisystem):
    def drive(self):
        print("Car is moving")

my_car = car()
my_car.start()
my_car.play_music()
my_car.drive()