import math
from AbstractClass import Shape
class Circle(Shape):
    def __init__(self,r=1):
        self.radius=r
    def setRadius(self,r):
        self.radius=r
    def area(self):
        return 2*(math.pi)*math.pow(self.radius,2)
    def perimeter(self):
        return 2*math.pi*self.radius

