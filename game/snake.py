import pygame

pygame.init()

game = pygame.display.set_mode((480,320))
pygame.display.set_caption("Snake Game")
pygame.display.update()

closeGame = False

while not closeGame:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            closeGame = True
       
    game.blit(pygame.image.load("6.png"),[0,0])
    pygame.display.update()

pygame.quit()

quit()