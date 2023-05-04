import random
from dino_runner.utils.constants import CLOUD,SCREEN_WIDTH

class Cloud():
    def __init__(self):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.choice([100, 120, 150, 170])
    
    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x == 0:
            self.rect.x = SCREEN_WIDTH
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
