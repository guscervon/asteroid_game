from constants import *
from player import Player
import pygame

def main():

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatetables = pygame.sprite.Group()
    drawtables = pygame.sprite.Group()
    Player.containers = (updatetables, drawtables)
    
    player = Player(x, y)


    dt = 0
    background_color = (0,0,0) # RGB sequence for black

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for update_item in updatetables:
            update_item.update(dt)

        screen.fill(color=background_color)
        for draw_item in drawtables:
            draw_item.draw(screen)

        pygame.display.flip() # Refresh screen
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
