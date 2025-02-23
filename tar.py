import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named "star"
star = turtle.Turtle()
star.color("blue")
star.speed(3)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        star.forward(size)
        star.right(144)

# Draw multiple stars
for i in range(5):
    draw_star(100)
    star.penup()
    star.forward(200)
    star.pendown()

# Hide the turtle and display the window
star.hideturtle()
turtle.done()
