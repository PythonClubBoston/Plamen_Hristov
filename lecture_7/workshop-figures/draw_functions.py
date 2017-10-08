import sys
import json
import turtle

from simple_figures import Circle, Square, Rectangular
from complex_figures import Polygon, Pie


FIGURE_TYPES = {'circle': Circle, 'square': Square, 'rectangular' : Rectangular, 'polygon' : Polygon, 'pie' : Pie}

def main():

    if len(sys.argv) < 2:
        print("Usage: {} input-file.json".format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        figures_info = create_figures(input_data)
        draw_figures(figures_info)

    except Exception as e:
        print("Invalid input file provided! Error: " + str(e))
        return 2

def load_input_data(input_filename):

    with open(input_filename) as f:
        input_data = json.load(f)
        return input_data


def create_figures(input_data: dict)-> []: #Will create list of
    result = []
    for figure in input_data:
        figure_type = figure['type']
        del figure['type']
        if figure_type in FIGURE_TYPES:
            figure_class = FIGURE_TYPES[figure_type]
            result.append(figure_class(**figure))
        else:
            raise ValueError('Unsupported type')

    return result



def draw_figures(figures:[]):

    for figure in figures:
        t = turtle.Turtle()
        t.speed('fast')
        figure.draw(t)

    turtle.exitonclick()

if __name__ == "__main__":
    sys.exit(main())