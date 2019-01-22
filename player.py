import pygame
from constants import *
from settings import path_to_player

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load(path_to_player).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        pass
        