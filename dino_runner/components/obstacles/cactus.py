import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS

class Cactus(Obstacle):
    LARGE_CACTUS_POS = 300
    SMALL_CACTUS_POS = 325
    
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        if self.image == LARGE_CACTUS:
            self.rect.y = self.LARGE_CACTUS_POS
        else:   
            self.rect.y = self.SMALL_CACTUS_POS
        