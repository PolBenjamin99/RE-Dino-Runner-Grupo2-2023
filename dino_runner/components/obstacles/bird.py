from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    BIRD_POS_Y = 250
    
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = self.BIRD_POS_Y
        self.fly_index = 0


        
    

       