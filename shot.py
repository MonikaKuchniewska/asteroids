from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt