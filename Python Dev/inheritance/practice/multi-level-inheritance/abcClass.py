class A:
    def a(self):
        print("clas A")
class B(A):
    def b(self):
        print("class B")
class C(B):
    def c(self):
        print("class C")

c= C()
c.c()
c.a()
c.b()