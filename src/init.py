import pygame
from pygame import mixer
import random 
import math

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('../content/ufo.png')
pygame.display.set_icon(icon)

mixer.music.load("../content/background.wav")
mixer.music.play(-1)

score = 0
font = pygame.font.Font("../content/Cheese Burger.otf", 32)
textX = 10
textY = 10
over_font = pygame.font.Font("../content/Cheese Burger.otf", 80)

def show_score(x,y):
    score_text = font.render("Score: "+str(score), True, (255,255,255))
    screen.blit(score_text, (x,y))

def display_game_over():
    over_text = over_font.render("GAME OVER", True, (255, 0 , 0))
    screen.blit(over_text,(320, 250))

playerImg = pygame.image.load("../content/spaceship.png")
playerX,playerY = (370,450)
playerX_change = 0

# enemyImg = pygame.image.load("../content/ufo_enemy.png")
# enemyX,enemyY = (random.randint(0,800),random.randint(0,150))
# enemyX_change = -4
# enemyY_change = 0

n_enemies = 6
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for e in range(n_enemies):
    enemyImg.append(pygame.image.load("../content/ufo_enemy.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(-4)
    enemyY_change.append(0)



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
def enemy(x,y,e):
    screen.blit(enemyImg[e],( x, y))
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
                    bullet_sound = mixer.Sound("../content/laser.wav")
                    bullet_sound.play()
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

    for e in range(n_enemies):
        if enemyY[e] > 400:
            if collission(enemyX[e],enemyY[e], playerX, playerY):
                display_game_over()
                bulletState = False
                break
                
        if enemyX[e] > 800 - 64:
            enemyX_change[e] = -4
            enemyY_change[e] = 45
        if enemyX[e] < 0:
            enemyX_change[e] = +4
            enemyY_change[e] = 45

        enemyX[e] += enemyX_change[e]
        enemyY[e] += enemyY_change[e]
        enemyY_change[e] = 0

        if bulletState and collission(enemyX[e],enemyY[e],bulletX,bulletY):
            explosion_sound = mixer.Sound("../content/explosion.wav")
            explosion_sound.play()
            bulletState = False
            enemyX[e] = random.randint(0,800)
            enemyY[e] = random.randint(0,150)
            score += 1

        enemy(enemyX[e],enemyY[e], e)

    player(playerX,playerY)
    
    if bulletState and bulletY > 0:
        bulletY -= bulletY_change
        bullet(bulletX, bulletY)
    else:
        bulletState = False

    show_score(textX,textY)

    pygame.display.update()# Display -> update
