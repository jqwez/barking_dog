import pygame

class TitleBar(pygame.sprite.Sprite):

    color = (30,37,37)
    grey = (211, 211, 211)
    red = (255, 0, 0)
    
    

    def __init__(self, screen, height=25, icon='', rect=''):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.height = height
        self.title = pygame.Rect(0, 0, self.screen.get_width(), self.height)
        self.xColor = self.grey
        self.xHover = False
        self.icon = icon
        self.icon_rect = rect
        self.setIcon()
        

    def drawTitle(self):
        pygame.draw.rect(self.screen, self.color, self.title)
        self.hoverX()
        self.drawX()
        self.drawIcon()
        self.drawCaption()

    def setIcon(self):
        self.icon = pygame.image.load(f'./assets/dog/idle.png').convert_alpha()
        self.icon = pygame.transform.scale(self.icon, (20,20))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.y = 3
        self.icon_rect.x = 8

    def drawIcon(self):
        self.screen.blit(self.icon, self.icon_rect)

    def get_height(self):
        return self.height

    def drawCaption(self):
        font = pygame.font.SysFont(None, 24)
        img = font.render('Ultimate Barking Dog', True, self.grey)
        rect = pygame.Rect(self.screen.get_width()/2-img.get_width()/2, self.height/2-6, 24, 24)
        self.screen.blit(img, rect)

    def drawX(self):
        font = pygame.font.SysFont(None, 24)
        img = font.render('X', True, self.xColor)
        rect = pygame.Rect(self.screen.get_width()-30, self.height/2-6, 24, 24)
        self.screen.blit(img, rect)

    def hoverX(self):
        if self.xHover == True:
            self.xColor = self.animateColorFrame(self.xColor, self.red)
        else:
            self.xColor = self.animateColorFrame(self.xColor, self.grey)

    def animateColorFrame(self, currentColor, targetColor):
        a, b, c = currentColor[0], currentColor[1], currentColor[2] 
        x, y, z = targetColor[0], targetColor[1], targetColor[2]

        
        def changeValue(a, b):
            if a > b and a-b >100:
                return a-10
            if a > b and a-b >30:
                return a-6
            if a > b:
                return a-1
            if a < b and b-a>100:
                return a+10
            if a < b and b-a>30:
                return a+6
            if a < b:
                return a+1
            else: return a

        return tuple(map(changeValue, [a,b,c],[x,y,z]))

