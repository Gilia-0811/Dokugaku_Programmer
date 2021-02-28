# http://tinyurl.com/hz9qdh3

class Shape() :
    def what_am_i(self) :
        print("I am a shape.")

class Rectangle(Shape) :
    def __init__(self, width, length) :
        self.width = width
        self.length = length

    def calculate_perimeter(self) :
        return self.width * 2 + self.length * 2

class Square(Shape) :
    def __init__(self, length) :
        self.length = length

    def calculate_perimeter(self) :
        return self.length * 4

    def change_size(self, change_size) :
        self.length += change_size

a_rectangle = Rectangle(10, 5)
a_square = Square(10)

a_square.change_size(-5)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())

a_rectangle.what_am_i()
a_square.what_am_i()
