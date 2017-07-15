import turtle

def drawRectangular(color, size):
    counter = 0
    turtle.begin_fill()
    while (counter < 4):
        turtle.color(color)
        turtle.forward(size)
        turtle.left(90)
        counter += 1
    turtle.up()    
    turtle.end_fill()

def moveTurtle(sizeOfRect):
    turtle.up()
    turtle.goto(sizeOfRect)
    turtle.down()

def drawBoard(sizeOfSide):

    turtle.goto(0, 0)
    turtle.pendown()
    counter = 0
    currentSize = 0

    while(counter < 4):
        if(counter%2==0):
            drawRectangular('black', sizeOfSide/8)
        else:
            drawRectangular('white', sizeOfSide/8)              
        counter += 1
        currentSize += sizeOfSide/8
        moveTurtle(currentSize)
        
drawBoard(240)
turtle.done()