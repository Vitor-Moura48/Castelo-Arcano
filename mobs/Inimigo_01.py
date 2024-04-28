from Configurações.config import *
from Configurações  import Global
from mobs.Mob import Mob

sprite_sheet_inimigo = pygame.image.load(os.path.join('imagens/inimigo1.png')).convert_alpha()
rect_inimigo1 = sprite_sheet_inimigo.get_rect()
largura_inimigo1 = rect_inimigo1.width
altura_inimigo1 = rect_inimigo1.height

class SpritesInimigo1(pygame.sprite.Sprite, Mob):  # criar classe de sprites para os inimigos 1
    def __init__(self, vida, dano):
        pygame.sprite.Sprite.__init__(self)
        Mob.__init__(self, vida, dano)


        # seleciona a sprite que vai ser exibida
        self.image = sprite_sheet_inimigo.subsurface((0, 0), (391, 639))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (largura_inimigo1 * 0.13 * Global.proporcao, altura_inimigo1 * 0.13 * Global.proporcao))
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

        self.rect.x = randint(Global.dimensoes_janela[0], Global.dimensoes_janela[0] + 1000)
        self.rect.y = randint(int(Global.dimensoes_janela[1] * 0.1), int(Global.dimensoes_janela[1] - self.rect.size[1]))
    

    # atualizar estado
    def update(self):

        self.contar_vulnerabilidade
        if self.conferir_vida():
            self.morrer()
        
        # mudar escala
        self.image = pygame.transform.scale(self.image, (largura_inimigo1 * 0.13 * Global.proporcao, altura_inimigo1 * 0.13 * Global.proporcao))

        # ajusta as dimensoes do retangulo
        self.posicao_atual_rect = self.rect.center
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.inflate(self.rect, -(largura_inimigo1 * 0.025), -(altura_inimigo1 * 0.015))
        self.rect.center = self.posicao_atual_rect

        # alternar o movimento em y (zig-zag)
        if Global.inimigos_restantes <= 20:

            if self.subir:
                self.rect.top -= Global.velocidade_inimigo * 0.75
                self.image = self.imagem_para_cima
                if self.rect.top < Global.dimensoes_janela[1] * 0.1:
                    self.subir = False

            if not self.subir:
                self.rect.top += Global.velocidade_inimigo * 0.75
                self.image = self.imagem_para_baixo
                if self.rect.bottom > Global.dimensoes_janela[1]:
                    self.subir = True

        else:
            self.image = self.imagem_normal

        # movimentar no eixo x
        self.rect.x -= Global.velocidade_inimigo

        if self.rect.top < Global.dimensoes_janela[1] * 0.1:
            self.rect.top = Global.dimensoes_janela[1] * 0.1
        if self.rect.bottom > Global.dimensoes_janela[1]:
            self.rect.bottom = Global.dimensoes_janela[1]