from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH,BIRD

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        
        if self.image == BIRD:  
            self.fly_index += 1
            if self.fly_index < 5:
                self.type = 0
            elif self.fly_index < 10:
                self.type = 1
            if self.fly_index >= 10:  
                self.fly_index = 0

        if self.rect.x < -SCREEN_WIDTH:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)
        