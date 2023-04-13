import pygame
from random import choice, randrange
pygame.init()
Width, Height=1280, 720
RES=(Width, Height)

FONT_SIZE=15
alpha_value=randrange(30, 40, 5)

chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','と','う','き','ょ','う', 'A','B','C',
       'D', 'E', 'F','G','H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','w', 'X', 'Y', 'Z']

font=pygame.font.Font('font/Rajdhani-Light.ttf', FONT_SIZE)
font_2=pygame.font.Font('font/Rajdhani-Light.ttf', FONT_SIZE-FONT_SIZE//6)
font_3=pygame.font.Font('font/Rajdhani-Light.ttf', FONT_SIZE-FONT_SIZE//3)

green_chars=[font.render(char, True, (randrange(0, 100), 255, randrange(0, 100))) for char in chars]
green_chars_2=[font_2.render(char, True, (40, randrange(100, 175), 40)) for char in chars]
green_chars_3=[font_3.render(char, True, (40, randrange(50, 100), 40)) for char in chars]

screen=pygame.display.set_mode(RES)
display_surface=pygame.Surface(RES)
display_surface.set_alpha(alpha_value)

clock=pygame.time.Clock()

class Symbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 40
        self.value = choice(green_chars)

    def draw(self):
        self.value = choice(green_chars)
        self.y = self.y + self.speed if self.y < Height else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value, (self.x, self.y))

    def draw_2(self):
        self.value_2 = choice(green_chars_2)
        self.y = self.y + self.speed if self.y < Height else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value_2, (self.x, self.y))

    def draw_3(self):
        self.value_3 = choice(green_chars_3)
        self.y = self.y + self.speed if self.y < Height else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value_3, (self.x, self.y))

symbols=[Symbol(x, randrange(-Height, 0)) for x in range(0, Width, FONT_SIZE * 3)]
symbols_2=[Symbol(x, randrange(-Height, 0)) for x in range(FONT_SIZE, Width, FONT_SIZE * 3)]
symbols_3=[Symbol(x, randrange(-Height, 0)) for x in range(FONT_SIZE * 2, Width, FONT_SIZE * 3)]

run=True
while run:

    screen.blit(display_surface, (0, 0))
    display_surface.fill(pygame.Color('black'))

    [symbol.draw() for symbol in symbols]
    [symbol_2.draw_2() for symbol_2 in symbols_2]
    [symbol_3.draw_3() for symbol_3 in symbols_3]

    pygame.time.delay(140)
    pygame.display.update()
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False