import math
import random

import pygame
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('ss-bspline.png')
mixer.music.load("background.wav")
mixer.music.play(-1)
pygame.display.set_caption("fox shooting")
ic = pygame.image.load('21781-free-cartoon-fox-free-download - Copy (1).png')
pygame.display.set_icon(ic)
Img = pygame.image.load('player.png')
pX = 370
pY = 480
pX_change = 0
eImg = []
eX = []
eY = []
eImg1= []
eX_change = []
eY_change = []
num = 6
for i in range(num):
    eImg.append(pygame.image.load('kindpng_4919029 (1).png'))
    eImg.append(pygame.image.load('21781-free-cartoon-fox-free-download - Copy (1).png'))
    eX.append(random.randint(0, 850))
    eY.append(random.randint(50, 150))
    eX_change.append(4)
    eY_change.append(40)
ba = pygame.image.load('pngegg (1).png')
bX = 0
bY = 480
bX_change = 0
bY_change = 10
b_state = "ready"
sco = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

f = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = f.render("Score : " + str(sco), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    screen.blit(Img, (x, y))
def enemy(x, y, i):
    screen.blit(eImg[i], (x, y))
def fire_bullet(x, y):
    global b_state
    b_state = "fire"
    screen.blit(ba, (x + 16, y + 10))
def isCollision(eX, eY, bX, bY):
    distance = math.sqrt(math.pow(eX - bX, 2) + (math.pow(eY - bY, 2)))
    if distance < 27:
        return True
    else:
        return False
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if b_state is "ready":
                    bulletSound = mixer.Sound("bubble-pop-6395.wav")
                    bulletSound.play()
                    bX = pX
                    fire_bullet(bX, bY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    pX += pX_change
    if pX <= 0:
        pX = 0
    elif pX >= 736:
        pX = 736

    for i in range(num):

        if eY[i] > 440:
            for j in range(num):
                eY[j] = 2000
            game_over_text()
            break

        eX[i] += eX_change[i]
        if eX[i] <= 0:
            eX_change[i] = 750
            eY[i] += eY_change[i]
        elif eX[i] >= 736:
            eX_change[i] = -4
            eY[i] += eY_change[i]

        collision = isCollision(eX[i], eY[i], bX, bY)
        if collision:
            Sound = mixer.Sound("bubble-pop-6395.wav")
            Sound.play()
            bY = 480
            bullet_state = "ready"
            sco += 1
            eX[i] = random.randint(0, 736)
            eY[i] = random.randint(50, 150)

        enemy(eX[i], eY[i], i)

    if bY <= 0:
        bY = 480
        b_state = "ready"

    if b_state is "fire":
        fire_bullet(bX, bY)
        bY -= bY_change

    player(pX, pY)
    show_score(textX, testY)
    pygame.display.update()

