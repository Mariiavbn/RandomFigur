import random
import pygame as pg

size = (500, 500)
screen = pg.display.set_mode(size)

fps = 5
clock = pg.time.Clock()

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    screen.fill(pg.Color(r, g, b))

    type = random.randint(0, 3)
    rectelips = (r, g, 158, b)
    if type == 0:
        #pg.draw.rect(screen, pg.Color(r, b, g), (r, g, 100, 58), 4)
        pg.draw.rect(screen, pg.Color(r, b, g), rectelips)
    if type == 1:
        pg.draw.circle(screen, pg.Color(g, r, b), (g, r), 200)
    if type == 2:
        #pg.draw.ellipse(screen, pg.Color(g, r, b), (b, r, 70, 100))
        pg.draw.ellipse(screen, pg.Color(g, r, b), rectelips)
    if type == 3:
        pg.draw.polygon(screen, pg.Color(g, b, r), ((g, b), (450, 70), (53, 62)))

    pg.draw.line(screen, pg.Color("black"), (84, 267), (418, 218))

    pg.display.flip()
    clock.tick(fps)