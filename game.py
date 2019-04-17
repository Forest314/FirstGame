import pygame   

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Cubes Game")


walkRight = [pygame.image.load('Sprite/right_1.png'),
pygame.image.load('Sprite/right_2.png'), pygame.image.load('Sprite/right_3.png'),
pygame.image.load('Sprite/right_4.png'), pygame.image.load('Sprite/right_5.png'),
pygame.image.load('Sprite/right_6.png')]

walkLeft = [pygame.image.load('Sprite/left_1.png'),
pygame.image.load('Sprite/left_2.png'), pygame.image.load('Sprite/left_3.png'),
pygame.image.load('Sprite/left_4.png'), pygame.image.load('Sprite/left_5.png'),
pygame.image.load('Sprite/left_6.png')]

playerStand = pygame.image.load('Sprite/idle.png')

bg = pygame.image.load('Sprite/pygame_bg.jpg')

clock = pygame.time.Clock()

x = 50
y = 430
wiegth = 60
height = 71
speed = 5

isJump = False
JumpCount = 10

left = False
right = False
animCount = 0
LastMovie = 'right'

class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)    

def drowWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))    

    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_f]:
        if LastMovie == 'right':
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(snaryad(round(x + wiegth // 2), 
            round(y + height // 2), 5, (255, 0, 0), facing  ))


    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        LastMovie = 'left'
    elif keys[pygame.K_RIGHT] and x < 500 - wiegth - 5:
        x += speed
        left = False
        right = True
        LastMovie = 'right'
    else:
        left = False
        right = False
        animCount = 0

    if not(isJump):    
        if keys[pygame.K_SPACE]:
            isJump = True    
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2    
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else:
            JumpCount = 10
            isJump = False        
    drowWindow()
pygame.quit()