from base import Figure

class Circle(Figure):

    def __init__(self, type_figure, center_x, center_y, radius, color='black'):
        super().__init__(type_figure, center_x, center_y, color)
        self.radius = radius


    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x, self.center_y - self.radius)  # From docs: The center is radius units left of the turtle;
        turtle.pendown()
        turtle.color(self.color)
        turtle.circle(self.radius)

class Square(Figure):

    def __init__(self, type_figure, center_x, center_y, side, color='black'):
        super().__init__(type_figure, center_x, center_y, color)
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