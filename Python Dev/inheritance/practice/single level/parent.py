class parent:
    def work(self):
        print("Parent work hard")

class child(parent):
    def play(self):
        print("Child study to get job")

c= child()
c.play()
c.work()