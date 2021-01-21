import pygame as pyg

pyg.init()

pink = (255,0,255)
yellow = (255,255,0)

frame = pyg.display.set_mode((800,400))
frame1 = pyg.display.set_mode((800,400))
pyg.display.set_caption("Yogesh Gaur")
pyg.display.set_caption("Aman Solanki")

setX=400
setY=200
setX1 = 400
setY1 = 200


background = pyg.image.load("green.jpg").convert()
pyg.display.update()

gameClose = False

while not gameClose:

    frame.blit(background,[0,0])
    pyg.draw.circle(frame,pink,(setX,setY),25)
    pyg.draw.rect(frame,yellow,[setX1,setY1,25,25])
    pyg.display.update()

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            gameClose = True
        print(event)

        if event.type == pyg.KEYDOWN:

            if event.key == pyg.K_LEFT:
                setX -= 25
            
            if event.key == pyg.K_RIGHT:
                setX += 25

            if event.key == pyg.K_UP:
                setY -= 25

            if event.key == pyg.K_DOWN:
                setY += 25
    
pyg.quit()

quit()   
            
