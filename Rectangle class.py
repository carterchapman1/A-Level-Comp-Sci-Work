import math

class Rectangle:
    def __init__(self, len, height):
        self.len = len
        self.height = height
    
    def rectarea(self):
        print(self.len * self.height)

    def rectperimeter(self):
        print(2*(self.len + self.height))

    def rectdiagonal(self):
        diag = math.sqrt(self.len^2+self.height^2)
        print(diag)

r1 = Rectangle(2,3)
r1.rectdiagonal()
r1.rectperimeter()
r1.rectarea()