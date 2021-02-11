from math import pi

class Circle:
    def __init__(self,radius):
        self.radius = radius     
        self._area = None
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,value):
        self._area = None
        self._radius = value
        
    @property
    def area(self):
        if self._area is None:
            print('Calculating Area...')
            self._area = pi * (self._radius**2)
        return self._area

c = Circle(1)

print(c.area) # will calculate the area as area is None.
              # If we change the radius , then only the area will be calcuated again 
              # else it will return the area from the cache.

