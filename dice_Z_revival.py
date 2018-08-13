import pygame
import random
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_icon(pygame.image.load('clouder_games.png'))
class player(object):
    def __init__(self, x, y, width, height, vel, walkCount):
        self.x = 250
        self.y = 250
        self.width = 64
        self.height = 64
        self.vel = 5
        self.walkCount = 0
        self.standing = True
###### GET SPRITES
    def draw(self, win, left, right):
        if not(self.standing):
            if self.left:
                win.blit()
            elif self.right:
                win.blit()
            else:
                win.blit()
        else:
            if self.left:
                win.blit()
            else:
                win.blit()
###### GET SPRITES
isJump = False
jumpCount = 10
# big loop
man = player(250, 250, 64, 64, 5, 0)
run = True
while run == True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and man.x > 0:
        man.x -= man.vel
        man.standing = False
        right = False
        left = True
    if keys[pygame.K_d] and man.x < 500:
        man.x += man.vel
        man.standing = False
        right = True
        Left = False
    if keys[pygame.K_SPACE]:
        isJump = True
    if (isJump):
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            jumpCount -= 1  
            y -= 5 * neg
    pygame.display.update()

            


