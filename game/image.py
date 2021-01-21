import pygame
# add background
pygame.init()


gameWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")

pygame.display.update()

gameClose =False

background_Image = pygame.image.load("quantum.jpg").convert()

while not gameClose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameClose =True


    gameWindow.blit(background_Image,[0,0])

    pygame.display.update()

pygame.quit()

quit()