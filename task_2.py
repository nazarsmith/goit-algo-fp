import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # Fastest drawing speed

def draw_tree(length, order):
    if order == 0:
        return
    
    # Draw the trunk
    t.forward(length)
    # Save the current position and heading
    pos = t.position()
    heading = t.heading()
    
    # Left branch
    t.left(degree)
    draw_tree(length * math.sqrt(2) / 2, order - 1)

    # Restore the position and heading
    t.setposition(pos)
    t.setheading(heading)
    
    # Right branch
    t.right(degree)
    draw_tree(length * math.sqrt(2) / 2, order - 1)
    
    # Restore the position and heading
    t.setposition(pos)
    t.setheading(heading)

# Initial parameters
initial_length = 100
initial_order = 7
degree = 35

# Move the turtle to the starting position
t.penup()
t.goto(0, -200)
t.left(90)
t.pendown()

# Draw the tree
draw_tree(initial_length, initial_order)

# Finish up
turtle.done()
