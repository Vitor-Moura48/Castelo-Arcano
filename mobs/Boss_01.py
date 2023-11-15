from Configurações.config import *
from Configurações  import Variaveis_globais

sprite_sheet_boss_01 = pygame.image.load(os.path.join('imagens/boss_01.png')).convert_alpha()
rect_inimigo1 = sprite_sheet_boss_01.get_rect()
largura_boss_01 = rect_inimigo1.width
altura_boss_01 = rect_inimigo1.height

class SpritesBoss1(pygame.sprite.Sprite):  # criar classe de sprites para primeiro boss
    def __init__(self, HP, dano):
        pygame.sprite.Sprite.__init__(self)

        self.vida_restante = HP
        self.dano = dano

        self.contador_ivulnerabilidade = 0

        # caso a velocidade do boss seja muito lenta
        self.acumulador_velocidade = 0

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
        self.image = pygame.transform.scale(self.image, (largura_boss_01 * 0.7 * Variaveis_globais.proporcao, altura_boss_01 * 0.7 * Variaveis_globais.proporcao))
        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        novo_retangulo = pygame.Rect.inflate(self.rect, -10, -10)
        self.rect = novo_retangulo

        self.rect.right = Variaveis_globais.dimensoes_janela[0]
        self.rect.centery = Variaveis_globais.dimensoes_janela[1] / 2

    # atualizar estado
    def update(self):

        if self.vida_restante <= 0:
            self.kill()
            Variaveis_globais.inimigos_restantes -= 1
        
        if self.contador_ivulnerabilidade > 0:
            self.contador_ivulnerabilidade -= 1
        
        if self.index < 17:

            self.index += 0.1     
            self.image = self.sprites[int(self.index)]

        # movimentar no eixo x
        if int(Variaveis_globais.velocidade_inimigo * 0.1) == 0:
           
            self.acumulador_velocidade += Variaveis_globais.velocidade_inimigo * 0.1
            self.rect.x -= self.acumulador_velocidade
            if int(self.acumulador_velocidade) >= 1:
                
                self.acumulador_velocidade = 0
                   
        else:
            self.rect.x -= Variaveis_globais.velocidade_inimigo * 0.1
        
        # movimento no eixo y
        self.rect.y += numpy.cos(self.rect.x / 15)

        # mudar escala
        self.image = pygame.transform.scale(self.image, (largura_boss_01* 0.7 * Variaveis_globais.proporcao, altura_boss_01 * 0.7 * Variaveis_globais.proporcao))

boss_01 = SpritesBoss1(0, 0)