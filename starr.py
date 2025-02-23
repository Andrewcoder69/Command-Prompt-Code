import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the speed to the maximum

# List of colors to use in the pattern
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# Function to draw a spiral pattern
def draw_spiral():
    for i in range(360):
        pen.color(random.choice(colors))
        pen.forward(i * 2)
        pen.right(121)  # Change the angle to create different patterns

# Function to draw a star pattern
def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

# Function to draw a complex pattern combining spirals and stars
def draw_complex_pattern():
    for _ in range(36):
        draw_spiral()
        pen.right(10)
        draw_star(100)
        pen.right(10)

# Draw the complex pattern
draw_complex_pattern()

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()
