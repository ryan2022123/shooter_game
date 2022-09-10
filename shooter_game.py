#Create your own shooter
from pygame import *
from random import randint

window = display.set_mode((700,500))
display.set_caption("Shooter")

background = transform.scale(image.load("galaxy.jpg"), (700,500))
rocket = transform.scale(image.load("rocket.png"), (75, 75))
enemy = transform.scale(image.load("ufo.png"), (75, 75))

game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, width, height, picture, xcor, ycor, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(picture), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocket(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - self.height:
            self.rect.y += self.speed
    
    def shoot(self):
        bullet = Bullet(50 , 50, "bullet.png", self.rect.centerx, self.rect.top, 2)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global miss
        if self.rect.y > 500:
            self.rect.y = randint(-10, -1)
            self.rect.x = randint(0, 600)
            miss += 1
        #if self.rect.y 
enemies = sprite.Group()
for i in range(2):
    enemy = Enemy(75, 75, "ufo.png", 250, 0, 1)
    enemies.add(enemy)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
bullets = sprite.Group()

score = 0
miss = 0
font.init()
font1 = font.Font(None, 40)
score_txt = font1.render(f"Score: {score}", True, (255, 255, 255))
missed = font1.render(f"Missed: {miss}", True, (255, 255, 255))
win = font1.render("You win!", True, (0, 255,0))
lose = font1.render("You lose! PRESS X TO CLOSE", True, (255, 0, 0))


rocket = Rocket(75, 75, "rocket.png", 50, 50, 2)
clock = time.Clock()   
fps = 55

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.shoot()
        if e.type == KEYDOWN:
            if e.key == K_x:
                game = False
    if not finish:

        window.blit(background, (0, 0))
        window.blit(score_txt, (150, 30))
        missed = font1.render(f"Missed: {miss}", True, (255, 255, 255))
        window.blit(missed, (150, 50))
        
        enemies.draw(window)

        enemies.update()

        bullets.draw(window)

        bullets.update()

        rocket.draw()
        rocket.update()

        if sprite.spritecollide(rocket, enemies, True):
            window.blit(lose, (300, 300))
            finish = True
        collisions = sprite.groupcollide(enemies, bullets, True, True)
        for i in collisions:
            enemy = Enemy(75, 75, "ufo.png", randint(0, 600), 0, 1)
            enemies.add(enemy)
            score += 1
            score_txt = font1.render(f"Score: {score}", True, (255, 255, 255))
        if score >= 15:
            window.blit(win, (300, 300))
            finish = True
    display.update()
clock.tick(fps)







        
    