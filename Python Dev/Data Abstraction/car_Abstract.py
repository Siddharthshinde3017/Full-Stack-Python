from abc import ABC, abstractmethod


class car(ABC):
    def comfert(self,name):
        print("comfertable",name )
    @abstractmethod
    def

class suzuki(car):
    def safty(self,name):
        print("* * ",name)
    def service(self,name):
        print("Best service")


class Tata(car):
    def safty(self,name):
        print("* * * * *",name)
    def service(self,name):
        print("poor service")

t = Tata()
t.safty("nexon")
t.service("nexon")
t.comfert("nexon")

s = suzuki()
s.safty("Wagnor")
s.service("Wagnor")
s.comfert("wagnor")