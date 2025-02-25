import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        plus_velocity = self.velocity.rotate(angle) * 1.2
        minus_velosity = self.velocity.rotate(-angle) * 1.2
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = plus_velocity
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = minus_velosity
        
            



        
    
