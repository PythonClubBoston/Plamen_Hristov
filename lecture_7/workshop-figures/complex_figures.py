from simple_figures import Circle



class Polygon(Circle):

    def __init__(self, center_x, center_y, color, radius, num_sides):
        super().__init__(center_x, center_y, color, radius)
        self.num_sides = num_sides

    def draw(self, turtle):

        turtle.penup()
        turtle.goto(self.center_x - self.radius, self.center_y)  # From docs: The center is radius units left of the turtle;
        turtle.pendown()
        turtle.color(self.color)
        angle = 360.0 / self.num_sides

        for i in range(self.num_sides):
            turtle.forward(self.radius)
            turtle.right(angle)

class Pie(Circle):

    def __init__(self, center_x, center_y, color, radius, percentage):
        super().__init__(center_x, center_y, color, radius)
        self.percentage = percentage

    def draw(self, turtle):

        pie_angle = self.percentage * 3.6
        turtle.penup()
        turtle.goto(self.center_x - self.radius, self.center_y)  # From docs: The center is radius units left of the turtle;
        turtle.pendown()
        turtle.color(self.color)
        turtle.circle(self.radius)
        turtle.left(90)
        turtle.forward(self.radius)
        turtle.left(pie_angle)
        turtle.forward(self.radius)