import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Dino jumper")

clock = pygame.time.Clock()

doExit = False

p1x = 20
p1y = 200
yVel = 10
touchGround = False

CactusHeights= [80,40,20,80,30]

CactusXpos=[]

for x in range(1, 5):

    CactusXpos.append(random.randrange(200, 3000))
    
#CactusImg = pygame.image.load('cactus.png')

#gameloop
while not doExit: 
            
#timer
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True;
            
    p1y += yVel

    CactusXpos = [x - 5 for x in CactusXpos]

    for x in range(len(CactusXpos)):
        if CactusXpos[x]<0:
            CactusXpos[x]=random.randrange(640, 5000)
            print("reset to", CactusXpos[x])
            
    for x, y in zip(CactusXpos, CactusHeights):
        a = pygame.Rect((x, 480-y), (30, 80))
        b = pygame.Rect((p1x, p1y), (30, 30))
        if a.colliderect(b) == True:
            print("Collision")
#gravity
    if (p1y+30) > 480:
        touchGround = True
    else:
        touchGround = False
        
    if touchGround == False:
        yVel += 0.5 #gravity
    else:
        yVel = 0
            
    #input section
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and touchGround == True:
        p1y-= 300 #jump
        
 #render section
    screen.fill((0,0,0))
         
#dino
    pygame.draw.rect(screen, (61, 145, 64), (p1x, p1y, 40, 40), 20)
    
    for x, y in zip(CactusXpos, CactusHeights):
        pygame.draw.rect(screen, (0, 255, 0), (x-15, 480-y, 20, 100))
        #screen.blit(CactusImg, (x-15,480-y))

    pygame.display.flip()
 #end game loop
pygame.quit()

