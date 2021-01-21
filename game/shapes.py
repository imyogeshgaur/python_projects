import pygame
# add background
pygame.init()


gameWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")

pygame.display.update()

gameClose =False

background_Imaage = pygame.image.load("quantum.jpg").convert()

while not gameClose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameClose =True


    gameWindow.blit(background_Imaage,[0,0])
    pygame.draw.line(gameWindow,(0,255,0),[0,0],[50,30])
    pygame.draw.polygon(gameWindow,(255,255,255),[[100,200],[34,23],[21,56],[23,46],[42,50]])
    pygame.draw.rect(gameWindow,(255,0,0),[75,10,25,75])  
    pygame.draw.circle(gameWindow,(0,0,255),[400,300],40,20)
    # x,y,length,width
    pygame.display.update()

pygame.quit()

quit()