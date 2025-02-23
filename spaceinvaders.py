import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Space Invaders")
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

# Player settings
player = canvas.create_rectangle(275, 350, 325, 370, fill="blue")
player_speed = 20

# Enemy settings
enemy_speed = 2
enemies = []
for i in range(5):
    for j in range(3):
        enemy = canvas.create_rectangle(50 + i*100, 50 + j*50, 90 + i*100, 70 + j*50, fill="red")
        enemies.append(enemy)

# Player movement
def move_left(event):
    canvas.move(player, -player_speed, 0)

def move_right(event):
    canvas.move(player, player_speed, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Enemy movement
def move_enemies():
    for enemy in enemies:
        canvas.move(enemy, enemy_speed, 0)
        pos = canvas.coords(enemy)
        if pos[2] >= 600 or pos[0] <= 0:
            for e in enemies:
                canvas.move(e, 0, 20)
                global enemy_speed
                enemy_speed = -enemy_speed
            break
    root.after(50, move_enemies)

# Start the game
move_enemies()
root.mainloop()
