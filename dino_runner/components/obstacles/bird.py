from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    BIRD_POS_Y = 250 
    #BIRD_POS_VAR = [200, 250, 300]
    #ELEMENT_POS = random.randint(0,2)
    # BIDR_POS_Y =  BIRD_POS_VAR[ELEMENT_POS]
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = self.BIRD_POS_Y
        self.fly_index = 0

#agregar 2 alturas mas a la lista de BIRD_POS_Y
#hacer que un seleccionador random eliga uno de esos tres valores para que el pajaro aparezca en 3 alturas diferentes

        
    

       