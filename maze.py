from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (sprite_widht, sprite_hight))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y

        self.speed = sprite_speed

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
sprite1 = transform.scale(image.load('hero.png'), (80,80))
vrag = transform.scale(image.load('cyborg.png'), (80,80))
socrovishe =  transform.scale(image.load('treasure.png'), (80,80))




run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    
    window.blit(background, (0,0))
    window.blit(sprite1, (100, 100))
    window.blit(vrag, (500,200))
    window.blit(socrovishe, (500, 400))
    display.update()
    clock.tick(FPS)
   