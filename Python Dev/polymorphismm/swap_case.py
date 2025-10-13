class logic:
    def swap(self,num1,num2):
        temp = num1
        num1 = num2
        num2 = temp
        print(f"after swaping {num1,num2}")
class op(logic):
    def swap(self,num1,num2):
        super().swap(num1,num2)
        print(num1,num2)

o=op()
o.swap(10 , 20)