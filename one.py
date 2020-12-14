import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill('white')
circle(screen, (255,190,70), (200, 200), 70)
circle(screen, (1,1,1), (200, 200), 70, 1)
circle(screen, ('white'), (170, 170), 20)
circle(screen, ('white'), (230, 170), 20)
circle(screen, 'black', (170, 170), 20, 1)
circle(screen, ('black'), (230, 170), 20, 1)
circle(screen, ('black'), (170, 170), 10)
circle(screen, ('black'), (230, 170), 10)
polygon(screen, (0, 0, 0), [(170,220), (230,220),
                               (220,230), (180,230) ])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()