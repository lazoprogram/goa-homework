from turtle import *

#we want to paint a house

#step 1:  draw a square
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("green")
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a  windows

color("yellow")
left(30)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)



right(180)
forward(200)
left(180)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)





exitonclick()