class A:
    def f1(self):
        print("From class A")

class B:
    def f2(self):
        print("from class B")

class C (A,B):
    def f3(self):
        print("from class A&B")

c = C()
c.f3()