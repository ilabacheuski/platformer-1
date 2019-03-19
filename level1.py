import pygame
from constants import *
from settings import level1_image

class Level1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        surface = pygame.image.load(level1_image).convert()
        scale_coefficient = WIDTH / surface.get_rect().width
        raw_surface = pygame.transform.rotozoom(surface, 0, scale_coefficient)
        count = 10
        surface_height = raw_surface.get_rect().height
        self.image = pygame.Surface((WIDTH, surface_height * count))
        for i in range(count):
            self.image.blit(raw_surface, (0, surface_height * i))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH / 2, HEIGHT)