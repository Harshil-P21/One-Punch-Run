
import pygame
import random
import time
import textwrap

def game():
    import stage1


pygame.init()

display_width = 500
display_height = 500
gameDisplay = pygame.display.set_mode([display_width,display_height])
pygame.display.set_caption("Summative Game")
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)
lightblue=(187, 218, 237)
green = (0,200,0)
yellow = (255,215,0)
red = (200,0,0)
darkgrey=(83, 85, 86)
lightgrey=(142, 147, 150)
bright_green = (0,255,0)
bright_yellow = (255,255,0)
bright_red = (255,0,0)




all_sprites_list = pygame.sprite.Group()
clouds_list= pygame.sprite.Group()

def quitGame():
    pygame.quit()
    quit()

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,width,height,iC,aC,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # detect if "button" was pressed
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, aC, (x,y,width,height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, iC, (x,y,width,height))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(width/2)),(y+(height/2)) )
    gameDisplay.blit(textSurf, textRect)

class clouds(pygame.sprite.Sprite): 
    #setting Patrick vaules. Loading and scaling image, starting points, height and width
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image=pygame.image.load('clouds.png')
        self.rect=self.image.get_rect()
        self.rect.x=10 
        self.rect.y=20
        self.width=50
        self.height=80
clouds=clouds()
all_sprites_list.add(clouds)
class building(pygame.sprite.Sprite): 
    #setting Patrick vaules. Loading and scaling image, starting points, height and width
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image=pygame.image.load('building.png')
        self.rect=self.image.get_rect()
        self.rect.x=-30 
        self.rect.y=320
        self.width=50
        self.height=50
building=building()
all_sprites_list.add(building)

#frame1
class man1(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('man1.png')
        self.rect=self.image.get_rect()
        self.rect.x=200 
        self.rect.y=285
        self.width=500
        self.height=500
man1=man1()
all_sprites_list.add(man1)
#frame 2
class one(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('one.png')
        self.rect=self.image.get_rect()
        self.rect.x=5 
        self.rect.y=15
        self.width=100
        self.height=100
one=one()
all_sprites_list.add(one)
class punch(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('punch.png')
        self.rect=self.image.get_rect()
        self.rect.x=5 
        self.rect.y=10
        self.width=100
        self.height=100
punch=punch()
all_sprites_list.add(punch)
class run(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('run.png')
        self.rect=self.image.get_rect()
        self.rect.x=5 
        self.rect.y=160
        self.width=100
        self.height=100
run=run()
all_sprites_list.add(run)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((lightblue))
        #building
        all_sprites_list.draw(gameDisplay)
        #button
        button("PLAY",50,400,400,50,darkgrey,lightgrey,game)
        pygame.draw.rect(gameDisplay,lightgrey, (49, 400, 401, 51),2)

        #sprites
        
        all_sprites_list.update()
        #cloud movement
        clouds.rect.x += 1
        if clouds.rect.x >= 600:
            clouds.rect.x = -200
        pygame.display.update()
        clock.tick(15)


    
game_intro()

