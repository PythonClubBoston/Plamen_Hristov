import sys
import json
import turtle

from simple import Circle, Square

FIGURE_TYPES = {'circle': Circle, 'square': Square}

def main():
    if len(sys.argv) < 2:
        print("Usage: {} input-file.json".format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        figures = create_figures(input_data)
        draw_figures(figures)
    except Exception as e:
        print("Invalid input file provided! Error: " + str(e))
        return 2

def load_input_data(input_filename):
    with open(input_filename) as f:
        input_data = json.load(f)
        return input_data

def create_figures(input_data: dict)-> []: # return List of objects type Figure
    result = []
    for f_info in input_data:
        type_figure = f_info['type_figure']

        if type_figure in FIGURE_TYPES:
            figure_class = FIGURE_TYPES[type_figure]
            result.append(figure_class(**f_info))
        else:
            raise ValueError("Unsupported figure")
    return result

def draw_figures(figures: []):
    i = 6
    for figure in figures:
        print(figure.type_figure)
        t = turtle.Turtle()
        t.speed('fast')
        figure.draw(t)
    turtle.exitonclick()

if __name__ == "__main__":
    sys.exit(main())

