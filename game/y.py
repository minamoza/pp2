import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))

done = False
backgroundImage = pygame.image.load("background.jpg")
playerImage = pygame.image.load("player.png")
player_x = 200
player_y = 500

enemyImage = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 536)
enemy_y = random.randint(20, 50)

enemy_dx = 5
enemy_dy = 30

bulletImage=pygame.image.load("bullet.png")
bullet_y=480
bullet_x=217
bullet_dy = 30

hit=False
press=False
a=0

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def Bullet(x,y):
    screen.blit(bulletImage,(x,y))


while not done:
    for event in pygame.event.get():
        # event on quit
        if event.type == pygame.QUIT: # event.type == pygame.KEYDOWN
            done = True

    if bullet_y==0:
        a=0
        bullet_y=480
        press=False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: player_x -= 5
    if pressed[pygame.K_RIGHT]: player_x += 5

    enemy_x += enemy_dx
    if enemy_x < 0 or enemy_x > 536:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy
    
    if pressed[pygame.K_SPACE]:
        bullet_x=player_x+17
        press=True
        a=bullet_y

    if a>0 and a<570:
        bullet_y -= bullet_dy

    if enemy_y<=bullet_x<=enemy_x+64 and bullet_y<=enemy_y+64: hit=True

    screen.blit(backgroundImage, (0, 0))
    player(player_x, player_y)
    if hit==False: enemy(enemy_x,enemy_y)
    
    if press==True:
        Bullet(bullet_x,bullet_y)
    else:
        Bullet(player_x+17,bullet_y)
    
    pygame.display.flip()