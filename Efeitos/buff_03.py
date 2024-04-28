from Configurações.config import *
from Configurações  import Global

sprite_sheet_efeitos = pygame.image.load(os.path.join('imagens/bolas de efeito.png')).convert_alpha()
rect_efeitos = sprite_sheet_efeitos.get_rect()
largura_efeitos = rect_efeitos.width
altura_efeitos = rect_efeitos.height

class SpritesEfeito3(pygame.sprite.Sprite):  # classe para efeito especiail 3 (multti projeteis)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # define imagem que vai ser exibida
        self.image = sprite_sheet_efeitos.subsurface((320 * 2, 320 * 0), (320, 320))

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

        if arquivo_upgrade.iloc[2, 0] == True:
            Global.tempo_buff_3_projeteis = 300
        else:
            Global.tempo_buff_3_projeteis = 600

    # atualizar estado
    def update(self):

        # movimentar buff no eixo x
        self.rect.x -= Global.velocidade_inimigo  * Global.proporcao

        # mudar escala do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.13 * Global.proporcao, 320 * 0.13 * Global.proporcao))


efeito_buff3 = SpritesEfeito3()
