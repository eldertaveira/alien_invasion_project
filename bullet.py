import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Uma classe que administra as balas disparadas pela espaçosave"""

    def __init__(self, ai_settings, screen, ship):
        """Cria uma bala na posição atual da espaçosave"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Cria um retângulo para a bala em (0, 0) e, em seguida, define a
        # posição correta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena a posição da bala como um valor decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move a bala para cima na tela"""
        # Atualiza a posição decimal da bala
        self.y -= self.speed_factor
        # Atualiza a posição do retângulo
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha a bala na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)