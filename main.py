import sys, pygame

from characters.Dog import Dog
from components.TitleBar import TitleBar

pygame.init()

size = width, height = 1080, 720
black = 15, 100, 15

speed = 8

screen = pygame.display.set_mode(size, pygame.NOFRAME)
pygame.display.set_caption("Ultimate Barking Dog")

clock = pygame.time.Clock()

title_bar = TitleBar(screen)
dog = Dog()
pygame.display.set_icon(dog.states[0])

while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if dog.rect.left <= screen.get_width() - dog.rect.width:
            dog.set_right()
            dog.rect = dog.rect.move([speed,0])
    if keys[pygame.K_a]:
        if dog.rect.left >= 0:
            dog.set_left()
            dog.rect = dog.rect.move([-speed,0])
    if keys[pygame.K_s]:
        if dog.rect.top <= screen.get_height() - dog.rect.height:
            dog.set_down()
            dog.rect = dog.rect.move([0,speed])
    if keys[pygame.K_w]:
        if dog.rect.top >= title_bar.height:
            dog.set_idle()
            dog.rect = dog.rect.move([0,-speed])

    print(clock.get_fps())

    

    screen.fill(black)
    screen.blit(dog.image, dog.rect)
    
    
    title_bar.drawTitle()
    pygame.display.flip()