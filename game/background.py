import pygame
# add background
pygame.init()

aqua=(0,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)

gameWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")

pygame.display.update()

gameClose =False

while not gameClose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameClose =True

    gameWindow.fill(aqua)
    pygame.display.update()

pygame.quit()

quit()