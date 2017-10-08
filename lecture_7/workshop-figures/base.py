class Figure:

    def __init__(self, center_x: int, center_y: int, color: str):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def __str__(self):
        return "Figure : ({}, {})".format(self.center_x, self.center_y)

    def draw(self, turtle):
        pass

    def jump_to(self, turtle, x, y):
        pass

        # turtle.penup()
        # turtle.goto(x, y)
        # turtle.pendown()