class Figure:

    def __init__(self, type_figure, center_x, center_y, color):

        self.type_figure = type_figure
        self.center_x =  center_x
        self.center_y =  center_y
        self.color = color

    def __str__(self):
        return "Figure center_x is {}" \
               " center_y is {} and the color is {} the type is {}".format(
            self.center_x, self.center_y, self.color, self.type_figure)

    def draw(self, turtle):
        pass
