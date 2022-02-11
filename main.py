import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space killer")


# main player
playerImg = pygame.image.load('space_invader/ufo.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 5

for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('space_invader/shredder.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50,100))
    enemyX_change.append(0.5)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# bullet for shooting
bulletImg = pygame.image.load('space_invader/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.7
bullet_state = "ready"


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


# collision check
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) +
                         (math.pow(bulletY-enemyY, 2)))
    if distance < 20:
        return True
    else:
        return False


#score
score_value = 0
font1 = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

def showScore(x,y):
    score = font1.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


# bullet over function
bullet_count = 0
font2 = pygame.font.Font('freesansbold.ttf',32)
bullet_valueX = 540
bullet_valueY = 10


def show_Bullet(x,y):
    bullet_score = font2.render("Bullet used : " + str(bullet_count),True,(255,255,255))
    screen.blit(bullet_score,(x,y))

#Game over
over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))


# Game loop
run = True

while run:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_count+=1
                    bulletX = playerX
                    bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # enemy
    for i in range(no_of_enemies):

        #Game over code
        if enemyY[i] >=470:
            for j in range(no_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] += 0.2
            enemyY[i] += enemyY_change[i]
    
    
    
        Collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if Collision:
            score_value+=1
            bulletY = 480
            bullet_state="ready"
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50,100)

        enemy(enemyX[i], enemyY[i], i)

    # bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # PLAYER
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
     
    
    player(playerX, playerY)

    showScore(textX,textY)
    
    show_Bullet(bullet_valueX,bullet_valueY)

    pygame.display.update()
