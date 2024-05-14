class Settings():
    """"Uma classe para armazenar todas as configurações da Invasão Alienigena."""
    def __init__(self):
        """Inicia as configurações do jogo."""
        # Configurações da tela
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230, 230, 230)
        # Configurações da espaçosave
        self.ship_speed_factor = 1.5