from turtle import *
hideturtle()
pensize(10)
circle(50)

up()
goto(-50, -25)
down()
for i in range(4):
    forward(100)
    circle(25, 90)

up()
goto(55, 95)
down()
circle(5, 360)
done()
