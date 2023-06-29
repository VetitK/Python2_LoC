import math 

class Triangle:
    def __init__(self, a, b, c, base=None, height=None) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.base = base
        self.height = height

    def perimeter(self):
        # perimeter = self.a + self.b + self.c
        # return perimeter
        return self.a + self.b + self.c
    
    def area(self): # 1/2 * b * h
        if self.base is None or self.height is None:
            return None
        return 0.5 * self.base * self.height
    
    def area_advance(self): # sqrt(s(s-a)(s-b)(s-c)) s=(a+b+c)/2
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
    
    def is_right_triangle(self) -> bool:
        length_list = [self.a, self.b, self.c]
        length_list.sort()
        longest_side = length_list[-1]
        shortest_side = length_list[0]
        middle_side = length_list[1]
        
        # if shortest_side ** 2 + middle_side ** 2 == longest_side ** 2:
        #     return True
        # else:
        #     return False
        return shortest_side ** 2 + middle_side ** 2 == longest_side ** 2

triangle_A = Triangle(3, 4, 5)
print(triangle_A.is_right_triangle())

