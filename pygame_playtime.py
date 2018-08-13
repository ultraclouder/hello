import pygame
import sys
import time
pygame.init()
########## a to go left, d to go right, spacebar to jump, left click to throw boomerang
win = pygame.display.set_mode((500, 500))
pygame.display.set_icon(pygame.image.load('clouder_games.png'))
pygame.display.set_caption('play')
clock = pygame.time.Clock()
width = 64
length = 64
vel = 5
class player(object): 
    def __init__(self, x, y, width, height, vel, isJump, jumpCount):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.pushupCount = 0
        self.dopushups = False
        self.standing = True
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.pushupCount +1 >= 40:
            self.pushupCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//7], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//7], (self.x, self.y))
                self.walkCount += 1
                self.right = True
            elif self.dopushups:
                win.blit(pushUps[self.pushupCount//10], (self.x, self.y))
                self.pushupCount += 1
        else: 
            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(walkRight[0], (self.x, self.y))

class projectile(object):
    def __init__ (self, x, y, spinCount):
        self.x = x
        self.y = y
        self.spinCount = 0
        self.throw = False
        self.throwCount = 10
    def draw(self, win):
            if self.spinCount + 1 == 40:
                self.spinCount = 0
                self.throw = False
            if self.throw:
                self.spinCount += 1
                win.blit(boomerang[self.spinCount //10], (self.x, self.y))

class enemy(object):
    walkRight = [pygame.image.load('turtR1.png'), pygame.image.load('turtR1.png')]
    walkLeft = [pygame.image.load('turtL1.png'), pygame.image.load('turtL2.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
    def draw(self,win):
        self.move()
        if self.walkCount + 1 <= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
    def move(self):
        if self.vel > 0:
            if self.x <= self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
                if self.x > 0:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1    
                    self.walkCount = 0



dopushups = False     
bg = pygame.image.load('firstbackground.png')
pushUps = [pygame.image.load('gobpush1.png'), pygame.image.load('gobpush2.png'), pygame.image.load('gobpush3.png'), pygame.image.load('gobpush4.png')]
walkCount = 0
walkRight = [pygame.image.load('gobR1.png'), pygame.image.load('gobR2.png'), pygame.image.load('gobR3.png'), pygame.image.load('gobR4.png')]
walkLeft = [pygame.image.load('gobL1.png'), pygame.image.load('gobL2.png'), pygame.image.load('gobL3.png'), pygame.image.load('gobL4.png')]
boomerang = [pygame.image.load('boo1.png'),pygame.image.load('boo2.png'),pygame.image.load('boo3.png'),pygame.image.load('boo4.png')]
Char = pygame.image.load('char.png')
def redrawGameWindow(man_,proj_,turtle):
    win.blit(bg, (0, 0))
    man_.draw(win)
    turtle.draw(win)
    proj_.draw(win)
    pygame.display.update()




def main(argv):
# main loop

    
    man = player(250, 420, 64, 64, 5, False, 10)
    turtle = enemy(0, 450, 64, 64, 400)
    proj = projectile(man.x + 32, man.y + 16,0)
    man.jumpCount = 10
    man.isJump = False
    run = True
    while run == True:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()


        if keys[pygame.K_a] and man.x > 0:
            if proj.throw == False:    
                man.x -= man.vel
                man.left = True
                man.right = False
                man.dopushups = False
                man.standing = False

        elif keys[pygame.K_d] and man.x < 450:
            if proj.throw == False:
                man.x += man.vel
                man.left = False
                man.right = True
                man.dopushups = False
                man.standing = False
        elif keys[pygame.K_t]:
            man.dopushups = True
        else:
            man.dopushups = False
            man.standing = True
        if not(man.isJump):
            if keys[pygame.K_SPACE]:
                man.isJump = True
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                if man.jumpCount != 0:
                    man.y -= 10 * neg
                man.jumpCount -= 1
            else:
                man.jumpCount = 10
                man.isJump = False
        
        if not(proj.throw):
            proj.x = man.x - 32
            proj.y = man.y
            if man.left:
                proj.x = man.x - 32
                proj.y = man.y
            elif man.right:
                proj.x = man.x + 32
                proj.y = man.y
            else:
                proj.x = man.x + 32
                proj.y = man.y
            if (mouse[0]):
                proj.throw = True
        if proj.throw == True:
            if proj.throwCount >= -9:
                neg = 1
                if proj.throwCount < 1:
                    neg = -1
                if proj.throwCount != 0:
                    if man.left:
                        proj.x -= 10 * neg
                        if proj.x == man.x:
                            proj.throw = False
                        if neg == -1:
                            pass
                    elif man.right:
                        proj.x += 10 * neg
                        if proj.x == man.x - 32:
                            proj.throw = False
                        if neg == -1:
                            pass    
                proj.throwCount -= 1
            elif proj.throwCount < -9:
                proj.throwCount = 10
                proj.throw = False                
        redrawGameWindow(man,proj,turtle)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":   
    main(sys.argv)
#### end of file