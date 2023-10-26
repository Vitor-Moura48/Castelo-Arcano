from Configurações.config import *
from Configurações import Variaveis_globais
from mobs import Player

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
            eixo_x_joystick = event.value

        if eixo_joystick == 1:
            eixo_y_joystick = event.value


def conferir_teclado():
    # para mover player ao pressionar tecla, ou joystick
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT] or Variaveis_globais.eixo_x_joystick >= 0.4:
        Player.player.rect.x -= Variaveis_globais.velocidade_player
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT] or Variaveis_globais.eixo_x_joystick >= 0.4:
        Player.player.rect.x += Variaveis_globais.velocidade_player
    
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP] or Variaveis_globais.eixo_y_joystick >= 0.4:
        Player.player.rect.y -= Variaveis_globais.velocidade_player
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN] or Variaveis_globais.eixo_y_joystick >= 0.4:
        Player.player.rect.y += Variaveis_globais.velocidade_player
    

# criar objetos
controle = Joystick()

