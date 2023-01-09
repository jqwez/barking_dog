import sys, pygame

from characters.Dog import Dog
from components.TitleBar import TitleBar
from assets.bg.Grass import Grass

pygame.init()

size = width, height = 1080, 720
black = 15, 100, 15

speed = 8

screen = pygame.display.set_mode(size, pygame.NOFRAME)
pygame.display.set_caption("Ultimate Barking Dog")

clock = pygame.time.Clock()

title_bar = TitleBar(screen)
dog = Dog()
grass = Grass(screen, screen.get_width(), screen.get_height())
pygame.display.set_icon(dog.states[0])

alwaysUpdate = pygame.sprite.Group()
alwaysUpdate.add(title_bar)


def Main():
    while True:
        mX, mY = pygame.mouse.get_pos()
        if mX >= screen.get_width()-30 and mY <= title_bar.get_height():
            title_bar.xHover = True
            if pygame.mouse.get_pressed()[0] == True:
                sys.exit()
        else:
            title_bar.xHover = False


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


        
        screen.fill(black)
        grass.drawField()
        screen.blit(dog.image, dog.rect)
        
        
        title_bar.drawTitle()
        pygame.display.flip()

if __name__ == "__main__":
    Main()