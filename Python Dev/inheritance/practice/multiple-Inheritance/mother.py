class mother:
    def quality(self):
        print("caring")
class father:
    def skill(self):
        print("hard work")

class son(mother,father):
    def talent(self):
        print("smart and kind")

s = son()
s.skill()
s.talent()
s.quality()