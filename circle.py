import turtle
turtle.speed(0)
turtle.bgcolor('black')

turtle.color('red')
for c in range(60):
    for n in range(36):
        turtle.fd(25)
        turtle.rt(10)
    turtle.rt(6)

turtle.color('gold')
for c in range(30):
    for n in range(36):
        turtle.fd(20)
        turtle.rt(10)
    turtle.rt(12)
