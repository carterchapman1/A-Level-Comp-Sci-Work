import math
class Scalar:
    def __init__(self,x):
        self.x = x
    
    def __str__(self):
        return print(scalar)
    
class Vector:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return print(vector)

    def __mul__(self, scalar):
        y = self.y * scalar
        x = self.x * scalar
        return (x,y)

    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self) -> float:
        return math.sqrt((self.x*self.x)+(self.y*self.y))
    
    def __eq__(self, other):
        equal : bool = self.x == other.x and self.y == other.y
        return equal
    
    def angle(self) -> float:
        return (180 / math.pi)*(math.atan(self.y/self.x))
    def __str__(self):
        return(f'X is {self.x} and Y is {self.y}!')
    def test():
        vector1 = Vector(3,4)
        vector2 = Vector(6,7)
        print(vector1)
        print(vector2)
        print(vector1.magnitude())
        print(vector2.magnitude())
        sumvector = vector1 + vector2
        

Vector.test()

