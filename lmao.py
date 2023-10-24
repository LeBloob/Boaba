from pygame import *
win_height = 700
win_width = 500
window = display.set_mode ((win_height, win_width))
display.set_caption('Maze Game')
bgColor = (108, 210, 216)
class GameSprite(sprite.Sprite):
    def __init__ (self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Bullets(GameSprite):
    def __init__ (self, picture, w, h, x, y, speed):
        super().__init__ (picture, w, h, x, y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 700:
            self.kill()
class Enemy(GameSprite):
    def __init__ (self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
        self.direction = 'left'
    def update(self):
        if self.rect.x <= 465:
            self.direction = 'right'
        elif self.rect.x >= 650:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

            

        
            

class Player(GameSprite):
    def __init__ (self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullets('bullet.png', self.rect.right, self.rect.centery, 15, 20, 15 )
        bullets.add(bullet)

wall_1 = GameSprite('wall.png', 80, 180, 400, 250)
wall_2 = GameSprite('wall.png', 80, 180, 400, 100)
wall_3 = GameSprite('wall_v.png', 400, 50, 110, 235)
player = GameSprite('hero.png', 80, 80, 5, 400)
player = Player('hero.png', 80,80,80,80,0,0)
enemy = Enemy('enemy.png', 80, 80, 600, 200, 2)
final = GameSprite('final.png', 70, 70, 600, 400)
finish = False
run = True
enemies = sprite.Group()
enemies.add(enemy)
bullets = sprite.Group()
barriers = sprite.Group()
barriers.add(wall_1)
barriers.add(wall_2)
barriers.add(wall_3)
while run:
    time.delay (50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_a:
                player.x_speed = -5
            elif e.key == K_d:
                player.x_speed = 5
            elif e.key == K_w:
                player.y_speed = -5
            elif e.key == K_s:
                player.y_speed = 5
            elif e.key == K_SPACE:
                player.fire()
        elif e.type == KEYUP:
            if e.key == K_a or e.key == K_d:
                player.x_speed = 0
            elif e.key == K_w or e.key == K_s:
                player.y_speed = 0
    if finish != True:
        window.fill(bgColor)
        barriers.draw(window)
        player.reset()
        player.update()
        final.reset()
        enemies.update()
        enemies.draw(window)
        bullets.update()
        bullets.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)
        sprite.groupcollide(enemies, bullets, True, False)
        if sprite.collide_rect(player, final):
            finish = True
            img = image.load('thumb.jpg')
            window.fill((255,255,255))
            window.blit(transform.scale(img, (win_width, win_height)),(0,0))    
        if sprite.collide_rect(player, enemy):
            finish = True
            img = image.load('jhon.jpg')
            window.fill((255,255,255))
            window.blit(transform.scale(img, (win_width, win_height)),(0,0))
        display.update()
        
        
            
  
        
    