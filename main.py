# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    



    # Game loop
    while True:  
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     
            
        # Update game state    
        updatable.update(dt)

        # Collision objects
        for asteroid in asteroids: 
            if player.collision(asteroid):
                 print("Game over!")
                 sys.exit()
            for shot in shots:
                 if asteroid.collision(shot):
                      asteroid.split()
                      shot.kill()
        # Draw everything
        screen.fill("black")

        # drawable.draw(screen)
        for sprite in drawable:
             sprite.draw(screen)

        pygame.display.flip()

        # Update dt
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
	main()
