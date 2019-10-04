import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))

x=10
y=10

done = False
while not done:
    pygame.draw.rect(screen, (100,0,0), (x, y, x+50, y+50))
    pygame.display.flip()

    press = pygame.key.get_pressed()
    if press[pygame.K_a]: print("bull-shit")
    if press[pygame.K_ESCAPE]: done = True
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("fuck you")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            print("somthing")
        

pygame.quit()
