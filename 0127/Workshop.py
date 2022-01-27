#도형 만들기
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y



class Rectangle():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_area(self):
        rlt = (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)
        return rlt
    
    def get_perimeter(self):
        rlt = (self.p2.x - self.p1.x) + (self.p1.y - self.p2.y)
        return 2*rlt

    def is_square(self):
        if (self.p2.x - self.p1.x) == (self.p1.y - self.p2.y):
            return True
        else:
            return False

p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3,7)
p4 = Point(6,4)
r2 = Rectangle(p3,p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

'''
3,7
6,4
   #(3,7)

     #(6,4)



      
'''


# class Rectangle(Point):
#     def __init__(self,x,y):
#         super().__init__(x, y)
#         self.x = Point.x
#         self.y = Point.y
    
#     def get_area(self):
#         rlt = self.p1.y * self.p2.x
#         return rlt
    
#     def get_parameter(self):
#         return (self.x + self.y) * 2

#     def is_square(self):
#         if self.x == self.y:
#             return True
#         else:
            # return False

