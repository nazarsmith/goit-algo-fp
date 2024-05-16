import turtle
import math

def koch_curve(t, order, size):
    print(size)
    if order == 0:
        
        print("move", size / 3)
        t.forward(size / 3)
    else:
        for angle in [30, 180, 120, 180]:
            koch_curve(t, order - 1, size / (math.sqrt(size) / 2))
            print(f"turn {angle}")
            t.left(angle)

def draw_koch_curve(order, size=30000):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(1)  
    t.penup()
    t.goto(0 / 3, 0)
    t.pendown()
    t.left(90)

    for _ in range(2):
        koch_curve(t, order, size)
        print("turn wha")
        t.right(180)
        # t.forward(size / 3)
    window.mainloop()

draw_koch_curve(2) ## order
