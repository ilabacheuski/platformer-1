import pygame
from constants import *
from settings import enemy_image

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        surface = pygame.image.load(enemy_image).convert_alpha()
        scale_coefficient = ENEMY_WIDTH / surface.get_rect().width
        scaled_surface = pygame.transform.rotozoom(surface, 180, scale_coefficient)
        self.image = pygame.transform.rotate(scaled_surface, 180)
        self.rect = self.image.get_rect()
        self.rect.midtop = ( WIDTH / 2 , 20)
        self.speedx = 0
        self.accx = 5