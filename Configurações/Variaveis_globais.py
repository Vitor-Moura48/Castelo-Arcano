from Configurações.config import *

eixo_joystick = 0
eixo_x_joystick = 0
eixo_y_joystick = 0


barreira = 0
vidas_castelo = 10
inimigos_restantes = 0
inimigos_totais = 0

velocidade_player = velocidade_base_player
velocidade_inimigo = 0
mudanca_de_velocidade = [False, False, False, False]

perdeu = False
ganhou = False

maior_recorde = []

dificuldade = 0

tempo_buff_velocidade = 0
tempo_de_recarga = 60


# agrupar sprites
todas_as_sprites = pygame.sprite.Group()
grupo_inimigos1 = pygame.sprite.Group()
grupo_inimigos2 = pygame.sprite.Group()
grupo_todos_inimigos = pygame.sprite.Group()
grupo_efeito1 = pygame.sprite.Group()
grupo_efeito2 = pygame.sprite.Group()
grupo_projeteis_aliados = pygame.sprite.Group()
