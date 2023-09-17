import pygame
import random 
import math
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('../content/ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load("../content/spaceship.png")
playerX,playerY = (370,450)
playerX_change = 0

enemyImg = pygame.image.load("../content/ufo_enemy.png")
enemyX,enemyY = (random.randint(0,800),random.randint(0,150))
enemyX_change = -4
enemyY_change = 0



#background image
background = pygame.image.load("../content/background.png")

#bullet
# stated the bullet is not moving False
# fired the bullet is on motion True
bulletImg = pygame.image.load("../content/bullet.png")
bulletState = False
bulletX = 0
bulletY = 0
bulletY_change = 5

def fire_bullet(x,y):
    screen.blit(bulletImg,(x,y))

def player(x,y):
    screen.blit(playerImg,( x, y))
def enemy(x,y):
    screen.blit(enemyImg,( x, y))
def bullet(x,y):
    screen.blit(bulletImg,(x,y))

def collission(x1,y1,x2,y2):
    distance = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    if distance < 27:
        return True
    return False

running = True
while running:
    # screen.fill((22,74,165))# RGB
    #Background
    screen.blit(background, (0,0))#this takes more time, so every movement is slower than before
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = +5
            if event.key == pygame.K_SPACE:
                if not bulletState:
                    bulletX = playerX+64//2
                    bulletY = playerY-24
                    bulletState = True
                    bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            # if event.key == pygame.K_SPACE:
            #     bulletState = False

    playerX += playerX_change
    if playerX > 800 - 64:
        playerX = 800-64
    if playerX < 0:
        playerX = 0

    if enemyX > 800 - 64:
        enemyX_change = -4
        enemyY_change = 5
    if enemyX < 0:
        enemyX_change = +4
        enemyY_change = 10

    enemyX += enemyX_change
    enemyY += enemyY_change    
    enemyY_change = 0

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    
    if bulletState and bulletY > 0:
        bulletY -= bulletY_change
        bullet(bulletX, bulletY)
    else:
        bulletState = False

    if bulletState and collission(enemyX,enemyY,bulletX,bulletY):
        bulletState = False
        enemyX = random.randint(0,800)
        enemyY = random.randint(0,150)


    pygame.display.update()# Display -> update
