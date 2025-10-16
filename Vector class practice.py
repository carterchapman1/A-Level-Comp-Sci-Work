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

   """ def __rmul__(self):
        return Vector(self.magnitude, other)"""

    def magnitude(self) -> float:
        return math.sqrt((self.x*self.x)+(self.y*self.y))
    
    def angle(self) -> float:
        return (180 / math.pi)*(math.atan(self.y/self.x))

vector = Vector(3,4)
scalar = Scalar(1)
print(vector.magnitude())
print(vector.angle())


