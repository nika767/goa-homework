from turtle import *


#we want to paint a house 

#step 1:draw a square
speed(40)
width(7)
shape("turtle")
color("blue")
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

forward(75)
color("green")
begin_fill()
left(90)
forward(120)
right(90)                       #the parametrs of the door
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

#drawing a right window

penup()
goto(199,190)
pendown()
color("black")
begin_fill()
right(60)                    #right window
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#drawing a left window

penup()
goto(0, 187)
pendown()
color("black")
begin_fill()
forward(50)
right(90)
forward(50)              #left window
right(90)
forward(50)
end_fill()


exitonclick()


#the end of the project