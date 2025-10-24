class Shape:
    def area(self, a=None, b=None):
        if a is not None and b is not None:
            print("Rectangle area:", a * b)
        elif a is not None:
            print("Square area:", a * a)
        else:
            print("No data to calculate area")

s = Shape()
s.area(5)        # Square
s.area(5, 3)     # Rectangle
s.area()         # No data
