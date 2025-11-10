class person:
    def speak(self):
        print("person speaking")

class men(person):
    def work(self):
        print('men working')

m= men()
m.work()
m.speak()