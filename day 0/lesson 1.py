from turtle import *


# we want to paint a house

speed(30)
width(7)
color("purple")
#step 1 draw a square
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


 
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
left(90)
forward(30)
width(9)
color("green")
goto(10, 190 )
pendown()
left(30)
forward(45)
right(90)
forward(55)
right(90)
forward(45)
right(90)
forward(55)

penup()

width(9)
color("green")
goto(145, 190)
pendown()
right(90)
forward(45)
right(90)
forward(55)
right(90)
forward(45)
right(90)
forward(55)
pendown()
color("green")
begin_fill()



exitonclick()









