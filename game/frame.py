import pygame
# add frame and event
pygame.init()

gameWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")

pygame.display.update()
while True:
    for event in pygame.event.get():
        print(event)

pygame.quit()

quit()