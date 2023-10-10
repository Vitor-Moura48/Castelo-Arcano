from Configurações.config import *
from Configurações  import Variaveis_globais
import Player


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

        # alternar o movimento em y (zig-zag)
        if Variaveis_globais.inimigos_restantes <= 20:

            if self.subir:
                self.rect.top -= Variaveis_globais.velocidade_inimigo * 0.75
                self.image = self.imagem_para_cima
                if self.rect.top <= 70:
                    self.subir = False

            if not self.subir:
                self.rect.top += Variaveis_globais.velocidade_inimigo * 0.75
                self.image = self.imagem_para_baixo
                if self.rect.top >= 400:
                    self.subir = True

        else:
            self.image = self.imagem_normal

        # movimentar no eixo x
        self.rect.x -= Variaveis_globais.velocidade_inimigo
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

        # alternar o movimento em relação com o jogador (para subir)
        if  Player.player.rect.center[1] > int(altura_da_tela * 0.5) and self.rect.top > int(altura_da_tela * 0.14):
            self.rect.top -= 300 / fps
            if self.rect.top <= int(altura_da_tela * 0.14):
                self.image = self.imagem_normal
            else:
                self.image = self.imagem_para_cima

        # alternar o movimento em relação com o jogador (para descer)
        if  Player.player.rect.center[1] <= int(altura_da_tela * 0.5) and self.rect.bottom < altura_da_tela:
            self.rect.top += 300 / fps
            if self.rect.bottom >= altura_da_tela:
                self.image = self.imagem_normal
            else:
                self.image = self.imagem_para_baixo

        # alterar movimento em x
        self.rect.x -= Variaveis_globais.velocidade_inimigo * 0.8

        # faz com que o inimigo fique mais rápido quando está nas bordas de cima ou de baixo da tela
        if self.rect.top <= 70 or self.rect.bottom >= 500:
            self.rect.x -= 2

        # mudar tamanho da sprite
        self.image = pygame.transform.scale(self.image, (largura_inimigo2 * 0.25, altura_inimigo2 * 0.25))