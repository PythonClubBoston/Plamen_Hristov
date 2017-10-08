from .base import Figure

class Circle(Figure):

    def __init__(self, center_x, center_y, color, radius):
        super().__init__(center_x, center_y, color)
        self.radius = radius


class Rectangular(Figure):
    pass