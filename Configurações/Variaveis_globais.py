from Configurações.config import *

# criar a tela
tela = display.set_mode(dimensao_base, pygame.RESIZABLE)

# definir cor da tela
tela.fill((000, 000, 000))

eixo_joystick = 0
eixo_x_joystick = 0
eixo_y_joystick = 0


barreira = 0
vidas_castelo = 10
vida_player = 5
inimigos_restantes = 0
inimigos_totais = 0

contador_de_bosses = 0

perdeu = False
ganhou = False
player_em_jogo = True

maior_recorde = []

dificuldade = 0

tempo_buff_velocidade = 0
tempo_buff_3_projeteis = 0
tempo_buff_velocidade_disparo = 0
tempo_buff_disparo_teleguiado = 0
tempo_de_recarga_disparo = 0

amplitude_projeteis = 10 # graus de desvio, para mais e para menos

dimensoes_janela = pygame.display.get_surface().get_size()

# apenas uma dimensão porque a proporção é sempre a mesma
proporcao = dimensoes_janela[0] / dimensao_base[0]

velocidade_player = velocidade_base_player * proporcao
velocidade_inimigo = 0
mudanca_de_velocidade = [False, False, False, False]

# agrupar sprites
todas_as_sprites = pygame.sprite.Group()
grupo_inimigos1 = pygame.sprite.Group()
grupo_inimigos2 = pygame.sprite.Group()
grupo_inimigos3 = pygame.sprite.Group()
grupo_todos_inimigos = pygame.sprite.Group()
grupo_todos_bosses = pygame.sprite.Group()

grupo_efeito1 = pygame.sprite.Group()
grupo_efeito2 = pygame.sprite.Group()
grupo_efeito3 = pygame.sprite.Group()
grupo_efeito4 = pygame.sprite.Group()
grupo_efeito5 = pygame.sprite.Group()
grupo_todos_efeitos = pygame.sprite.Group()

grupo_projeteis_aliados = pygame.sprite.Group()
grupo_projeteis_inimigos = pygame.sprite.Group()

componentes = pygame.sprite.Group()
