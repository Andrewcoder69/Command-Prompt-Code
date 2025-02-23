import tkinter as tk
import random

root = tk.Tk()
root.title("Catch the Ball Game")
root.resizable(False, False)
canvas = tk.Canvas(root, width=400, height=400, bg="lightblue")
canvas.pack()

paddle = canvas.create_rectangle(175, 380, 225, 390, fill="blue")
paddle_speed = 20

ball = canvas.create_oval(190, 190, 210, 210, fill="red")
ball_speed = [3, 3]

def move_paddle(event):
    if event.keysym == "Left":
        canvas.move(paddle, -paddle_speed, 0)
    elif event.keysym == "Right":
        canvas.move(paddle, paddle_speed, 0)

root.bind("<Left>", move_paddle)
root.bind("<Right>", move_paddle)

def move_ball():
    canvas.move(ball, ball_speed[0], ball_speed[1])
    ball_pos = canvas.coords(ball)
    if ball_pos[0] <= 0 or ball_pos[2] >= 400:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball_pos[3] >= 400:
        canvas.coords(ball, 190, 190, 210, 210)
    root.after(30, move_ball)

move_ball()

def check_collision():
    ball_pos = canvas.coords(ball)
    paddle_pos = canvas.coords(paddle)
    if (paddle_pos[0] < ball_pos[2] < paddle_pos[2] or paddle_pos[0] < ball_pos[0] < paddle_pos[2]) and paddle_pos[1] < ball_pos[3] < paddle_pos[3]:
        ball_speed[1] = -ball_speed[1]
    root.after(10, check_collision)

check_collision()

root.mainloop()
