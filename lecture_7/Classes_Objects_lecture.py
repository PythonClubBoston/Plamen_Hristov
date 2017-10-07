class Figure:


    #__init__ and all methods with '__' are called magic methods
    #__init__ is like the constructor in other languagies initialize properties
    #  of the class
    def __init__(self, center, color):
        self.center =  center
        self.color = color
    def __str__(self):
        return "Figure center is {} and color is {}".format(
            self.center, self.color)

    #for all methods in class -> first arguments is always self

    def print(self):
        print("Figure center is {} and color is {}"
              .format(self.center, self.color))

class Circle(Figure):

    def __init__(self, center, color, radius):
        super().__init__(center, color)
        self.radius = radius

    def __str__(self):  #This is equal to toString() you should always do that

        return \
            super().__str__() + " radius: " + str(self.radius)
        #     "Circle center is {} and color is {}, radius is {}".format(
        #             self.center,
        #             self.color,
        #             self.radius,
        # )


     #indent is with default value if for some reason we do not place it when we call it
    def print(self, indent=4):
        print("{} : Circle center is {} and color is {}, radius is {}"
              .format(' '*indent, self.center, self.color, self.radius))

c = Circle((10, 20), 'Red', 14)
print(c)