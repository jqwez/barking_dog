import pygame.sprite
import random



        

class SingleGrass(pygame.sprite.Sprite):
    grass_path = "../assets/bg/"
    tile_types = [
        "grass_block",
        "grass_block2",
        "grass_block_90",
        "grass_block2_90"
        ]



    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(random.choice([f'./assets/bg/{tile}.png' for tile in self.tile_types]))
        self.rect = self.image.get_rect()

class Grass(pygame.sprite.Sprite):
    tiles = []
    single_grass = SingleGrass()
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width + self.single_grass.rect.width
        self.height = height + self.single_grass.rect.height
        
        self.createField()

    def createField(self):
        for i in range(self.width%self.single_grass.rect.width):
            for j in range(self.height%self.single_grass.rect.height):
                grass_tile = SingleGrass()
                grass_tile.rect.x = grass_tile.rect.width*i
                grass_tile.rect.y = grass_tile.rect.height*j
                self.tiles.append(grass_tile)
    
    def drawField(self):
        for tile in self.tiles:
            self.screen.blit(tile.image, tile.rect)
