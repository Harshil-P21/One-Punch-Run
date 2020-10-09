import pygame
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("One Punch Run")

######################################################################## load images
walkRight = [pygame.image.load('walk1.png'),pygame.image.load('walk2.png'),pygame.image.load('walk3.png'),pygame.image.load('walk4.png')]
walkLeft = [pygame.image.load('walkl1.png'),pygame.image.load('walkl2.png'),pygame.image.load('walkl3.png'),pygame.image.load('walkl4.png')]
char= pygame.image.load("stand.png") 

bg = pygame.image.load('bg3.png')
######################################################################## music n sounds
bulletsound= pygame.mixer.Sound('punch.wav')
hitsound= pygame.mixer.Sound('hitsound.wav')
#music= pygame.mixer.music.load('zeze.mp3')
#pygame.mixer.music.play(-1)

####################################################################### CLOCK AND SCORE
time=0
clock = pygame.time.Clock()
score = 0



###################################################### importing ending
def ending():
    import ending

####################################################################### DEFINING PLAYER AND ANIMATIONS AND WHAT HAPPENS IF HE GETS HIT

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox= (self.x + 35, self.y, 28, 60)
        
    def draw(self, win):
        if self.walkCount + 1 >= 12:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(char,(self.x,self.y))
        self.hitbox= (self.x + 35, self.y, 28, 60)

        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)


    def hit(self):
        self.isJump = False
        self.jumpCount= 10
        self.x=-20
        self.y=410
        font1=pygame.font.SysFont('ebrima', 100)
        text = font1.render('OOF', 1,(255,0,0))
        win.blit(text, (230, 200))
        pygame.display.update()
        i= 0
        while i <300:
            pygame.time.delay(1)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i= 101
                    pygame.quit()
        #have to do something with the charecter

####################################################################### MAKING SURE THE BULLET IS FIRED THE RIGHT WAY

class projectile(object):
    def __init__(self,x,y,radius,color, facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing= facing
        self.vel= 8*facing

    def draw(self, win):
        pygame.draw.circle(win, self.color,(self.x,self.y), self.radius)

####################################################################### MAKING
class bboros(object):
    walkRight = [pygame.image.load('boros1r.png'),pygame.image.load('boros2r.png'),pygame.image.load('boros3r.png'),pygame.image.load('boros4r.png')]
    walkLeft = [pygame.image.load('boros1l.png'),pygame.image.load('boros2l.png'),pygame.image.load('boros3l.png'),pygame.image.load('boros4l.png')]
    def __init__(self, x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path= [self.x , self.end]
        self.walkCount =0
        self.vel = 18
        self.hitbox= (self.x + 30, self.y+15, 28, 55)
        self.health= 20
        self.visible= True    
    def draw(self,win):
        if self.visible:
            self.move()
            if self.walkCount +1 >= 12:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount +=1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount +=1


            pygame.draw.rect(win, (255,0,0), (self. hitbox[0], self.hitbox[1]-10, 100, 10,))
            pygame.draw.rect(win, (0,255,0), (self. hitbox[0], self.hitbox[1]-10, 50 - (5 *(10 - self.health)), 10,))  
            self.hitbox= (self.x+80, self.y+10, 80, 150)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
    def move(self):
        if self.vel > 0:
            if self.x+ self.vel  <  self.path[1]:
                self.x +=self.vel
            else:
                self.vel = self.vel *-1
                self.walkCount=0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel *-1
                self.walkCount=0
    def hit(self):
        if self. health > 0:
            self.health = self.health - 1
        else:
            self.visible= False
        print ("omega")



#######################################################################  DRAWING LOOPS (TO DRAW THE DIFFERENT STAGES)                
        
def redrawGameWindow():
    if man.x<500:
        win.blit(bg, (0,0))     
        #text= font.render('Score :' + str(score), 1, (245, 247, 155))
        #win.blit(text, (380, 15)) #score on screen lol
        man.draw(win)
        boros.draw(win)
        


            
        for bullet in bullets:
            bullet.draw(win)
    else:
        ending()
        
    pygame.display.update()
font = pygame.font.SysFont('georgia', 25, True , True )#bold, italics
man = player(-20, 410, 64,64)
boros = bboros(0, 290, 64, 64, 450)


stagex=30
shoot = 0
bullets = []
run = True
while run:
    clock.tick(27)

        
        
    if boros.visible == True:
        if man.hitbox[1] < boros.hitbox[1] + boros.hitbox[3] and man.hitbox[1] + man.hitbox[3] > boros.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > boros.hitbox[0] and man.hitbox[0] < boros.hitbox[0] + boros.hitbox[2]:
                man.hit()
                score -= 5
    if shoot > 0:
        shoot +=1
    if shoot > 3:
        shoot = 0
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:        
        if bullet.y - bullet.radius < boros.hitbox[1] + boros.hitbox[3] and bullet.y +bullet.radius > boros.hitbox[1]:
            if bullet.x + bullet.radius > boros.hitbox[0] and bullet.x - bullet.radius < boros.hitbox[0] + boros.hitbox[2]:
                if boros.visible == True:
                    hitsound.play()
                    boros.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
        if bullet.x < 600 and bullet.x > 0:
            bullet.x += bullet.vel  
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if man.x>10:
        if keys[pygame.K_SPACE] and shoot == 0 :
            bulletsound.play()
            
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
                bullets.append(projectile(round(man.x+man.width//2), round(man.y + man.height//2), 6, (0,255,0), facing)) 

            shoot= 1

    if boros.visible == True:     
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            stagex -= man.vel
            man.left = True
            man.right = False
            man.standing = False 
        elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
            man.x += man.vel
            stagex += man.vel
            man.right = True
            man.left = False
            man.standing = False 
        else:
            man.standing = True
            man.walkCount = 0
    elif boros.visible == False:
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            stagex -= man.vel 
            man.left = True
            man.right = False
            man.standing = False 
        elif keys[pygame.K_RIGHT]:
            man.x += man.vel
            stagex += man.vel
            man.right = True
            man.left = False
            man.standing = False 
        else:
            man.standing = True
            man.walkCount = 0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()
 
            

pygame.quit()
