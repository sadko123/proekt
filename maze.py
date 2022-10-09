from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (sprite_widht, sprite_hight))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):

        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y < (window_hight - sprite_hight):
            self.rect.y += self.speed
        if key_pressed[K_DOWN] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < (window_widht - sprite_widht):
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed


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

sprite1 = Player(sprite1_image, 50, 50, 10)
vrag = GameSprite(vrag_image, 600, 200, 5)
socrovishe = GameSprite(socrovishe_image , 600, 400, 0)

run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    
    sprite1.update()


    window.blit(background, (0,0))
    sprite1.reset()
    vrag.reset()
    socrovishe.reset()
    display.update()
    clock.tick(FPS)
   