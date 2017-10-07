import sys
import json
import turtle

from .figures.simple import Circle


def main():
    if len(sys.argv) < 2:
        print("Usage: {} input-file.json".format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        draw_figures(input_data)
    except Exception as e:
        print("Invalid input file provided! Error: " + str(e))
        return 2

def load_input_data(input_filename):
    with open(input_filename) as f:
        input_data = json.load(f)
        return input_data

def draw_figures(figures_info):
    t = turtle.Turtle()
    t.speed('fast')
    for f_info in figures_info:
        figure_type = f_info['type']
        if figure_type == 'square':
            draw_square(
                turtle_instance=t,
                center_x=f_info['center_x'],
                center_y=f_info['center_y'],
                side=f_info['side'],
                color=f_info['color']
            )
        elif figure_type == 'circle':
            draw_circle(
                turtle_instance=t,
                center_x=f_info['center_x'],
                center_y=f_info['center_y'],
                radius=f_info['radius'],
                color=f_info['color']
            )
        else:
            raise ValueError("Unsupported figure")

    turtle.exitonclick()

if __name__ == "__main__":
    sys.exit(main())

def draw_circle(turtle_instance, center_x, center_y, radius, color):

    turtle_instance.penup()
    turtle_instance.goto(center_x - radius, center_y)  # From docs: The center is radius units left of the turtle;
    turtle_instance.pendown()
    turtle_instance.color(color)
    turtle_instance.circle(radius)

def draw_square(turtle_instance, center_x, center_y, side, color):

    half_side = side / 2
    left = center_x - half_side
    top = center_y + half_side

    turtle_instance.penup()
    turtle_instance.goto(left, top)
    turtle_instance.pendown()
    turtle_instance.color(color)
    turtle_instance.forward(1)
    turtle_instance.setheading(270)  # point the turtle down
    for _ in range(4):
        turtle_instance.forward(side)
        turtle_instance.left(90)