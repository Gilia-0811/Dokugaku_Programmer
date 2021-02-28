# http://tinyurl.com/gpqe62e

class Triangle() :
    def __init__(self, base, height) :
        self.base = base
        self.height = height

    def calculate_area(self) :
        return self.height * self.base / 2

a_triangle = Triangle(10, 5)
print(a_triangle.calculate_area())
