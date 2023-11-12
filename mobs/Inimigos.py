from Configurações.config import *
from Configurações  import Variaveis_globais
from mobs import Player


sprite_sheet_inimigo = pygame.image.load(os.path.join('imagens/inimigo1.png')).convert_alpha()
rect_inimigo1 = sprite_sheet_inimigo.get_rect()
largura_inimigo1 = rect_inimigo1.width
altura_inimigo1 = rect_inimigo1.height

sprite_sheet_inimigo2 = pygame.image.load(os.path.join('imagens/inimigo2.png'))
rect_inimigo2 = sprite_sheet_inimigo2.get_rect()
largura_inimigo2 = rect_inimigo2.width
altura_inimigo2 = rect_inimigo2.height

class SpritesInimigo1(pygame.sprite.Sprite):  # criar classe de sprites para os inimigos 1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # seleciona a sprite que vai ser exibida
        self.image = sprite_sheet_inimigo.subsurface((0, 0), (391, 639))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (largura_inimigo1 * 0.13 * Variaveis_globais.proporcao, altura_inimigo1 * 0.13 * Variaveis_globais.proporcao))
        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        self._rect = pygame.Rect.inflate(self.rect, -(largura_inimigo1 * 0.025), -(altura_inimigo1 * 0.015))

        # randomiza as coordenadas que o inimigo vai spawnar
        self.randomizar()

        # variavel para ajudar a definir a direção do 'zig-zag'
        self.subir = True

        # variaveis para animação
        self.imagem_para_cima = pygame.transform.rotate(self.image, -10)
        self.imagem_para_baixo = pygame.transform.rotate(self.image, 10)
        self.imagem_normal = pygame.transform.rotate(self.image, 0)

    def randomizar(self):

        self.rect.x = randint(Variaveis_globais.dimensoes_janela[0], Variaveis_globais.dimensoes_janela[0] + 1000)
        self.rect.y = randint(int(Variaveis_globais.dimensoes_janela[1] * 0.1), int(Variaveis_globais.dimensoes_janela[1] - self.rect.size[1]))

    # atualizar estado
    def update(self):
        
        # mudar escala
        self.image = pygame.transform.scale(self.image, (largura_inimigo1 * 0.13 * Variaveis_globais.proporcao, altura_inimigo1 * 0.13 * Variaveis_globais.proporcao))

        # ajusta as dimensoes do retangulo
        self.posicao_atual_rect = self.rect.center
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.inflate(self.rect, -(largura_inimigo1 * 0.025), -(altura_inimigo1 * 0.015))
        self.rect.center = self.posicao_atual_rect

        # alternar o movimento em y (zig-zag)
        if Variaveis_globais.inimigos_restantes <= 20:

            if self.subir:
                self.rect.top -= Variaveis_globais.velocidade_inimigo * 0.75
                self.image = self.imagem_para_cima
                if self.rect.top < Variaveis_globais.dimensoes_janela[1] * 0.1:
                    self.subir = False

            if not self.subir:
                self.rect.top += Variaveis_globais.velocidade_inimigo * 0.75
                self.image = self.imagem_para_baixo
                if self.rect.bottom > Variaveis_globais.dimensoes_janela[1]:
                    self.subir = True

        else:
            self.image = self.imagem_normal

        # movimentar no eixo x
        self.rect.x -= Variaveis_globais.velocidade_inimigo

        if self.rect.top < Variaveis_globais.dimensoes_janela[1] * 0.1:
            self.rect.top = Variaveis_globais.dimensoes_janela[1] * 0.1
        if self.rect.bottom > Variaveis_globais.dimensoes_janela[1]:
            self.rect.bottom = Variaveis_globais.dimensoes_janela[1]


class SpritesInimigo2(pygame.sprite.Sprite):  # criar classe de inimigos 2

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # seleciona a sprite que vai ser exibida
        self.image = sprite_sheet_inimigo2.subsurface((60, 150), (330, 390))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (largura_inimigo2 * 0.2, altura_inimigo2 * 0.2))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()
        rect_ajustado = pygame.Rect.inflate(self.rect, -(largura_inimigo2 * 0.1), -(altura_inimigo2 * 0.01))
        self.rect = rect_ajustado

        self.aceleracao = 0

        # randomizar as coordenadas de spaw do inimigo
        self.randomizar()

        # variaveis para animação
        self.imagem_para_cima = pygame.transform.rotate(self.image, -10)
        self.imagem_para_baixo = pygame.transform.rotate(self.image, 10)
        self.imagem_normal = pygame.transform.rotate(self.image, 0)

    def randomizar(self):

        self.rect.x = randint(Variaveis_globais.dimensoes_janela[0], Variaveis_globais.dimensoes_janela[0] + 500)
        self.rect.y = randint(int(Variaveis_globais.dimensoes_janela[1] * 0.1), int(Variaveis_globais.dimensoes_janela[1] - self.rect.size[1]))

    # atualizar informações
    def update(self):
        # mudar tamanho da sprite
        self.image = pygame.transform.scale(self.image, (largura_inimigo2 * 0.2 * Variaveis_globais.proporcao, altura_inimigo2 * 0.2 * Variaveis_globais.proporcao))

        # ajusta as dimensoes do retangulo
        self.posicao_atual_rect = self.rect.center
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.inflate(self.rect, -(largura_inimigo2 * 0.1), -(altura_inimigo2 * 0.01))
        self.rect.center = self.posicao_atual_rect

        # alternar o movimento em relação com o jogador (para subir)
        if  Player.player.rect.center[1] > int(Variaveis_globais.dimensoes_janela[1] * 0.5) and self.rect.top > int(Variaveis_globais.dimensoes_janela[1] * 0.1):
            self.rect.top -= Variaveis_globais.velocidade_inimigo * 0.7
            if self.rect.top <= int(Variaveis_globais.dimensoes_janela[1] * 0.1):
                self.image = self.imagem_normal
            else:
                self.image = self.imagem_para_cima
                

        # alternar o movimento em relação com o jogador (para descer)
        if  Player.player.rect.center[1] <= int(Variaveis_globais.dimensoes_janela[1] * 0.5) and self.rect.bottom < Variaveis_globais.dimensoes_janela[1]:
            self.rect.top += Variaveis_globais.velocidade_inimigo * 0.7
            if self.rect.bottom >= Variaveis_globais.dimensoes_janela[1]:
                self.image = self.imagem_normal
            else:
                self.image = self.imagem_para_baixo

        
        # faz com que o inimigo fique mais rápido quando está nas bordas de cima ou de baixo da tela
        if self.rect.top <= Variaveis_globais.dimensoes_janela[1] * 0.2 or self.rect.bottom >= Variaveis_globais.dimensoes_janela[1] * 0.9 or self.rect.center[0] < Player.player.rect.center[0]:
            if self.aceleracao < Variaveis_globais.velocidade_inimigo:
                self.aceleracao += Variaveis_globais.velocidade_inimigo * 0.01
        else:
            if self.aceleracao > Variaveis_globais.velocidade_inimigo * -1:
                self.aceleracao -= Variaveis_globais.velocidade_inimigo * 0.01
        
    
        # alterar movimento em x
        self.rect.x -= (Variaveis_globais.velocidade_inimigo * 0.7) + self.aceleracao
