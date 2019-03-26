import pygame
from constants import *
from settings import enemy_image
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        surface = pygame.image.load(enemy_image).convert_alpha()
        scale_coefficient = ENEMY_WIDTH / surface.get_rect().width
        scaled_surface = pygame.transform.rotozoom(surface, 180, scale_coefficient)
        self.image = pygame.transform.rotate(scaled_surface, 180)
        self.rect = self.image.get_rect()
        border_gap = self.rect.width/2
        x = randint(0 + border_gap, WIDTH + border_gap)  
        self.rect.midbottom = (x, 0)

        self.direction = 1 # to Right
        self.speedx = 3
        self.speedy = 4
        self.traverse_limit = 0
        self.set_traverse_limit()
    
    def set_traverse_limit(self):
        self.direction *= -1
        distance = randint(ENEMY_TRAVERSE_MIN, ENEMY_TRAVERSE_MAX)
        if (self.rect.x <= distance):
            self.direction = 1
        if (self.rect.x >= WIDTH - distance):
            self.direction = -1
        self.traverse_limit = self.rect.x + self.direction * distance
    
    def update(self):
        self.rect.y += self.speedy

        self.rect.x += self.direction * self.speedx
        if (self.direction == 1):
            if (self.rect.x >= self.traverse_limit):
                self.set_traverse_limit()
        else:
            if(self.rect.x <= self.traverse_limit):
                self.set_traverse_limit()