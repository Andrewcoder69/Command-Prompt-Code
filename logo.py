import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named "logo"
logo = turtle.Turtle()
logo.speed(3)

# Function to draw a circle
def draw_circle(radius, color):
    logo.penup()
    logo.goto(0, -radius)
    logo.pendown()
    logo.color(color)
    logo.begin_fill()
    logo.circle(radius)
    logo.end_fill()

# Function to draw a star
def draw_star(size, color):
    logo.penup()
    logo.goto(-size/2, size/2)
    logo.pendown()
    logo.color(color)
    logo.begin_fill()
    for _ in range(5):
        logo.forward(size)
        logo.right(144)
    logo.end_fill()

# Draw the circle
draw_circle(100, "blue")

# Draw the star
draw_star(100, "yellow")

# Hide the turtle and display the window
logo.hideturtle()
turtle.done()
