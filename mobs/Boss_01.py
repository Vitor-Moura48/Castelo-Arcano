from Configurações.config import *
from Configurações  import Global
from mobs.Mob import Mob

sprite_sheet_boss_01 = pygame.image.load(os.path.join('imagens/boss_01.png')).convert_alpha()
rect_inimigo1 = sprite_sheet_boss_01.get_rect()
largura_boss_01 = rect_inimigo1.width
altura_boss_01 = rect_inimigo1.height

class SpritesBoss1(pygame.sprite.Sprite, Mob):  # criar classe de sprites para primeiro boss
    def __init__(self, vida, dano):
        pygame.sprite.Sprite.__init__(self)
        Mob.__init__(self, vida, dano)

        self.velocidade = 0

        # seleciona a sprite que vai ser exibida
        self.sprites = []
        for linha in range(5):
            for coluna in range(4):
                if linha == 3 and coluna >= 2:
                    pass
                else:
                    self.sprites.append(sprite_sheet_boss_01.subsurface((80 * coluna, 70 * linha), (80, 70)))
        self.index = 0

        self.image = self.sprites[self.index]

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (largura_boss_01 * 0.7 * Global.proporcao, altura_boss_01 * 0.7 * Global.proporcao))
        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        novo_retangulo = pygame.Rect.inflate(self.rect, -10, -10)
        self.rect = novo_retangulo

        self.rect.right = Global.dimensoes_janela[0]
        self.rect.centery = Global.dimensoes_janela[1] / 2

    # atualizar estado
    def update(self):

        self.contar_vulnerabilidade()
        if self.conferir_vida():
            self.morrer()
        
        
        if self.index < 17:

            self.index += 0.1     
            self.image = self.sprites[int(self.index)]

        # movimentar no eixo x
        self.velocidade += Global.velocidade_inimigo * 0.1
        self.rect.x -= int(Global.velocidade_inimigo * 0.1)
        self.velocidade -= int(Global.velocidade_inimigo * 0.1)
        
        # movimento no eixo y
        self.rect.y += numpy.cos(self.rect.x / 15)

        # mudar escala
        self.image = pygame.transform.scale(self.image, (largura_boss_01* 0.7 * Global.proporcao, altura_boss_01 * 0.7 * Global.proporcao))

boss_01 = SpritesBoss1(0, 0)