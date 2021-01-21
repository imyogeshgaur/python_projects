import pygame
# event handling 
pygame.init()

gameWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")

pygame.display.update()

gameClose = False
while not gameClose:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
           gameClose = True

pygame.quit()

quit()