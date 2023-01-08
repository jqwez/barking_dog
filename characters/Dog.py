import pygame.sprite, pygame.image
import random

class Dog(pygame.sprite.Sprite):    
    dog_path = "../assets/dog/"
    dog_images = [
        "idle",
        "idle_tongue",
        "idle_duck",
        "idle_duck_closed",
        "left",
        "left2",
        "right",
        "right2"
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.states = []
        
        for i in range(len(self.dog_images)):
            self.states.append(pygame.image.load(f'./assets/dog/{self.dog_images[i]}.png'))

        self.rect = self.states[0].get_rect()
        self.image = self.states[0]

    def set_visual_state(self, arg):
        if type(arg) == type('string'):
            self.image = self.states[self.dog_images.index(arg)]
        if type(arg) == type(2):
            self.image = self.states[arg]

    def set_down(self):
        self.animate("idle_duck")

    def set_up(self):
        self.animate("idle")

    def set_idle(self):
        self.animate("idle")

    def set_left(self):
        self.animate("left", "left", "left", "left", "left2","left2")

    def set_right(self):
        self.animate("right", "right", "right", "right", "right2", "right2")

    def animate(self, *args):
        self.set_visual_state(random.choice(args))
    