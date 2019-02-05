import pygame
from constants import *
from settings import player_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        surface = pygame.image.load(player_image).convert()
        scaled_surface = pygame.transform.scale(surface,(70,70))
        self.image = pygame.transform.rotate(scaled_surface, 180)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        pass
        # y1 = 228 x1 = 58
        # y2 = 671 x2 = 434