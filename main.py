# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    local_player = Player(x, y)
    asteroid_field = AsteroidField()

    while(True) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        for object in drawable:
            object.draw(screen)
        
        for object in updatable:
            object.update(dt);
        
        for asteroid in asteroids:
            if asteroid.detect_collision(local_player):
                sys.exit("Game over!")
        
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed / 1000

if __name__ == "__main__":
    main()