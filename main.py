from constants import *
import pygame

def main():

    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    background_color = (0,0,0) # RGB sequence for black

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                return
            screen.fill(color=background_color)
            pygame.display.flip() # Refresh screen
        


if __name__ == "__main__":
    main()
