import pgzrun
from random import randint

TITLE = "Nice Shot!"
WIDTH = 500
HEIGHT = 500

message = ""

alien = Actor('alien')

def draw():
    screen.clear()
    screen.fill(color = (128, 0, 0))

    alien.draw()
    screen.draw.text(message, center = (250, 20), fontsize = 30)

def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, WIDTH-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Nice Shot!"
        place_alien()
    else:
        message = "What a save!"

place_alien()
pgzrun.go()