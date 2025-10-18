class car:
    def start(self):
        print("engine starting")

class Wagnor(car):
    def start(self):
        super().start()
        print("engine started")

w = Wagnor()
w.start()