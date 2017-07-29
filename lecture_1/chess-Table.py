import turtle

def draw_filled_rect(color, size):#default values 'black' and 40 pixels per rectangular of the chess
    counter = 0
    turtle.begin_fill()
    while (counter < 4):
        turtle.color(color)
        turtle.forward(size)
        turtle.left(90)
        counter += 1
    turtle.up()    
    turtle.end_fill()

def draw_empty_rect(color, size): #default values 'black' and 40 pixels per rectangular of the chess
    counter = 0
    while (counter < 4):
        turtle.color(color)
        turtle.forward(size)
        turtle.left(90)
        counter += 1
    turtle.up()

def draw_rows(num_of_rows = 8):
    count_of_cols = 0
    count_of_rows = 0
    init_position_x = -200
    init_position_y = -160
    turtle.up()
    turtle.goto(init_position_x,init_position_y)

    while(count_of_rows < num_of_rows):

        current_position_y = init_position_y + count_of_rows*40

        #draw a rect with filling
        if(count_of_rows % 2 == 0):
            while(count_of_cols < 8):
                count_of_cols += 1
                current_position_x = init_position_x + count_of_cols*40
                turtle.goto(current_position_x, current_position_y)
                if(count_of_cols % 2 != 0):
                    draw_filled_rect(color = 'black', size = 40)

        else:
            while(count_of_cols < 8):
                count_of_cols += 1
                current_position_x = init_position_x + count_of_cols*40
                turtle.goto(current_position_x, current_position_y)
                if(count_of_cols % 2 == 0):
                    draw_filled_rect(color='black', size=40)


        count_of_rows += 1
        count_of_cols = 0
    turtle.pendown()


# needed variables rows and cols
# size_of_rect


#draw_empty_rect(color='black', size = 40)

draw_rows(8)
turtle.penup()
turtle.goto(-160,-160)
turtle.pendown()
draw_empty_rect('black', 320)
turtle.done()