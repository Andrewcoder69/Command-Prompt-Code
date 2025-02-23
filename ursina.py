from ursina import *

app = Ursina()

def update():
    if held_keys['a']:
        cube.x -= 1 * time.dt
    if held_keys['d']:
        cube.x += 1 * time.dt

cube = Entity(model='cube', color=color.orange, scale=(2, 2, 2))
app.run()
