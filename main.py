from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame
import sys

def main():

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatetables = pygame.sprite.Group()
    drawtables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatetables, drawtables)
    AsteroidField.containers = updatetables
    asteroidfield = AsteroidField()

    Player.containers = (updatetables, drawtables)
    player = Player(x, y)

    Shot.containers = (shots, updatetables, drawtables)


    dt = 0
    background_color = (0,0,0) # RGB sequence for black

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for update_item in updatetables:
            update_item.update(dt)

        for asteroid_item in asteroids:
            if asteroid_item.check_collision(player):
                sys.exit("Game over!")

            for bullet in shots:
                if asteroid_item.check_collision(bullet):
                    asteroid_item.kill()
                    bullet.kill()

        screen.fill(color=background_color)
        for draw_item in drawtables:
            draw_item.draw(screen)

        pygame.display.flip() # Refresh screen
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
