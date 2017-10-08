from base import Figure

class Circle(Figure):

    def __init__(self, center_x, center_y, color, radius, **kwargs):
        super().__init__(center_x, center_y, color, **kwargs)
        self.radius = radius

    def draw(self, turtle):

        turtle.penup()
        turtle.goto(self.center_x - self.radius, self.center_y)  # From docs: The center is radius units left of the turtle;
        turtle.pendown()
        turtle.color(self.color)
        turtle.circle(self.radius)


class Square(Figure):
    def __init__(self, center_x, center_y, color, side, **kwargs):
        super().__init__(center_x, center_y, color, **kwargs)
        self.side = side

    def draw(self, turtle):
        half_side = self.side / 2
        left = self.center_x - half_side
        top = self.center_y + half_side

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)

class Rectangular(Figure):

    def __init__(self, center_x, center_y, color, width, height):
        super().__init__(center_x, center_y, color)

        self.width = width
        self.height = height

    def draw(self, turtle):

        left = self.center_x - self.width
        top = self.center_y + self.height

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)