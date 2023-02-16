import turtle
import tkinter as tk

# Create a turtle object
t = turtle.Turtle()
t.speed(0)

# Save the turtle's initial position
initial_pos = t.pos()
# Define functions to draw shapes
def draw_square():
    for i in range(4):
        t.forward(50)
        t.right(90)

def draw_circle():
    t.circle(50)

def draw_triangle():
    for i in range(3):
        t.forward(50)
        t.left(120)

def draw_koch_snowflake(length, depth):
    if depth == 0:
        t.forward(length)
        return
    for angle in [60, -120, 60, 0]:
        draw_koch_snowflake(length / 3, depth - 1)
        t.left(angle)

def draw_sierpinski(length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
        return

    draw_sierpinski(length / 2, depth - 1)
    t.forward(length / 2)
    draw_sierpinski(length / 2, depth - 1)
    t.backward(length / 2)
    t.left(60)
    t.forward(length / 2)
    t.right(60)
    draw_sierpinski(length / 2, depth - 1)
    t.left(60)
    t.backward(length / 2)
    t.right(60)

def draw_square_circle(length, depth):
    if depth == 0:
        return
    for _ in range(4):
        t.forward(length)
        t.left(90)
        t.penup()
        t.goto(t.xcor() - length/2, t.ycor() - length/2)
        t.pendown()
        t.circle(length/2)
        t.penup()
        t.goto(t.xcor() + length/2, t.ycor() + length/2)
        t.pendown()
        draw_square_circle(length/2, depth-1)
        t.penup()
        t.goto(t.xcor() + length/2, t.ycor() - length/2)
        t.pendown()


def clear_screen():
    t.clear()
    t.penup()
    t.goto(initial_pos)
    t.pendown()


# Create a tkinter window
root = tk.Tk()
root.title("Turtle Shapes")
root.title("Koch Snowflake Fractal")
root.title("Sierpinski Triangle")
root.title("Square-Circle Fractal")

# Set the world coordinates to prevent the turtle from going out of bounds
turtle.setworldcoordinates(-250, -250, 250, 250)


# Create buttons for each shape
square_button = tk.Button(root, text="Square", command=draw_square)
circle_button = tk.Button(root, text="Circle", command=draw_circle)
triangle_button = tk.Button(root, text="Triangle", command=draw_triangle)
clear_button = tk.Button(root, text="Clear", command=clear_screen)
koch_button = tk.Button(root, text="Draw Koch Snowflake", command=lambda: draw_koch_snowflake(300, 4))
sierpinski_button = tk.Button(root, text="Draw Sierpinski Triangle", command=lambda: draw_sierpinski(200, 4))
square_circle_button = tk.Button(root, text="Draw Square-Circle Fractal", command=lambda: draw_square_circle(200, 4))



# Add the buttons to the window
square_button.pack(side="left")
circle_button.pack(side="left")
triangle_button.pack(side="left")
clear_button.pack(side="left")
koch_button.pack(side="left")
clear_button.pack(side="left")
sierpinski_button.pack(side="left")
square_circle_button.pack(side="left")

# Run the tkinter event loop
root.mainloop()
