
import sys
import pygame

def run_game():
    # Initialize pygame and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    #Define a cor de fundo
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redesenha a tela a cada passagem pelo loop
        screen.fill(bg_color)
        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()