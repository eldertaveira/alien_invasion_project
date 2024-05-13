import pygame

class Ship():
    """Inicializa a espaçonave e define sua posição inicial"""
    def __init__(self, screen):
        """inicializa a espaçosave e define sua posição inicial"""
        self.screen = screen
        #carrega a imagem da espaçosave e obtem seu rect
        self.image = pygame.image.load('imagens/ship.bmp')
        # Redimensiona a imagem para a largura e altura especificadas
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #inicia cada espaçosave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Flags de movimento
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """atualiza a posição da espaçosave de acordo com a flag de movimento"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
    def blitme(self):
        """desenha a espaçosave em sua posição"""
        self.screen.blit(self.image, self.rect)