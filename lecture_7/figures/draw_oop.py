import sys
import json
import turtle

from simple import Circle, Square

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

def create_figures(input_data: dict)-> []:
    result = []
    i = 1
    for f_info in input_data:
        type_figure = f_info['type_figure']
        if type_figure == 'square':
            square = Square(**f_info)
            # square = Square(
            #     type_figure = f_info['type_figure'],
            #     center_x=f_info['center_x'],
            #     center_y=f_info['center_y'],
            #     side=f_info['side'],
            #     color=f_info['color']
            # )
            result.append(square)

        elif type_figure == 'circle':
            circle = Circle(**f_info)
            # circle =  Circle(
            #     type_figure=f_info['type_figure'],
            #     center_x=f_info['center_x'],
            #     center_y=f_info['center_y'],
            #     radius=f_info['radius'],
            #     color=f_info['color']
            # )
            result.append(circle)
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

