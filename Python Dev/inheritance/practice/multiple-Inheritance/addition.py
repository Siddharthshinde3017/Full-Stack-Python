class A:
    def a(self,a):
        print(a)

class B:
    def b(self,b):
        print(b)
class C(A,B):
    def d(self,a,b):
        print(a+b)
addi = C()
C.d(32,3)
