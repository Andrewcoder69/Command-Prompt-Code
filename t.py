import tkinter as tk

class PlatformerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Platformer Game")
        self.canvas = tk.Canvas(root, width=800, height=600, bg="skyblue")
        self.canvas.pack()

        self.player = self.canvas.create_rectangle(50, 550, 100, 600, fill="red")
        self.platforms = [
            self.canvas.create_rectangle(0, 580, 800, 600, fill="green"),
            self.canvas.create_rectangle(150, 450, 300, 470, fill="green"),
            self.canvas.create_rectangle(400, 350, 550, 370, fill="green"),
            self.canvas.create_rectangle(600, 250, 750, 270, fill="green")
        ]

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
        self.canvas.bind_all("<KeyPress-Up>", self.jump)

        self.gravity = 2
        self.jump_speed = -20
        self.player_speed = 10
        self.player_velocity_y = 0

        self.update_game()

    def move_left(self, event):
        self.canvas.move(self.player, -self.player_speed, 0)

    def move_right(self, event):
        self.canvas.move(self.player, self.player_speed, 0)

    def jump(self, event):
        if self.is_on_ground():
            self.player_velocity_y = self.jump_speed

    def is_on_ground(self):
        player_coords = self.canvas.coords(self.player)
        for platform in self.platforms:
            platform_coords = self.canvas.coords(platform)
            if (player_coords[2] > platform_coords[0] and player_coords[0] < platform_coords[2] and
                player_coords[3] >= platform_coords[1] and player_coords[3] <= platform_coords[3]):
                return True
        return False

    def update_game(self):
        self.player_velocity_y += self.gravity
        self.canvas.move(self.player, 0, self.player_velocity_y)

        if self.is_on_ground():
            self.player_velocity_y = 0

        self.root.after(50, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = PlatformerGame(root)
    root.mainloop()
