import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Pong Game")

# Set up the canvas
canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

# Create paddles and ball
paddle1 = canvas.create_rectangle(30, 250, 50, 350, fill="white")
paddle2 = canvas.create_rectangle(750, 250, 770, 350, fill="white")
ball = canvas.create_oval(390, 290, 410, 310, fill="white")

# Variables to control the ball's movement
ball_dx = 3
ball_dy = 3

# Variables to control the paddles' movement
paddle1_dy = 0
paddle2_dy = 0

# Function to move paddles
def move_paddle1(event):
    global paddle1_dy
    if event.keysym == 'w':
        paddle1_dy = -5
    elif event.keysym == 's':
        paddle1_dy = 5

def stop_paddle1(event):
    global paddle1_dy
    paddle1_dy = 0

def move_paddle2(event):
    global paddle2_dy
    if event.keysym == 'Up':
        paddle2_dy = -5
    elif event.keysym == 'Down':
        paddle2_dy = 5

def stop_paddle2(event):
    global paddle2_dy
    paddle2_dy = 0

# Bind keys to paddle movement
root.bind('w', move_paddle1)
root.bind('s', move_paddle1)
root.bind('<KeyRelease-w>', stop_paddle1)
root.bind('<KeyRelease-s>', stop_paddle1)
root.bind('<Up>', move_paddle2)
root.bind('<Down>', move_paddle2)
root.bind('<KeyRelease-Up>', stop_paddle2)
root.bind('<KeyRelease-Down>', stop_paddle2)

# Function to update the game
def update_game():
    global ball_dx, ball_dy

    # Move paddles
    canvas.move(paddle1, 0, paddle1_dy)
    canvas.move(paddle2, 0, paddle2_dy)

    # Get current positions
    paddle1_pos = canvas.coords(paddle1)
    paddle2_pos = canvas.coords(paddle2)
    ball_pos = canvas.coords(ball)

    # Move ball
    canvas.move(ball, ball_dx, ball_dy)

    # Ball collision with top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[3] >= 600:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (ball_pos[0] <= paddle1_pos[2] and ball_pos[1] >= paddle1_pos[1] and ball_pos[3] <= paddle1_pos[3]) or \
       (ball_pos[2] >= paddle2_pos[0] and ball_pos[1] >= paddle2_pos[1] and ball_pos[3] <= paddle2_pos[3]):
        ball_dx = -ball_dx

    # Ball out of bounds
    if ball_pos[0] <= 0 or ball_pos[2] >= 800:
        canvas.coords(ball, 390, 290, 410, 310)
        ball_dx = -ball_dx

    # Schedule the next update
    root.after(20, update_game)

# Start the game loop
update_game()
root.mainloop()
