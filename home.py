import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (135, 206, 235)
GREY = (128, 138, 135)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False
clock = pygame.time.Clock()
sun_x = 350
sun_y = 50
angle = 0
counter = 0

def scene(bgc,c):
    global angle, sun_x, sun_y
    screen.fill(bgc)
    pygame.draw.rect(screen, RED, [170, 170, 170, 170])
    pygame.draw.rect(screen, GREEN, [210, 210, 20, 20])
    pygame.draw.rect(screen, GREEN, [280, 210, 20, 20])
    pygame.draw.rect(screen, BLACK, [245, 300, 20, 40])
    pygame.draw.polygon(screen, GREEN, [[170, 170], [340, 170], [255, 100]])
    pygame.draw.rect(screen, GREEN, [0, 340, 1000, 1000])
    pygame.draw.circle(screen, c, (sun_x, sun_y), 30)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    angle += 1
    
    if angle >= 180:
        angle = 0
        counter = counter + 1
    radians = math.radians(angle) 
    
    sun_x = 260 + int(150 * math.cos(radians))
    sun_y = 100 - int(50 * math.sin(radians))
    
    if counter % 2 == 0:
        scene(BLUE,RED)
    else:
        scene(GREY,WHITE)
   
    pygame.display.flip()
    clock.tick(45)
pygame.quit()
