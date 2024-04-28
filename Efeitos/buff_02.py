from Configurações.config import *
from Configurações  import Global
from Efeitos import animacoes

sprite_sheet_efeitos = pygame.image.load(os.path.join('imagens/bolas de efeito.png')).convert_alpha()
rect_efeitos = sprite_sheet_efeitos.get_rect()
largura_efeitos = rect_efeitos.width
altura_efeitos = rect_efeitos.height

class SpritesEfeito2(pygame.sprite.Sprite):  # classe para efeito especiail 2
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # define imagem que vai ser exibida
        self.image = sprite_sheet_efeitos.subsurface((640, 320), (320, 320))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.13 * Global.proporcao, 320 * 0.13 * Global.proporcao))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        # randomizar as coordenadas do spaw
        self.randomizar()

    def randomizar(self):

        self.rect.left = randint(Global.dimensoes_janela[0], Global.dimensoes_janela[0] + 500)
        self.rect.top = randint(int(Global.dimensoes_janela[1] * 0.14), int(Global.dimensoes_janela[1] * 0.84))

    # quando o player colide com o buff, ganha um ponto de escudo
    def buff(self):

        arquivo_upgrade = pandas.read_csv("csvs/upgrades.csv")

        if arquivo_upgrade.iloc[1, 0] == True:
            Global.barreira += 2
        else:
            Global.barreira += 1

        efeito_animacao = animacoes.EfeitosAnimacao()
        Global.todas_as_sprites.add(efeito_animacao)

    # atualizar estado
    def update(self):

        # movimentar buff no eixo x
        self.rect.x -= Global.velocidade_inimigo  * Global.proporcao

        # mudar escala do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.13 * Global.proporcao, 320 * 0.13 * Global.proporcao))


efeito_buff2 = SpritesEfeito2()
