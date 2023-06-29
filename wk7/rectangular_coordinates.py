import math

class RectangularCoordinates:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def get_coordinate(self):
        return (self.x, self.y)
    
    def is_on_axis(self) -> bool:
        # if self.x == 0 or self.y == 0:
        #     return True
        # else:
        #     return False
        return self.x == 0 or self.y == 0
    
    def check_quadrant(self):
        if self.is_on_axis():
            return None
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        else:
             return 4
         
    def distance_x(self):
        return abs(self.y)
    
    def distance_y(self):
        return abs(self.x)
    
    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
        
    def midpoint(self, a, b):
        return (self.x + abs(a - self.x) / 2, b - abs(b - self.y) / 2)
    
    