
from Configurações import *

x_player = int(largura_da_tela / 2)
y_player = int(altura_da_tela / 2)

x_inimigo = randint(largura_da_tela, largura_da_tela + 500)
y_inimigo = randint(int(altura_da_tela * 0.14), int(altura_da_tela * 0.84))


barreira = 0
vidas_castelo = 10

velocidade_player = 350 / fps
mudanca_de_velocidade = [False, False, False, False]

perdeu = False
ganhou = False

maior_recorde = []



