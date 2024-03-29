import time
import turtle
from turtle import Turtle
from random import randint

# WINDOW SETUP
window = turtle.Screen()
window.title("TURTLE RACE")
turtle.bgcolor("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.color("black")
turtle.write("TURTLE RACE", font=("Arial",30, "bold"))
turtle.penup()

# DIRT
turtle.setpos(-400, -180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

# FINISH LINE
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line,(150 - (i* square_size *2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size *2)))
    turtle.stamp()
    
turtle.hideturtle()

# Turtle 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()



# Turtle 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("cyan")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()


# Turtle 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("magenta")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()


# Turtle 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("yellow")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()



time.sleep(1)  # pause the game for 1 second before starting the game

# MOVE THE TURTLE
for i in range(145):
    turtle1.up()
    turtle1.forward(randint(1,5))
    turtle2.up()
    turtle2.forward(randint(1,5))
    turtle3.up()
    turtle3.forward(randint(1,5))
    turtle4.up()
    turtle4.forward(randint(1,5))
    
    
    
turtle.exitonclick()