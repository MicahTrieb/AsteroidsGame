from circleshape import *
class Shots(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,5):

    def draw(self):
        pygame.draw.circle(screen,"white",self.position,self.radius)
    def update(self, dt):
        pass
    def shoot(self):
        
