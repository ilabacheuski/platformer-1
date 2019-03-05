import pygame
from constants import *
from settings import bullet_image
from spritesheet import Spritesheet

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = Spritesheet(bullet_image)
        surface = ss.image_at((13, 10, 478, 112))
        scale_coefficient = BULLET_WIDTH / surface.get_rect().width
        self.image = pygame.transform.rotozoom(surface, 180, scale_coefficient)
        self.rect = self.image.get_rect()
        self.rect.midtop = (WIDTH / 2, HEIGHT / 2)