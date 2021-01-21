import pygame
# add background
pygame.init()


gameWindow = pygame.display.set_mode((480,300))
pygame.display.set_caption("Move The Box")

pygame.display.update()

gameClose =False

start_x=240
start_y =150


background_Imaage = pygame.image.load("green.jpg").convert()

while not gameClose:
    for event in pygame.event.get():
        gameWindow.blit(background_Imaage,[0,0])
        pygame.draw.rect(gameWindow,(255,0,0),[start_x,start_y,25,25])  
        # x,y,length,width
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                start_x -= 25
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                start_x += 25
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                start_y -= 25
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                start_y += 25
        if event.type == pygame.QUIT:
            gameClose =True


    pygame.display.update()

pygame.quit()

quit()