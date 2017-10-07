class Fridge:
    """
        This class implements a fridge where ingredients can be added and removed individually,
        or in groups. The fridge will retain a count of every ingredient added or removed,
        and will raise an error if a sufficient quantity of an ingredient isn't present.

        Methods:

        has(food_name [, quantity]) - checks if the string food_name is in the
        fridge. Quantity will be set to 1 if you don't secify a number.
        has_various(foods) - checks if enough of every food in the dictionary is in

        the fridge
        add_one(food_name) - adds a single food_name to the fridge
        add_many(food_dict) - adds a whole dictionary filled with food
        get_one(food_name) -
        get_many(food_dict) -
        get_ingredients(food) - If passed and object that has the __ingredients__ method, get_many
        will invoke this to get the list of ingredients.

    """
    def __init__(self, fridge_name='', brand=''):
        self.fridge_name = fridge_name
        self.brand = brand

    def print_fridge_name(self):
        print(self.fridge_name + ' : ' + self.brand)
f = Fridge(brand='Philips', fridge_name='Marisa')


f.print_fridge_name()