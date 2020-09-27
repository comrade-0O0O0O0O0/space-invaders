import pygame
import random
import math

#initialize the pygame
pygame.init()

#createm a screen
screen = pygame.display.set_mode((800,800))

#Title and Icon
pygame.display.set_caption("Space Invaders")

#background
BgImg = pygame.image.load("bg.jpg")

#score
score_value=0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: "+ str(score_value), True,(255,255,255))
    screen.blit(score, (x, y))


# Game over function
game_over = pygame.font.Font('freesansbold.ttf', 200)

def game_over_text():
    over_text = font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(350,400))

#Player
playerImg = pygame.image.load("spaceship.png")
playerX = 100
playerY = 680
dx=0
def player(x,y):
    screen.blit(playerImg, (x, y))

#multiple enemies
enenmyImg = []
enemyX = []
enemyY = []
edx=[]
edy=[]
number_of_enemies = 8


for i in range(number_of_enemies):
    enenmyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(64,736))
    enemyY.append(random.randint(50,150))
    edx.append(0.5)
    edy.append(0.25)

#bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 680
bdx=0
bdy=10
bullet_state = "ready"


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletImg,(x+16,y+10))

def enemy(x,y,i):
    screen.blit(enenmyImg[i],(x,y))

def collision(X,Y,x,y):
    distance = math.sqrt((math.pow(X-x,2))+(math.pow(Y-y,2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #this block controls the movement mechanism
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                dx=-4
            if event.key == pygame.K_d:
                dx=4
            if event.key == pygame.K_SPACE:
                 bulletX = playerX
                 fire_bullet(bulletX,bulletY)

        if event.type==pygame.KEYUP:
            dx=0

    
    screen.fill((0,0,50))
    screen.blit(BgImg,(0,0))    
    playerX+=dx

    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    player(playerX,playerY)

    #enemy movement
    for i in range(number_of_enemies):
        if enemyY[i] > 650:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        #Collison mechanism
        if enemyX[i]<=0 or enemyX[i]>=736:
            edx[i] *=-1
        collided = collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collided:
            score_value+=1
            bullet_state="ready"
            bulletY=680
            enemyX[i] = random.randint(0,730)
            enemyY[i] = random.randint(50,150)

        enemyX[i]+=edx[i]
        enemyY[i]+=edy[i]
        enemy(enemyX[i],enemyY[i],i)
    
    #bullet movement 
    if bulletY <=0:
        bulletY=680
        bullet_state = "ready"
    if bullet_state is "fired":
        fire_bullet(bulletX,bulletY)
        bulletY-=bdy



    show_score(textX,textY)    

    

    
    pygame.display.update()
