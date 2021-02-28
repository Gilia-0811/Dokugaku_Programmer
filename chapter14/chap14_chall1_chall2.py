# http://tinyurl.com/j9qjnep

class Shape() :
    def what_am_i(self) :
        print("I am a shape.")

class Square(Shape) :
    square_list = []
    
    def __init__(self, length) :
        self.length = length
        self.square_list.append(self)

    def calculate_perimeter(self) :
        return self.length * 4

    def change_size(self, change_size) :
        self.length += change_size

    def __repr__(self) :
        return"{} by {} by {} by {}".format(self.length, self.length, self.length, self.length)

a_square = Square(29)
print(a_square)

