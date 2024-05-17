from Configurações.config import *
from Configurações import Global
from Objetos import Mobs

class Controle:  # criar classe para resolver coisas sobre controle
    def __init__(self):

        self.eixo_x = 0
        self.eixo_y = 0

        self.iniciar_joy()
    
    def iniciar_joy(self):
        
        quantidade_joysticks = pygame.joystick.get_count() # verificar se há joysticks
        if quantidade_joysticks > 0:
            self.controle = pygame.joystick.Joystick(0)
            self.controle.init()
    
    def conferir_joystik(self, event):
        eixo_joystick = event.axis
        if eixo_joystick == 0:
            self.eixo_x = event.value
        if eixo_joystick == 1:
            self.eixo_y = event.value
    
    def mover(self):
        # para mover player ao pressionar tecla, ou joystick
        if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT] or self.eixo_x <= -0.4:
            Mobs.player.rect.x -= Global.velocidade_player
        if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT] or self.eixo_x >= 0.4:
            Mobs.player.rect.x += Global.velocidade_player
        
        if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP] or self.eixo_y <= -0.4:
            Mobs.player.rect.y -= Global.velocidade_player
        if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN] or self.eixo_y >= 0.4:
            Mobs.player.rect.y += Global.velocidade_player

controle = Controle()