import pygame
from dino_runner.utils.constants import HAMMER,SCREEN_WIDTH
from pygame.sprite import Sprite

class DinoHammer(Sprite):
    def __init__(self):
        self.image = HAMMER
        self.hammer_rect = self.image.get_rect()
        self.hammer_rect.x = 95
        self.hammer_rect.y = 335
        self.hammer_enable = False

    def update(self, game_speed):
        if self.hammer_enable:
            self.hammer_rect.x += game_speed
            if self.hammer_rect.x > SCREEN_WIDTH:
                self.hammer_rect.x = 95
                self.hammer_enable = False
  
    
    def draw(self,screen):
        if self.hammer_enable:
            screen.blit(self.image, self.hammer_rect)


