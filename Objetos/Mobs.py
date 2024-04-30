from Configurações.config import pygame, os, randint, efeito_morte, draw, numpy, choice
from Configurações import Global
from Objetos import Projeteis

player = None
castelo = None
class Mob(pygame.sprite.Sprite):
    def __init__(self, caminho, linhas_colunas, dimensoes, inflar, vida, dano=0, random_x=500, escala=None):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = pygame.image.load(os.path.join(caminho)).convert_alpha()
    
        self.sprites = [ self.sprite.subsurface((coluna *  dimensoes[0], linha * dimensoes[1]), (dimensoes[0], dimensoes[1])) for linha in range(linhas_colunas[0]) for coluna in range(linhas_colunas[1]) ]
        self.sprite_index = 0

        self.image = self.sprites[self.sprite_index]
        self.image = pygame.transform.scale(self.image, escala) if escala != None else self.image

        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.inflate(self.rect, inflar[0], inflar[1])

        self.vida = vida
        self.dano = dano
        self.random_x = random_x
        self.linhas = linhas_colunas[0]
        self.colunas = linhas_colunas[1]
        self.contador_ivulnerabilidade = 0
        self.velocidade_x = 0
        self.velocidade_y = 0
    
    def receber_dano(self, dano):
        self.vida -= dano
    
    def conferir_vida(self):
        if self.vida <= 0:
            return True
    
    def contar_vulnerabilidade(self):
        if self.contador_ivulnerabilidade > 0:
            self.contador_ivulnerabilidade -= 1

    def morrer(self):
        if Global.som_ligado:
            efeito_morte.play()
        self.kill()
        Global.inimigos_restantes -= 1
    
    def randomizar(self):
        self.rect = self.image.get_rect()
        self.rect.x = randint(Global.dimensoes_janela[0], Global.dimensoes_janela[0] + self.random_x)
        self.rect.y = randint(int(Global.dimensoes_janela[1] * 0.1), int(Global.dimensoes_janela[1] - self.rect.size[1]))
    
    def mover(self):
        if abs(self.velocidade_x) >= 1:
            self.rect.x += self.velocidade_x
            self.velocidade_x -= int(self.velocidade_x)
        if abs(self.velocidade_y) >= 1:
            self.rect.y += self.velocidade_y
            self.velocidade_y -= int(self.velocidade_y)
    
    def contar_index(self, taxa=0.1):
        if self.sprite_index < ( self.linhas * self.colunas ) - 1:
            self.image = self.sprites[int(self.sprite_index)]
            self.sprite_index += taxa
            return True
        else:
            return False


sprite2 = pygame.image.load(os.path.join("imagens/mago_master.png"))
class SpritesPlayer(Mob):  # criar classe de sprites para o jogador
    def __init__(self, vida, dano):
        Mob.__init__(self, 'imagens/mago.png', (2, 4), (85, 94), (-30, -10), vida, dano, escala=(68 * Global.proporcao, 95 * Global.proporcao))

        self.sprites2 = [ sprite2.subsurface((coluna *  122, linha * 110), (122, 110)) for linha in range(2) for coluna in range(4) ]

        self.modo_atual = 1

        self.rect.center = (Global.dimensoes_janela[0] // 2, Global.dimensoes_janela[1] // 2)
    
    def trocar_modo(self):
        self.sprite_index = 0
        if self.modo_atual == 1:
            self.modo_atual = 2
        else:
            self.modo_atual = 1
    
    # atualizar imagem
    def update(self):

        self.contar_vulnerabilidade()

        if not self.contar_index():
            self.sprite_index = 0

        if self.modo_atual == 1:
            pass
        else:
            pass

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Global.dimensoes_janela[0]:
            self.rect.right = Global.dimensoes_janela[0]
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Global.dimensoes_janela[1]:
            self.rect.bottom = Global.dimensoes_janela[1]
        
        draw.rect(Global.tela, (255,000, 000), self.rect, 2)


class SpritesBoss1(Mob):  # criar classe de sprites para primeiro boss
    def __init__(self, vida, dano):
        Mob.__init__( self, 'imagens/boss_01.png', (5, 4), (80, 70), (-10, -10), vida, dano, escala=( 224 * Global.proporcao, 245 * Global.proporcao ) )

        self.rect.right = Global.dimensoes_janela[0]
        self.rect.centery = Global.dimensoes_janela[1] / 2

    # atualizar estado
    def update(self):

        self.contar_vulnerabilidade()
        if self.conferir_vida():
            self.morrer()
        
        self.contar_index()
       
        # movimentar
        self.velocidade_x -= Global.velocidade_inimigo * 0.1
        self.rect.y += numpy.cos(self.rect.x / 15)
        self.mover()

        # mudar escala
        self.image = pygame.transform.scale(self.image, (224 * Global.proporcao, 245 * Global.proporcao))


class SpriteCastelo(Mob):  # criar classe de sprites para o cenário
    def __init__(self, vida):
        Mob.__init__( self, 'imagens/dark_castle.png', (1, 1), (381, 655), (0, 0), vida, escala=( 248 * Global.proporcao, 426 * Global.proporcao ) )

        # posicionar o fundo da imagem na parte mais 'baixa' da tela
        self.rect.bottomleft = (0, Global.dimensoes_janela[1])


class SpritesInimigo1(Mob):  # criar classe de sprites para os inimigos 1
    def __init__(self, vida, dano):
        Mob.__init__(self, 'imagens/inimigo1.png', (1, 1), (391, 639), (-10, -10), vida, dano, random_x=1000, escala=(51 * Global.proporcao, 83 * Global.proporcao))

        # randomiza as coordenadas que o inimigo vai spawnar
        self.randomizar()

        # variavel para ajudar a definir a direção do 'zig-zag'
        self.subir = choice([True, False])

        # variaveis para animação
        self.imagem_para_cima = pygame.transform.rotate(self.image, -10)
        self.imagem_para_baixo = pygame.transform.rotate(self.image, 10)
        self.imagem_normal = pygame.transform.rotate(self.image, 0)
    
    # atualizar estado
    def update(self):

        self.contar_vulnerabilidade
        if self.conferir_vida():
            self.morrer()

        # alternar o movimento em y (zig-zag)
        if Global.inimigos_restantes <= 20:

            if self.subir:
                self.velocidade_y -= Global.velocidade_inimigo * 0.75
                self.image = self.imagem_para_cima
                if self.rect.top < Global.dimensoes_janela[1] * 0.1:
                    self.subir = False

            if not self.subir:
                self.velocidade_y += Global.velocidade_inimigo * 0.75
                self.image = self.imagem_para_baixo
                if self.rect.bottom > Global.dimensoes_janela[1]:
                    self.subir = True

        else:
            self.image = self.imagem_normal

        # movimentar no eixo x
        self.velocidade_x -= Global.velocidade_inimigo
        self.mover()


class SpritesInimigo2(Mob):  # criar classe de inimigos 2
    def __init__(self, vida, dano):
        Mob.__init__(self, 'imagens/inimigo2.png', (1, 1), (340, 420), (-33, -39), vida, dano, escala=(66 * Global.proporcao, 78 * Global.proporcao) )

        self.aceleracao = 0

        # randomizar as coordenadas de spaw do inimigo
        self.randomizar()

        # variaveis para animação
        self.imagem_para_cima = pygame.transform.scale(pygame.transform.rotate(self.image, -10), (95 * Global.proporcao, 120 * Global.proporcao)) # ajuste de distorção
        self.imagem_para_baixo = pygame.transform.scale(pygame.transform.rotate(self.image, 10), (95 * Global.proporcao, 120 * Global.proporcao))
        self.imagem_normal = pygame.transform.rotate(self.image, 0)

    # atualizar informações
    def update(self):

        self.contar_vulnerabilidade()
        if self.conferir_vida():
            self.morrer()

        # alternar o movimento em relação com o jogador (para subir)
        if  player.rect.center[1] > int(Global.dimensoes_janela[1] * 0.5) and self.rect.top > int(Global.dimensoes_janela[1] * 0.1):
            self.velocidade_y -= Global.velocidade_inimigo * 0.7
            if self.rect.top <= int(Global.dimensoes_janela[1] * 0.1):
                self.image = self.imagem_normal
            else:
                self.image = self.imagem_para_cima

        # alternar o movimento em relação com o jogador (para descer)
        else:
            if self.rect.bottom < Global.dimensoes_janela[1]:
                self.velocidade_y += Global.velocidade_inimigo * 0.7
                if self.rect.bottom >= Global.dimensoes_janela[1]:
                    self.image = self.imagem_normal
                else:
                    self.image = self.imagem_para_baixo

        # faz com que o inimigo fique mais rápido quando está nas bordas de cima ou de baixo da tela
        if self.rect.top <= Global.dimensoes_janela[1] * 0.2 or self.rect.bottom >= Global.dimensoes_janela[1] * 0.9 or self.rect.center[0] < player.rect.center[0]:
            if self.aceleracao < Global.velocidade_inimigo: # limite de avamço
                self.aceleracao += Global.velocidade_inimigo * 0.01 # avança
        else:
            if self.aceleracao > Global.velocidade_inimigo * -1: # limite de recuo
                self.aceleracao -= Global.velocidade_inimigo * 0.01 # recua
        
    
        # alterar movimento em x
        self.velocidade_x -= (Global.velocidade_inimigo * 0.7) + self.aceleracao
        self.mover()


class SpritesInimigo3(Mob):  # criar classe de sprites para os inimigos 3
    def __init__(self, vida, dano):
        Mob.__init__(self, 'imagens/inimigo3.png', (3, 4), (45, 51), (0, 0), vida, dano, escala=( 90 * Global.proporcao, 76 * Global.proporcao ) )

        self.recarga_disparos = 180
        # randomiza as coordenadas que o inimigo vai spawnar
        self.randomizar()

    def atirar(self):
        projetil_inimigo_03 = Projeteis.ProjetilInimigo(self.rect.center, 1, 1)
        Global.grupo_projeteis_inimigos.add(projetil_inimigo_03)
        Global.todas_as_sprites.add(projetil_inimigo_03)
        projetil_inimigo_03.atirar()
        self.recarga_disparos = 180
    
    # atualizar estado
    def update(self):

        if self.conferir_vida():
            self.morrer() if not self.contar_index() else None
  
        else:
            self.contar_vulnerabilidade()
            
            self.recarga_disparos -= 1

            # movimentar no eixo x
            if self.rect.right > Global.dimensoes_janela[0] * 0.9:
                self.velocidade_x -= Global.velocidade_inimigo * 0.4
            # quando chegar a uma certa distancia, para no eixo x e passa a desviar do projeteis
            else:
                projetil_mais_proximo = None

                for projeil in Global.grupo_projeteis_aliados:

                    distancia_x = projeil.rect.center[0] - self.rect.center[0]
                    distancia_y = projeil.rect.center[1] - self.rect.center[1]
                    distancia_absoluta = (abs(distancia_x) ** 2 + abs(distancia_y) ** 2) ** 0.5

                    if projetil_mais_proximo == None or distancia_absoluta < projetil_mais_proximo[1]:
                        projetil_mais_proximo = [projeil, distancia_absoluta, distancia_x, distancia_y]
                
                if projetil_mais_proximo != None and projetil_mais_proximo[1] < 800:
                    
                    if projetil_mais_proximo[0].rect.centery < Global.dimensoes_janela[1] / 2:
                        self.velocidade_y += Global.velocidade_inimigo * 1.5
                    else:
                        self.velocidade_y -= Global.velocidade_inimigo * 1.5
                  
                # confere se é possível disparar algum projetil
                if self.recarga_disparos <= 0:
                    self.atirar()
            
            # define os limites de movimentação
            if self.rect.top < Global.dimensoes_janela[1] * 0.1:
                self.rect.top = Global.dimensoes_janela[1] * 0.1

            if self.rect.bottom > Global.dimensoes_janela[1]:
                self.rect.bottom = Global.dimensoes_janela[1]
        
        self.mover()