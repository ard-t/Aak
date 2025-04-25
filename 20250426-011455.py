import turtle
import time

# Set up screen
screen = turtle.Screen()
screen.title("Turtle Scanner Simulation")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Draw scanner frame
frame = turtle.Turtle()
frame.color("green")
frame.pensize(3)
frame.penup()
frame.goto(-200, 200)
frame.pendown()
for _ in range(4):
    frame.forward(400)
    frame.right(90)
frame.hideturtle()

# Create scanner line
line = turtle.Turtle()
line.color("lime")
line.pensize(2)
line.penup()
line.goto(-200, 200)
line.pendown()

# Animation loop
line_speed = 5
y = 200

while True:
    # Clear old line
    line.clear()
    line.penup()
    line.goto(-200, y)
    line.pendown()
    line.forward(400)

    y -= line_speed
    if y < -200:
        y = 200  # Reset line to top

    time.slee