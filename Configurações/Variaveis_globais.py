from Configurações.config import *

x_player = int(largura_da_tela / 2)
y_player = int(altura_da_tela / 2)

x_inimigo = randint(largura_da_tela, largura_da_tela + 500)
y_inimigo = randint(int(altura_da_tela * 0.14), int(altura_da_tela * 0.84))


eixo_joystick = 0
eixo_x_joystick = 0
eixo_y_joystick = 0


barreira = 0
vidas_castelo = 10
inimigos_restantes = 0
inimigos_totais = 0

velocidade_player = 350 / fps
velocidade_inimigo = 0
mudanca_de_velocidade = [False, False, False, False]

perdeu = False
ganhou = False

maior_recorde = []

dificuldade = 1


tempo_buff_velocidade = 0


# agrupar sprites
todas_as_sprites = pygame.sprite.Group()
grupo_inimigos1 = pygame.sprite.Group()
grupo_inimigos2 = pygame.sprite.Group()
grupo_todos_inimigos = pygame.sprite.Group()
grupo_efeito1 = pygame.sprite.Group()
grupo_efeito2 = pygame.sprite.Group()
