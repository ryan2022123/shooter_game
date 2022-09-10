#create a Maze game!
from pygame import *

window = display.set_mode((700,500))
display.set_caption("Maze")

background = transform.scale(image.load("background.jpg"), (700,500))
hero = transform.scale(image.load("hero.png"), (60, 60))
cyborg = transform.scale(image.load("cyborg.png"), (98, 100))
treasure = transform.scale(image.load("treasure.png"), (104, 75))


game = True
finished = True


# hero_x = 100
# hero_y = 100

class GameSprite(sprite.Sprite):
    def __init__(self, width, height, picture, xcor, ycor, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.picture = transform.scale(image.load(picture), (width, height))
        self.rect = self.picture.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
        self.speed = speed
        self.og_x = xcor
        self.og_y = ycor
    def update(self):
        window.blit(self.picture, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def move(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            # print(self.xcor)
            # print(self.ycor)
        if keys[K_RIGHT] and self.rect.x < 700 - self.width:
            self.rect.x += self.speed
            # print(self.xcor)
            # print(self.ycor)
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            # print(self.xcor)
            # print(self.ycor)
        if keys[K_DOWN] and self.rect.y < 500 - self.height:
            self.rect.y += self.speed
            # print(self.xcor)
            # print(self.ycor)

class Enemy(GameSprite):
    def move_auto(self):

        if self.rect.x >= self.og_x - 100:
            self.flag = "left"
            
        if self.rect.x <= self.og_x - 200:
            self.flag = "right"
        
        if self.flag == "left":
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, width, height, xcor, ycor, color):
        super().__init__()
        self.image = Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Treasure(sprite.Sprite):
    def __init__(self, width, height, xcor, ycor, picture):
        super().__init__()
        self.width = width
        self.height = height
        self.picture = transform.scale(image.load(picture), (width, height))
        self.rect = self.picture.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
    def update(self):
        window.blit(self.picture, (self.rect.x, self.rect.y))
hero = Hero(50, 50, "hero.png", 0, 0, 2)
cyborg = Enemy(50, 50, "cyborg.png", 205, 150, 1)
cyborg2 = Enemy(50, 50, "cyborg.png", 500, 150, 1)
treasure = Treasure(50, 50, 650, 450, "treasure.png")


wall1 = Wall(10, 250, 100, 100, (50, 75, 150))
wall2 = Wall(10, 350, 100, 450, (50, 75, 150))
wall3 = Wall(10, 300, 200, 150, (50, 75, 150))
wall4 = Wall(10, 50, 200, 50, (50, 75, 150))
wall5 = Wall(10, 100, 300, 400, (50, 75, 150))
wall6 = Wall(10, 75, 300, 0, (50, 75, 150))
wall7 = Wall(10, 175, 300, 150, (50, 75, 150))
wall8 = Wall(10, 150, 400, 150, (50, 75, 150))
wall9 = Wall(10, 100, 400, 250, (50, 75, 150))
wall10 = Wall(10, 50, 400, 450, (50, 75, 150))
wall11 = Wall(10, 350, 600, 150, (50, 75, 150))
wall12 = Wall(10, 440, 500, 0, (50, 75, 150))
wall_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12]
wall_group = sprite.Group()
for wall in wall_list:
    wall_group.add(wall)

enemy_list = [cyborg, cyborg2]
enemy_group = sprite.Group()
for enemy in enemy_list:
    enemy_group.add(enemy)
treasure_list = [treasure]
treasure_group = sprite.Group()
for trs in treasure_list:
    treasure_group.add(trs)




treasure1 = Treasure(50, 50, 650, 450, "treasure.png")




clock = time.Clock()
fps = 120

font.init()
font1 = font.Font(None, 70)
win = font1.render("You win!", True, (0, 255,0))
lose = font1.render("You lose!", False, (255, 0, 0))
welcome = font1.render("Welcome To The Maze Game", True, (255, 255, 255))
enter = font1.render("Click SPACE To Continue", True, (255, 255, 255))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

money = mixer.Sound("money.ogg")

kick = mixer.Sound("kick.ogg")


while game:
    window.blit(welcome, (0, 100))
    window.blit(enter, (50, 225))
    for e in event.get(): 
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                finished = False
                
        if e.type == KEYDOWN:
            if e.key == K_x:
                game = False

        if e.type == QUIT:
            game = False
    if finished == False:
    
        
        window.blit(background, (0,0))

        hero.update()

        cyborg.update()

        cyborg2.update()

        cyborg2.move_auto()

        cyborg.move_auto()

        treasure1.update()

        wall_group.draw(window)

        hero.move()

        

        if sprite.spritecollide(hero, wall_group, False):
            finished = True
            window.blit(background, (0,0))
            window.blit(lose,(300,200))

        if sprite.spritecollide(hero, enemy_group, False):
            finished = True
            window.blit(background, (0,0))
            window.blit(lose,(300,200))

        if sprite.spritecollide(hero, treasure_group, False):
            finished = True
            window.blit(background, (0,0))
            window.blit(win,(300,200))

        

   
    display.update()
    clock.tick(fps)


