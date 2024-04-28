from Configurações.config import *
from Configurações  import Global

sprite_sheet_efeitos = pygame.image.load(os.path.join('imagens/bolas de efeito.png')).convert_alpha()
rect_efeitos = sprite_sheet_efeitos.get_rect()
largura_efeitos = rect_efeitos.width
altura_efeitos = rect_efeitos.height

class SpritesEfeito5(pygame.sprite.Sprite):  # classe para efeito especiail 5 (disparo teleguiado)
    def __init__(self):
   
        pygame.sprite.Sprite.__init__(self)

        # defina a imagem que vai ser exibida
        self.image = sprite_sheet_efeitos.subsurface((320 * 3, 320 * 1), (320, 320))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.15 * Global.proporcao, 320 * 0.15 * Global.proporcao))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        # randomizar a posição que o buff vai ser spawnado
        self.randomizar()

    def randomizar(self):

        self.rect.left = randint(Global.dimensoes_janela[0], int(Global.dimensoes_janela[0] * 1.5))
        self.rect.top = randint(int(Global.dimensoes_janela[1] * 0.14), int(Global.dimensoes_janela[1] * 0.84))

    # fução chamada quando o player colide com o buff
    def buff(self):

        arquivo_upgrade = pandas.read_csv("csvs/upgrades.csv")

        if arquivo_upgrade.iloc[3, 0] == True:
            Global.tempo_buff_disparo_teleguiado = 600
        else:
            Global.tempo_buff_disparo_teleguiado = 300

    # atualizar estado
    def update(self):
        # mudar dimensões da imagem
        self.image = pygame.transform.scale(self.image, (320 * 0.15 * Global.proporcao, 320 * 0.15 * Global.proporcao))

        # para movimentar o buff no eixo x
        self.rect.x -= Global.velocidade_inimigo * Global.proporcao

        
efeito_buff5 = SpritesEfeito5()

