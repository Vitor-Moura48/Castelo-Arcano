from Configurações.config import *
from Configurações  import Variaveis_globais

sprite_sheet_efeitos = pygame.image.load(os.path.join('imagens/bolas de efeito.png')).convert_alpha()
rect_efeitos = sprite_sheet_efeitos.get_rect()
largura_efeitos = rect_efeitos.width
altura_efeitos = rect_efeitos.height

class SpritesEfeito1(pygame.sprite.Sprite):  # classe para efeito especiail 1
    def __init__(self):
   
        pygame.sprite.Sprite.__init__(self)

        # defina a imagem que vai ser exibida
        self.image = sprite_sheet_efeitos.subsurface((0, 320), (320, 320))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.15 * Variaveis_globais.proporcao, 320 * 0.15 * Variaveis_globais.proporcao))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        # randomizar a posição que o buff vai ser spawnado
        self.randomizar()

    def randomizar(self):

        self.rect.left = randint(Variaveis_globais.dimensoes_janela[0], int(Variaveis_globais.dimensoes_janela[0] * 1.5))
        self.rect.top = randint(int(Variaveis_globais.dimensoes_janela[1] * 0.14), int(Variaveis_globais.dimensoes_janela[1] * 0.84))

    # fução chamada quando o player colide com o buff
    def buff(self):
        arquivo_upgrade = pandas.read_csv("csvs/upgrades.csv")

        if arquivo_upgrade.iloc[0, 0] == True:
            Variaveis_globais.tempo_buff_velocidade = 600
        else:
            Variaveis_globais.tempo_buff_velocidade = 300

    # atualizar estado
    def update(self):

        # para movimentar o buff no eixo x
        self.rect.x -= Variaveis_globais.velocidade_inimigo * Variaveis_globais.proporcao

        # mudar dimensões da imagem
        self.image = pygame.transform.scale(self.image, (320 * 0.15 * Variaveis_globais.proporcao, 320 * 0.15 * Variaveis_globais.proporcao))


efeito_buff1 = SpritesEfeito1()

