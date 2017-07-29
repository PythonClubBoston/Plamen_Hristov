import turtle

"""
Задача: 4. Рисуване в цикъл по зададени ъгъл и дължина на линията
 Назад
Направете програма, която по зададени ъгъл и дължина да рисува линии 
с turtle в безкраен цикъл, като всеки път завърта костенурката на подадения
 брой градуси, и рисува права линия със зададената дължина.

Ъгълът (в градуси) и дължината трябва да се въвеждат от конзолата при стартиране
 на програмата. За въвеждане от конзолата използвайте функцията input().

Turtle можете да използвате така:

import tutle

length = 100
turtle.left(length) 
turtle.forward(200)

Полезни операции с turtle:

turtle.forward(length) - чертае права линия напред с дължина length като премества и костенурката
turtle.backward(length) - чертае права линия назад с дължина length като премества и костенурката
turtle.left(degrees) - завърта костенурката наляво указания брой градуси.
turtle.right(degrees) - завърта костенурката надясно указания брой градуси.
turtle.color('red') - сменя цвета на чертане на костенурката; всички рисувания след това
 ще използват този цвят; За цветове можете да използвате 'black', 'red', 'green', 'blue',
  'orange', 'yellow', 'purple', и всички именовани цветове от HTML/CSS; също така можете да 
  използвате и HTML/CSS цветове, напр: '#BA3290'.
turtle.speed('fastest') - задава скоростта, с която костенурката рисува; можете да използвате 
'fastest', ''fast'', 'normal', 'slow' и 'slowest'.
"""

length = 20
angle = 90
turtle.bgcolor('skyblue')
true = True
turtle.penup()
x = -90
y = -90
turtle.goto(x, y)
turtle.pendown()
counter = 0

while counter < 40:
      
#RECT
  turtle.left(angle)
  turtle.forward(length)
  turtle.left(angle)
  turtle.forward(length)
  turtle.left(angle)
  turtle.forward(length)
  turtle.left(angle)
  turtle.forward(length)
  turtle.penup()

#NEW POSITION OF RECT
  
  counter += 10
  length += (length + counter)
  x += counter
  y += counter
  turtle.goto(x, y)
  turtle.pendown()

turtle.done()