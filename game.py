import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)

# Create a list to hold falling objects
falling_objects = []

# Function to create a new falling object
def create_falling_object():
    obj = turtle.Turtle()
    obj.shape("circle")
    obj.color("red")
    obj.penup()
    obj.speed(0)
    obj.goto(random.randint(-290, 290), 290)
    falling_objects.append(obj)

# Function to move the player left
def move_left():
    x = player.xcor()
    x -= 20
    if x < -290:
        x = -290
    player.setx(x)

# Function to move the player right
def move_right():
    x = player.xcor()
    x += 20
    if x > 290:
        x = 290
    player.setx(x)

# Keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Main game loop
while True:
    wn.update()

    # Create a new falling object every 30 frames
    if random.randint(1, 30) == 1:
        create_falling_object()

    # Move the falling objects
    for obj in falling_objects:
        y = obj.ycor()
        y -= 5
        obj.sety(y)

        # Check if the object has fallen off the screen
        if y < -300:
            obj.hideturtle()
            falling_objects.remove(obj)

        # Check for collision with the player
        if obj.distance(player) < 20:
            obj.hideturtle()
            falling_objects.remove(obj)
            print("Caught an object!")

wn.mainloop()
