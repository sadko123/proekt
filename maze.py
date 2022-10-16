from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_size, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):

        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y < window_hight - sprite_hight:
            self.rect.y += self.speed
        if key_pressed[K_DOWN] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < window_widht - sprite_widht:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x <= window_widht * 3 / 4:
            self.direction = 'right'
        if self.rect.x >= window_widht - sprite_widht:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed



window_widht = 700
window_hight = 500
sprite_widht = 50
sprite_hight = 50

clock = time.Clock()

FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()



window = display.set_mode((700, 500))

background = image.load('background.jpg')
background = transform.scale(background, (700, 500))
sprite1_image = 'hero.png'
vrag_image = 'cyborg.png'
socrovishe_image =  'treasure.png'
wall_image = 'wall.jpg'

sprite1 = Player(sprite1_image, 50, 50, (sprite_widht, sprite_hight), 10)
vrag = Enemy(vrag_image, 600, 200, (sprite_widht, sprite_hight), 5)
socrovishe = GameSprite(socrovishe_image , 600, 400, (sprite_widht, sprite_hight), 0)

wall_one = GameSprite(wall_image, 300, 10, (10, 250), 0)
wall_two = GameSprite(wall_image, 550, 350, (10, 250), 0)

run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    if not finish:
    sprite1.update()
    vrag.update()

    window.blit(background, (0,0))
    sprite1.reset()
    vrag.reset()
    socrovishe.reset()

    wall_one.reset()
    wall_two.reset()

    display.update()
    clock.tick(FPS)
   