import turtle

turtle.background_color('black')
turtle.speed(0)
turtle.width(1)
col=['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for n in range(255):
    turtle.color(col[n%6])
    turtle.forward(n)
    turtle.right(61)
