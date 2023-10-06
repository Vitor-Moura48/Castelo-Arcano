from Configurações import *
import Variaveis_globais
import Player


eixo_joystick = 0
eixo_x_joystick = 0
eixo_y_joystick = 0


# função para definir o modo de jogo e outras coisas
def iniciar_jogo():

    global inimigos_restantes, velocidade_player, \
           velocidade_inimigo, perdeu, ganhou, inimigos_totais

    if dificuldade == 1:

        inimigos_totais = 50
        inimigos_restantes = inimigos_totais
        velocidade_inimigo = 500 / fps

    if dificuldade == 2:

        inimigos_totais = 70
        inimigos_restantes = inimigos_totais
        velocidade_inimigo = 700 / fps

    if dificuldade == 3:

        inimigos_totais = 100
        inimigos_restantes = inimigos_totais
        velocidade_inimigo = 800 / fps

    

    pygame.mixer_music.play(-1)




sprite_sheet_castelo = pygame.image.load(os.path.join('imagens/dark_castle.png')).convert_alpha()
rect_castelo = sprite_sheet_castelo.get_rect()
largura_castelo = rect_castelo.width
altura_castelo = rect_castelo.height

sprite_sheet_inimigo = pygame.image.load(os.path.join('imagens/inimigo1.png')).convert_alpha()
rect_inimigo1 = sprite_sheet_inimigo.get_rect()
largura_inimigo1 = rect_inimigo1.width
altura_inimigo1 = rect_inimigo1.height

sprite_sheet_inimigo2 = pygame.image.load(os.path.join('imagens/inimigo2.png'))
rect_inimigo2 = sprite_sheet_inimigo2.get_rect()
largura_inimigo2 = rect_inimigo2.width
altura_inimigo2 = rect_inimigo2.height

sprite_sheet_efeitos = pygame.image.load(os.path.join('imagens/bolas de efeito.png')).convert_alpha()
rect_efeitos = sprite_sheet_efeitos.get_rect()
largura_efeitos = rect_efeitos.width
altura_efeitos = rect_efeitos.height

sprite_sheet_barreira = pygame.image.load(os.path.join('imagens/efeito barreira.png')).convert_alpha()
rect_barreira = sprite_sheet_barreira.get_rect()
largura_barreirra = rect_barreira.width
altura_barreira = rect_barreira.height

sprite_sheet_projeteis = pygame.image.load(os.path.join('imagens/Projeteis.png')).convert_alpha()
rect_projeteis = sprite_sheet_projeteis.get_rect()
largura_projeteis = rect_projeteis.width
altura_projeteis = rect_projeteis.height

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




class Projetil(pygame.sprite.Sprite):  # criar classe para projetil do player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # carregar e colocar as imagens na lista de sprites do projetil
        self.sprites_projetil = []

        for frame in range(8):

            self.img_linha9_projetil = sprite_sheet_projeteis.subsurface((215, 310), (50, 50))
            self.sprites_projetil.append(self.img_linha9_projetil)

        # definir a imagem que vai ser exibida
        self.index_lista_projetil = 0
        self.index_lista_projetil += 1
        self.image = self.sprites_projetil[int(self.index_lista_projetil)]

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # definir as coordenadas do projetil
        self.rect.center = (Variaveis_globais.x_player - 12, Variaveis_globais.y_player - 7)

        # para disparar projetil
        self.clicou = False
        self.contador = 0

        self.projetil_x = 0
        self.projetil_y = 0

    # lógica para atirar
    def atirar(self):

        # obtem as coordenadas do mouse
        posicao_mouse = mouse.get_pos()

        # obtem as diferencas entre o mouse e o projetil em cada eixo
        if self.contador == 0:
            self.projetil_x = (posicao_mouse[0] - self.rect.center[0])
            self.projetil_y = (posicao_mouse[1] - self.rect.center[1])
            self.contador += 1

        # armazena em uma variavel a 'mínima' parte da velocidade_projetil (de forma diretamente proporcional)
        distribuicao_velocidade = velocidade_projetil / (abs(self.projetil_x) + abs(self.projetil_y))

        # junta as 'mínimas partes' de forma diretamente proporcional a variavel self
        velocidade_x = distribuicao_velocidade * self.projetil_x
        velocidade_y = distribuicao_velocidade * self.projetil_y

        # faz o projetil se mover de acordo com resultado da distribuição final obtida
        self.rect.left += velocidade_x
        self.rect.top += velocidade_y

        # define se o projetil saiu ou não da tela, se sim, a função update deixa de chamar essa função repetidamente
        if self.rect.right > 1500 or self.rect.left < 0 or self.rect.top > 500 or self.rect.bottom < 0:
            self.clicou = False

    def update(self):

        # atualizar imagem
        self.index_lista_projetil += 10 / fps

        if self.index_lista_projetil >= 8:
            self.index_lista_projetil = 0

        self.image = self.sprites_projetil[int(self.index_lista_projetil)]

        # confere se o jogador clicou para disparar
        if self.clicou:
            self.atirar()
        # senão o projetil vai ficar "atrás" do mago (jogador)
        else:
            self.rect.center = (Variaveis_globais.x_player - 12, Variaveis_globais.y_player - 7)
            self.contador = 0


class SpritesInimigo1(pygame.sprite.Sprite):  # criar classe de sprites para os inimigos 1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # seleciona a sprite que vai ser exibida
        self.image = sprite_sheet_inimigo.subsurface((0, 0), (391, 639))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (largura_inimigo1 * 0.35, altura_inimigo1 * 0.35))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # randomiza as coordenadas que o inimigo vai spawnar
        self.randomizar()

        # variavel para ajudar a definir a direção do 'zig-zag'
        self.subir = True

        # variaveis para animação
        self.imagem_para_cima = pygame.transform.rotate(self.image, -10)
        self.imagem_para_baixo = pygame.transform.rotate(self.image, 10)
        self.imagem_normal = pygame.transform.rotate(self.image, 0)

    def randomizar(self):
        global largura_da_tela, altura_da_tela

        self.rect.x = randint(largura_da_tela, largura_da_tela + 500)
        self.rect.y = randint(int(altura_da_tela * 0.14), int(altura_da_tela * 0.84))

    # atualizar estado
    def update(self):
        global inimigos_restantes, barreira, vidas_castelo

        # alternar o movimento em y (zig-zag)
        if inimigos_restantes <= 20:

            if self.subir:
                self.rect.top -= velocidade_inimigo * 0.75
                self.image = self.imagem_para_cima
                if self.rect.top <= 70:
                    self.subir = False

            if not self.subir:
                self.rect.top += velocidade_inimigo * 0.75
                self.image = self.imagem_para_baixo
                if self.rect.top >= 400:
                    self.subir = True

        else:
            self.image = self.imagem_normal

        # movimentar no eixo x
        self.rect.x -= velocidade_inimigo
        self.rect.y = self.rect.y + (numpy.cos(self.rect.x / 140) * 4)

        if self.rect.top <= 70:
            self.rect.top = 70
        if self.rect.top > 400:
            self.rect.top = 400

        # mudar escala
        self.image = pygame.transform.scale(self.image, (largura_inimigo1 * 0.15, altura_inimigo1 * 0.15))


class SpritesInimigo2(pygame.sprite.Sprite):  # criar classe de inimigos 2

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # seleciona a sprite que vai ser exibida
        self.image = sprite_sheet_inimigo2.subsurface((0, 0), (391, 639))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (largura_inimigo2 * 0.25, altura_inimigo2 * 0.25))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # randomizar as coordenadas de spaw do inimigo
        self.randomizar()

        # variaveis para animação
        self.imagem_para_cima = pygame.transform.rotate(self.image, -10)
        self.imagem_para_baixo = pygame.transform.rotate(self.image, 10)
        self.imagem_normal = pygame.transform.rotate(self.image, 0)

    def randomizar(self):
        global largura_da_tela, altura_da_tela

        self.rect.x = randint(largura_da_tela, largura_da_tela + 500)
        self.rect.y = randint(int(altura_da_tela * 0.14), int(altura_da_tela * 0.82))

    # atualizar informações
    def update(self):
        global inimigos_restantes, barreira, vidas_castelo

        # alternar o movimento em relação com o jogador (para subir)
        if player.rect.center[1] > int(altura_da_tela * 0.5) and self.rect.top > int(altura_da_tela * 0.14):
            self.rect.top -= 300 / fps
            if self.rect.top <= int(altura_da_tela * 0.14):
                self.image = self.imagem_normal
            else:
                self.image = self.imagem_para_cima

        # alternar o movimento em relação com o jogador (para descer)
        if player.rect.center[1] <= int(altura_da_tela * 0.5) and self.rect.bottom < altura_da_tela:
            self.rect.top += 300 / fps
            if self.rect.bottom >= altura_da_tela:
                self.image = self.imagem_normal
            else:
                self.image = self.imagem_para_baixo

        # alterar movimento em x
        self.rect.x -= velocidade_inimigo * 0.8

        # faz com que o inimigo fique mais rápido quando está nas bordas de cima ou de baixo da tela
        if self.rect.top <= 70 or self.rect.bottom >= 500:
            self.rect.x -= 2

        # mudar tamanho da sprite
        self.image = pygame.transform.scale(self.image, (largura_inimigo2 * 0.25, altura_inimigo2 * 0.25))


class SpritesEfeito1(pygame.sprite.Sprite):  # classe para efeito especiail 1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # defina a imagem que vai ser exibida
        self.image = sprite_sheet_efeitos.subsurface((0, 320), (320, 320))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.2, 320 * 0.2))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # variaveis para definir o tempo de buff
        self.tempo_buff = 100
        self.buffar = False

        # randomizar a posição que o buff vai ser spawnado
        self.randomizar()

    def randomizar(self):
        global largura_da_tela, altura_da_tela

        self.rect.left = randint(largura_da_tela, largura_da_tela + 500)
        self.rect.top = randint(int(altura_da_tela * 0.14), int(altura_da_tela * 0.84))

    # fução chamada quando o player colide com o buff
    def buff(self):
        self.tempo_buff = 100
        self.buffar = True

    # atualizar estado
    def update(self):
        global velocidade_player

        # aplica o efeito de buff e começa a contar o tempo para parar o efeito (aumenta a velocidade do player)
        if self.buffar:
            self.tempo_buff -= 0.2

            if self.tempo_buff > 0:
                velocidade_player = 525 / fps

            else:
                velocidade_player = 350 / fps

                self.buffar = False
                self.tempo_buff = 100

        # para movimentar o buff no eixo x
        self.rect.x -= velocidade_inimigo

        # mudar dimensões da imagem
        self.image = pygame.transform.scale(self.image, (320 * 0.2, 320 * 0.2))


class SpritesEfeito2(pygame.sprite.Sprite):  # classe para efeito especiail 2
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # define imagem que vai ser exibida
        self.image = sprite_sheet_efeitos.subsurface((640, 320), (320, 320))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.2, 320 * 0.2))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # randomizar as coordenadas do spaw
        self.randomizar()

    def randomizar(self):
        global largura_da_tela, altura_da_tela

        self.rect.left = randint(largura_da_tela, largura_da_tela + 500)
        self.rect.top = randint(int(altura_da_tela * 0.14), int(altura_da_tela * 0.84))

    # quando o player colide com o buff, ganha um ponto de escudo
    def buff(self):
        global barreira

        Variaveis_globais.barreira += 1

    # atualizar estado
    def update(self):

        # movimentar buff no eixo x
        self.rect.x -= velocidade_inimigo

        # mudar escala do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.2, 320 * 0.2))


class SpritesCenario(pygame.sprite.Sprite):  # criar classe de sprites para o cenário
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # carregar e colocar as imagens na lista de sprites
        self.sprites_castelo = []

        self.img_linha1_castelo = sprite_sheet_castelo.subsurface((0, 0), (largura_castelo, altura_castelo))
        self.sprites_castelo.append(self.img_linha1_castelo)

        # definir imagem que vai ser exibida
        self.image = self.sprites_castelo[0]

        # ajustar escala da imagem
        self.image = pygame.transform.scale(self.image, (largura_castelo * proporcao * 0.65, altura_castelo * proporcao * 0.65))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

    # atualizar estado
    def update(self):
        # ajustar escala da imagem
        self.image = pygame.transform.scale(self.image, (largura_castelo * proporcao * 0.65, altura_castelo * proporcao * 0.65))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        # posicionar o fundo da imagem na parte mais 'baixa' da tela
        self.rect.bottom = altura_da_tela


class EfeitosAnimacao(pygame.sprite.Sprite):  # classe de efeitos diversos que acontecem as vezes
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # carregar e colocar as imagens na lista de sprites
        self.sprites_efeito_barreira = []

        for frame in range(6):
            self.img_linha2 = sprite_sheet_barreira.subsurface((frame * 102, 100), (102, 308))
            self.sprites_efeito_barreira.append(self.img_linha2)

        # definir imagem que vai ser exibida
        self.index_barreira = 0
        self.image = self.sprites_efeito_barreira[self.index_barreira]

        #  mudar dimensões da imagem
        self.image = pygame.transform.scale(self.image, (102 * 4, 308 * 4))

        # encontrar as dimensoes da imagem
        self.rect = self.image.get_rect()

        # posicionar sprite
        self.rect.center = (150, 135)

        # variavel para ajudar na execução do efeito de animação
        self.ativar = False

    def animar1(self):
        self.ativar = True

    # atualizar estado
    def update(self):

        # condição para executar animação
        if self.ativar:
            self.index_barreira += 10 / fps
            self.rect.center = (150, 135)
        else:
            self.rect.center = (-999, -999)

        # manter loop de animação
        if self.index_barreira >= 6:
            self.index_barreira = 0
            self.ativar = False

        # atualizar imagem
        self.image = self.sprites_efeito_barreira[int(self.index_barreira)]

        # ajustar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (102 * 4, 308 * 4))


class VerificarColisoes:  # classe para verificar colisões
    def __init__(self):
        pass

    # função para verificar colisão do jogador com algo
    def colisao_com_player(self):
        global inimigos_restantes

        colisoes_player_inimigo1 = pygame.sprite.spritecollide(player, grupo_inimigos1, True)
        colisoes_player_inimigo2 = pygame.sprite.spritecollide(player, grupo_inimigos2, True)
        colisoes_player_buff1 = pygame.sprite.spritecollide(player, grupo_efeito1, True)
        colisoes_player_buff2 = pygame.sprite.spritecollide(player, grupo_efeito2, True)

        # verifica colisões com inimigos e responde de acordo
        if colisoes_player_inimigo1:
            inimigos_restantes -= 1
            efeito_morte.play()

        if colisoes_player_inimigo2:
            inimigos_restantes -= 1
            efeito_morte.play()

        # verifica colisões com buffs e responde de acordo
        if colisoes_player_buff1:
            efeito_buff1.buff()

        if colisoes_player_buff2:
            efeito_buff2.buff()
            efeito_barreira.animar1()

    # função para verificar colisões do castelo com algo
    def colisao_com_castelo(self):
        global inimigos_restantes, barreira, vidas_castelo

        colisoes_castelo_inimigo1 = pygame.sprite.spritecollide(castelo, grupo_inimigos1, True)
        colisoes_castelo_inimigo2 = pygame.sprite.spritecollide(castelo, grupo_inimigos2, True)

        # verifica colisões com inimigos e responde de acordo
        if colisoes_castelo_inimigo1:
            if  Variaveis_globais.barreira == 0:
                Variaveis_globais.vidas_castelo -= 1
                efeito_explosao.play()
            else:
                Variaveis_globais.barreira -= 1
                efeito_defesa.play()

            inimigos_restantes -= 1

        if colisoes_castelo_inimigo2:
            if  Variaveis_globais.barreira == 0:
                Variaveis_globais.vidas_castelo -= 1
                efeito_explosao.play()
            else:
                Variaveis_globais.barreira -= 1
                efeito_defesa.play()

            inimigos_restantes -= 1

    # função para verificar colisões do projetil do jogador com algo
    def colisao_com_projetil_player(self):
        global inimigos_restantes

        colisoes_projetil_inimigo1 = pygame.sprite.spritecollide(projetil_player, grupo_inimigos1, True)
        colisoes_projetil_inimigo2 = pygame.sprite.spritecollide(projetil_player, grupo_inimigos2, True)

        # verifica colisões com inimigos e responde de acordo
        if colisoes_projetil_inimigo1:
            inimigos_restantes -= 1
            efeito_morte.play()
            projetil_player.clicou = False

        if colisoes_projetil_inimigo2:
            inimigos_restantes -= 1
            efeito_morte.play()
            projetil_player.clicou = False

# agrupar sprites


todas_as_sprites = pygame.sprite.Group()
grupo_inimigos1 = pygame.sprite.Group()
grupo_inimigos2 = pygame.sprite.Group()
grupo_todos_inimigos = pygame.sprite.Group()
grupo_efeito1 = pygame.sprite.Group()
grupo_efeito2 = pygame.sprite.Group()

# criar objetos
controle = Joystick()

projetil_player = Projetil()
todas_as_sprites.add(projetil_player)

player = Player.SpritesPlayer()
todas_as_sprites.add(player)

castelo = SpritesCenario()
todas_as_sprites.add(castelo)

efeito_buff2 = SpritesEfeito2()
todas_as_sprites.add(efeito_buff2)
grupo_efeito2.add(efeito_buff2)

efeito_barreira = EfeitosAnimacao()
todas_as_sprites.add(efeito_barreira)

colisoes = VerificarColisoes()

# criar um clock de atualização em fps
clock = time.Clock()

# fazer uma tela inicial
mensagem_dificuldade = 'Selecione a dificuldade'
mensagem_dificuldade_para_tela = fonte.render(mensagem_dificuldade, True, (255, 50, 50))

mensagem_facil = 'Fácil'
mensagem_facil_para_tela = fonte.render(mensagem_facil, True, (255, 50, 50))

mensagem_medio = 'Normal'
mensagem_medio_para_tela = fonte.render(mensagem_medio, True, (255, 50, 50))

mensagem_dificil = 'Difícil'
mensagem_dificil_para_tela = fonte.render(mensagem_dificil, True, (255, 50, 50))

mensagem_ajustar_tela = 'Ajustar dimensões'
mensagem_ajustar_tela_para_tela = fonte.render(mensagem_ajustar_tela, True, (50, 50, 255))

selecionou = False

while not selecionou:

    # retangulos visuais
    pygame.draw.rect(tela, (140, 140, 140), (655, 140, 200, 50))
    pygame.draw.rect(tela, (100, 100, 100), (655, 240, 200, 50))
    pygame.draw.rect(tela, (60, 60, 60), (655, 340, 200, 50))

    pygame.draw.rect(tela, (200, 200, 200), (135, 140, 300, 50))

    # retangulos para colisão
    facil_rect = pygame.Rect(655, 140, 200, 50)
    medio_rect = pygame.Rect(655, 240, 200, 50)
    dificil_rect = pygame.Rect(655, 340, 200, 50)

    ajuste_rect = pygame.Rect(135, 140, 300, 50)

    # desenhar mensagens
    tela.blit(mensagem_dificuldade_para_tela, (600, 70))
    tela.blit(mensagem_facil_para_tela, (720, 150))
    tela.blit(mensagem_medio_para_tela, (705, 250))
    tela.blit(mensagem_dificil_para_tela, (715, 350))

    tela.blit(mensagem_ajustar_tela_para_tela, (150, 145))

    display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            posicao_mouse = pygame.mouse.get_pos()

            if facil_rect.collidepoint(posicao_mouse):
                dificuldade = 1
                selecionou = True

            if medio_rect.collidepoint(posicao_mouse):
                selecionou = True
                dificuldade = 2

            if dificil_rect.collidepoint(posicao_mouse):
                selecionou = True
                dificuldade = 3

            if ajuste_rect.collidepoint(posicao_mouse):
                largura_da_tela = int(largura_da_tela * 0.95)
                altura_da_tela = int(altura_da_tela * 0.55)
                proprocao = largura_da_tela * altura_da_tela / 750000
                tela = display.set_mode((largura_da_tela, altura_da_tela))

iniciar_jogo()

# laço principal
while True:

    # plano de fundo da  tela 'fluido'
    tela.blit(plano_de_fundo, (-1200, 0))

    # adicionar objetos
    if len(grupo_inimigos1) < 2 and len(grupo_todos_inimigos) < inimigos_restantes:
        for i in range(1):
            inimigo1 = SpritesInimigo1()
            todas_as_sprites.add(inimigo1)
            grupo_inimigos1.add(inimigo1)
            grupo_todos_inimigos.add(inimigo1)

    if len(grupo_inimigos2) < 1 and len(grupo_todos_inimigos) < inimigos_restantes:
        for i in range(1):
            inimigo2 = SpritesInimigo2()
            todas_as_sprites.add(inimigo2)
            grupo_inimigos2.add(inimigo2)
            grupo_todos_inimigos.add(inimigo2)

    chance1 = randint(1, fps * 16)

    if len(grupo_efeito1) < 1 and chance1 == 1:
        efeito_buff1 = SpritesEfeito1()
        todas_as_sprites.add(efeito_buff1)
        grupo_efeito1.add(efeito_buff1)

    chance2 = randint(1, fps * 16)

    if len(grupo_efeito2) < 1 and chance2 == 1:
        efeito_buff2 = SpritesEfeito2()
        todas_as_sprites.add(efeito_buff2)
        grupo_efeito2.add(efeito_buff2)

    # adiconar objetos sprites na tela
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    # verificar colisões
    colisoes.colisao_com_player()
    colisoes.colisao_com_castelo()
    colisoes.colisao_com_projetil_player()

    # para criar texto na janela
    mensagem_kills = f"inimigos restantes: {inimigos_restantes}"
    mensagem_kills_para_tela = fonte.render(mensagem_kills, True, (80, 80, 255))

    mensagem_vidas_castelo = f"vidas restantes: {Variaveis_globais.vidas_castelo}"
    mensagem_vidas_castelo_para_tela = fonte.render(mensagem_vidas_castelo, True, (247, 24, 14))

    mensagem_barreira = f'defesa: {Variaveis_globais.barreira}'
    mensagem_barreira_para_tela = fonte.render(mensagem_barreira, True, (255, 100, 20))

    mensagem_derrota = "você perdeu, pressione enter para continuar"
    mensagem_derrota_para_tela = fonte.render(mensagem_derrota, False,  (200, 0, 0))

    mensagem_vitoria = "você ganhou! pressione enter para continuar"
    mensagem_vitoria_para_tela = fonte.render(mensagem_vitoria, True, (255, 255, 0))

    # responder a eventos
    for event in pygame.event.get():

        if event.type == QUIT:
            print("game over")
            dados = pandas.DataFrame(Variaveis_globais.maior_recorde)

            dados.to_csv('records/recorde_difícil.csv', index=False)
            print(dados)
            quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and not projetil_player.clicou:
            projetil_player.clicou = True
            projetil_player.atirar()

        # responde aos eventos do controle
        if event.type == JOYAXISMOTION:
            controle.movimento(event)

        if event.type == JOYDEVICEADDED:
            controle.__init__()

    # para mover player ao pressionar tecla, ou joystick
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT] or eixo_x_joystick >= 0.4:
        Variaveis_globais.x_player -= Variaveis_globais.velocidade_player
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT] or eixo_x_joystick >= 0.4:
        Variaveis_globais.x_player += Variaveis_globais.velocidade_player
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP] or eixo_y_joystick >= 0.4:
        Variaveis_globais.y_player -= Variaveis_globais.velocidade_player
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN] or eixo_y_joystick >= 0.4:
        Variaveis_globais.y_player += Variaveis_globais.velocidade_player

    # mudança de velocidade dos inimigos
    if inimigos_restantes <= inimigos_totais * 0.8 and not Variaveis_globais.mudanca_de_velocidade[0]:
        velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[0] = True

    elif inimigos_restantes <= inimigos_totais * 0.6 and not Variaveis_globais.mudanca_de_velocidade[1]:
        velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[1] = True

    elif inimigos_restantes <= inimigos_totais * 0.4 and not Variaveis_globais.mudanca_de_velocidade[2]:
        velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[2] = True

    elif inimigos_restantes <= inimigos_totais * 0.2 and not Variaveis_globais.mudanca_de_velocidade[3]:
        velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[3] = True

    # resposta para derrota
    if Variaveis_globais.vidas_castelo <= 0:
        perdeu = True
        efeito_derrota.play()

        while perdeu:
            tela.blit(mensagem_derrota_para_tela, (450, 20))
            display.flip()

            pygame.mixer_music.fadeout(100)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        iniciar_jogo()

    # resposta para vitória
    if inimigos_restantes <= 0:
        ganhou = True
        efeito_vitoria.play()

        if dificuldade == 1:
            novo_dataframe = pandas.DataFrame(data=[Variaveis_globais.vidas_castelo], columns=['Recorde'])
            novo_dataframe.to_csv('records/recorde_fácil.csv', mode='a', index=False, header=False)
        if dificuldade == 2:
            novo_dataframe = pandas.DataFrame()
            novo_dataframe.to_csv('records/recorde_médio.csv', mode='a', index=False, header=False)
        if dificuldade == 3:
            novo_dataframe = pandas.DataFrame(Variaveis_globais.maior_recorde)
            novo_dataframe.to_csv('records/recorde_difícil.csv', mode='a', index=False, header=False)

        while ganhou:
            tela.blit(mensagem_vitoria_para_tela, (450, 20))
            display.flip()

            pygame.mixer_music.fadeout(100)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        iniciar_jogo()

    # colocar o texto na janela
    tela.blit(mensagem_kills_para_tela, (650, 20))
    tela.blit(mensagem_vidas_castelo_para_tela, (20, 20))
    if Variaveis_globais.barreira > 0:
        tela.blit(mensagem_barreira_para_tela, (80, 80))

    # atualizar a tela
    display.flip()

    clock.tick(fps)
