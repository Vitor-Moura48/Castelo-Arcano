from Configurações.config import *
from Configurações import Variaveis_globais

# aplica o efeito de buff e começa a contar o tempo para parar o efeito (aumenta a velocidade do player)
def conferir_buffs():

    if Variaveis_globais.tempo_buff_velocidade > 0:

        Variaveis_globais.velocidade_player = 525 / fps
        Variaveis_globais.tempo_buff_velocidade -= 0.2

    else:
         Variaveis_globais.velocidade_player = 350 / fps