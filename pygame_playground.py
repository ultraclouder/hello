import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_icon(pygame.image.load('clouder_games.png'))
pygame.display.set_caption('DXR')
x = 50
y = 50
width = 40
height = 60
velocity = 5   

isJump = False
jumpCount = 10


# main loop
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > velocity:
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_d] and x < 500 - width:
        x += velocity
        left = False
        right = True
    else:
        right = False
        left = True
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_w] and y > velocity:
            y -= velocity
        if keys[pygame.K_s] and y < 500 - height:
            y += velocity
        if keys[pygame.K_SPACE]:
            isJump = True
 
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
