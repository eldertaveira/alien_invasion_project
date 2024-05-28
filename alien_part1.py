#import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Initialize pygame and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Cria a espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo para armazenar as balas
    bullets = Group()

    # Cria um alien
    alien = Alien(ai_settings, screen)  

    # Inicia o laço principal do jogo
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # Redesenha a tela a cada passagem pelo loop
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()