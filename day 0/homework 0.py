from turtle import * 

#we want to paint a house

#step 1:  draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left (90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#draing a door

forward(70)
color("purple")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window

penup()
goto(140,  140)
pendown()

color("cyan")
begin_fill()
left(120)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()



exitonclick()