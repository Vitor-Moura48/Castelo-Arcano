from Configurações.config import *
from Configurações import Global
from Objetos import Mobs

class Joystick:  # criar classe para resolver coisas sobre controle
    def __init__(self):

        # verificar se há joysticks
        quantidade_joysticks = pygame.joystick.get_count()

        if quantidade_joysticks > 0:
            self.controle = pygame.joystick.Joystick(0)
            self.controle.init()

    def movimento(self, event):

            eixo_joystick = event.axis

            if eixo_joystick == 0:
                Global.eixo_x_joystick = event.value

            if eixo_joystick == 1:
                Global.eixo_y_joystick = event.value

def conferir_teclado():
    
    # para mover player ao pressionar tecla, ou joystick
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT] or Global.eixo_x_joystick <= -0.4:
        Mobs.player.rect.x -= Global.velocidade_player
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT] or Global.eixo_x_joystick >= 0.4:
        Mobs.player.rect.x += Global.velocidade_player
    
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP] or Global.eixo_y_joystick <= -0.4:
        Mobs.player.rect.y -= Global.velocidade_player
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN] or Global.eixo_y_joystick >= 0.4:
        Mobs.player.rect.y += Global.velocidade_player
    

# criar objetos
controle = Joystick()

