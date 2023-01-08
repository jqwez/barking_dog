import pygame


class TitleBar:

    color = (30,37,37)
    def __init__(self, screen, height=25):
        self.screen = screen
        self.height = height
        self.title = pygame.Rect(0, 0, self.screen.get_width(), self.height)

    def drawTitle(self):
        pygame.draw.rect(self.screen, self.color, self.title)

    def get_height(self):
        return self.height