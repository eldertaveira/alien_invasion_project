import pygame

class Ship():
    """Inicializa a espaçonave e define sua posição inicial"""
    def __init__(self, ai_settings,screen):
        """inicializa a espaçosave e define sua posição inicial"""
        self.screen = screen
        self.ai_settings = ai_settings
        #carrega a imagem da espaçosave e obtem seu rect
        self.image = pygame.image.load('imagens/ship.bmp')
        # Redimensiona a imagem para a largura e altura especificadas
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #inicia cada espaçosave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Armazena um valor decimal para o centro da espaçosave
        self.center = float(self.rect.centerx)
        #Flags de movimento
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """atualiza a posição da espaçosave de acordo com a flag de movimento"""
        # Atualiza o valor do centro da espaçosave, e não o retângulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center
    def blitme(self):
        """desenha a espaçosave em sua posição"""
        self.screen.blit(self.image, self.rect)