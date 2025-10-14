class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))
print(calc.add(1, 2, 3))
print(calc.add(5))