import turtle
turtle.speed('fastest')

colors = ['gold', 'orange', 'lawngreen',  'deeppink', 'purple', 'red', 'deepskyblue']

for color in range(len(colors)):
    turtle.color(colors[color])
    angle = 1
    for counter in range(1, 200):
        turtle.forward(5)
        turtle.right(90 - angle)
        angle += 5
paxsTurtle = turtle.Turtle()
paxsTurtle.penup()
paxsTurtle.color('deepskyblue')
paxsTurtle.goto(-5, -58)
paxsTurtle.pendown()
paxsTurtle.circle(55)

paxsTurtle.penup()
paxsTurtle.color('red')
paxsTurtle.goto(76, 0)
paxsTurtle.width(3)

#P - start
paxsTurtle.pendown()
paxsTurtle.left(90)
paxsTurtle.forward(17)
paxsTurtle.right(90)
paxsTurtle.forward(7)
paxsTurtle.right(90)
paxsTurtle.forward(7)
paxsTurtle.right(90)
paxsTurtle.forward(7)
paxsTurtle.penup()
#P - end

#A - start
paxsTurtle.goto(90, 0)
paxsTurtle.right(90)
paxsTurtle.pendown()
paxsTurtle.forward(17)
paxsTurtle.right(90)
paxsTurtle.forward(7)
paxsTurtle.right(90)
paxsTurtle.forward(17)

paxsTurtle.penup()

paxsTurtle.goto(90, 11)
paxsTurtle.pendown()
paxsTurtle.left(90)
paxsTurtle.forward(13)
paxsTurtle.penup()
#A - end

#X - start
paxsTurtle.goto(104, 0)
paxsTurtle.pendown()
paxsTurtle.left(60)
paxsTurtle.forward(33)
paxsTurtle.penup()

paxsTurtle.goto(121, 0)
paxsTurtle.pendown()
paxsTurtle.left(60)
paxsTurtle.forward(33)
paxsTurtle.penup()
#X - end

#.
paxsTurtle.goto(130, 0)
paxsTurtle.pendown()
paxsTurtle.forward(1)
paxsTurtle.penup()
paxsTurtle.goto(137, 0)
turtle.done()