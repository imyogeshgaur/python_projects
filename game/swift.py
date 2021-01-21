import pygame
# add background
pygame.init()


gameWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Move The Box")

pygame.display.update()

gameClose =False

start_x=400
start_y =300
update_x = 0

clock = pygame.time.Clock()

background_Imaage = pygame.image.load("green.jpg").convert()

while not gameClose:
    for event in pygame.event.get():
        gameWindow.blit(background_Imaage,[0,0])
        pygame.draw.rect(gameWindow,(255,0,0),[start_x,start_y,25,25])  
        # x,y,length,width
        print(event)
        if event.type == pygame.QUIT:
            gameClose =True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                update_x = -25

            if event.key == pygame.K_RIGHT:
                update_x = +25
        
    start_x += update_x       
    pygame.display.update()

    clock.tick(12)
    # fps

pygame.quit()

quit()
