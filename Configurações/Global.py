from Configurações.config import *

# criar a tela
tela = display.set_mode(dimensao_base, pygame.RESIZABLE)

# definir cor da tela
tela.fill((000, 000, 000))

som_ligado = False

barreira = 0
inimigos_restantes = 0
inimigos_totais = 0

contador_de_bosses = 0

perdeu = False
ganhou = False

dificuldade = 0

tempo_buff_velocidade = 0
tempo_buff_multiplos_disparos = 0
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

textos = []

# agrupar sprites
todas_as_sprites = pygame.sprite.Group()
grupo_inimigos1 = pygame.sprite.Group()
grupo_inimigos2 = pygame.sprite.Group()
grupo_inimigos3 = pygame.sprite.Group()
grupo_todos_inimigos = pygame.sprite.Group()
grupo_todos_bosses = pygame.sprite.Group()

grupo_efeitos = pygame.sprite.Group()

grupo_projeteis_aliados = pygame.sprite.Group()
grupo_projeteis_inimigos = pygame.sprite.Group()

componentes = pygame.sprite.Group()
componente_botao = pygame.sprite.Group()
