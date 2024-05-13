import pygame
import sys

def check_events():
    """Responde aos eventos de teclado e mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    # Redesenha a tela a cada passagem pelo loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Deixa a tela mais recente visível
    pygame.display.flip()
