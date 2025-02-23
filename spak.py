import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Space Invaders")
root.resizable(False, False)

# Set up the canvas
canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

# Create the player's spaceship
player = canvas.create_rectangle(370, 550, 430, 580, fill="white")

# Player movement
def move_left(event):
    canvas.move(player, -20, 0)

def move_right(event):
    canvas.move(player, 20, 0)

# Bind the left and right arrow keys to the movement functions
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Main game loop
def game_loop():
    # Here you can add code to move enemies, check for collisions, etc.
    root.after(50, game_loop)

# Start the game loop
game_loop()

# Run the Tkinter event loop
root.mainloop()
