from Configurações.config import *

class Joystick:  # criar classe para resolver coisas sobre controle
    def __init__(self):

        # verificar se há joysticks
        quantidade_joysticks = pygame.joystick.get_count()

        if quantidade_joysticks > 0:
            self.controle = pygame.joystick.Joystick(0)
            self.controle.init()

    def movimento(self, event):
        global eixo_joystick, eixo_x_joystick, eixo_y_joystick

        eixo_joystick = event.axis

        if eixo_joystick == 0:
            eixo_x_joystick = event.value

        if eixo_joystick == 1:
            eixo_y_joystick = event.value


# criar objetos
controle = Joystick()

