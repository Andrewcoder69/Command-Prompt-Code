import tkinter as tk
import random

class CatchTheBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Ball Game")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        
        self.paddle = self.canvas.create_rectangle(175, 380, 225, 390, fill='blue')
        self.ball = self.canvas.create_oval(190, 190, 210, 210, fill='red')
        
        self.ball_speed = [3, 3]
        self.paddle_speed = 20
        
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)
        
        self.update_game()
    
    def move_left(self, event):
        self.canvas.move(self.paddle, -self.paddle_speed, 0)
    
    def move_right(self, event):
        self.canvas.move(self.paddle, self.paddle_speed, 0)
    
    def update_game(self):
        self.canvas.move(self.ball, self.ball_speed[0], self.ball_speed[1])
        
        ball_pos = self.canvas.coords(self.ball)
        paddle_pos = self.canvas.coords(self.paddle)
        
        if ball_pos[2] >= 400 or ball_pos[0] <= 0:
            self.ball_speed[0] = -self.ball_speed[0]
        
        if ball_pos[1] <= 0:
            self.ball_speed[1] = -self.ball_speed[1]
        
        if ball_pos[3] >= 400:
            if paddle_pos[0] < ball_pos[2] and paddle_pos[2] > ball_pos[0]:
                self.ball_speed[1] = -self.ball_speed[1]
            else:
                self.canvas.create_text(200, 200, text="Game Over", font=('Helvetica', 24), fill='red')
                return
        
        self.root.after(20, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = CatchTheBallGame(root)
    root.mainloop()
