import pygame
import time
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("One Punch Run")

music= pygame.mixer.Sound('victory.wav')

char= pygame.image.load("stand.png") 
bg = pygame.image.load('bg4.png')
winner = pygame.image.load('vic1.png')
#pygame.transform.scale(winner, (75, 25))
music.play(-1)
gameloop=True
while gameloop==True:
    win.blit(bg, (0,0))
    win.blit(char,(210,262))
    win.blit(winner,(80,100))
    pygame.display.update()
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
