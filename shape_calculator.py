class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'{__class__.__name__}(width={self.width}, height={self.height})'

    def set_width(self, num):
        self.width = num

    def set_height(self, num):
        self.height = num

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ''
            for i in range(self.height):
                picture += '*' * self.width + '\n'
            return picture

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        self.set_side(self.side)

    def __str__(self):
        return f'{__class__.__name__}(side={self.side})'

    def set_side(self, num):
        self.side = num
        self.width = num
        self.height = num

    def set_width(self, num):
        self.set_side(num)

    def set_height(self, num):
        self.set_side(num)

