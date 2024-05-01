from Configurações.config import *
from Configurações  import Global
from Objetos import Animacoes


class Buff(pygame.sprite.Sprite):
    def __init__(self, caminho, *superficie):
        pygame.sprite.Sprite.__init__(self)
        Global.todas_as_sprites.add(self)
        Global.grupo_efeitos.add(self)


        self.sprite = pygame.image.load(os.path.join(caminho)).convert_alpha()

        # defina a imagem que vai ser exibida
        self.image = self.sprite.subsurface(superficie)

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.15 * Global.proporcao, 320 * 0.15 * Global.proporcao))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        # randomizar a posição que o buff vai ser spawnado
        self.randomizar()
    
    def randomizar(self):
        self.rect.left = randint(Global.dimensoes_janela[0], int(Global.dimensoes_janela[0] * 1.5))
        self.rect.top = randint(int(Global.dimensoes_janela[1] * 0.14), int(Global.dimensoes_janela[1] * 0.84))
    
    def ativar(self):
        self.buff()
        self.kill()
    
    # atualizar estado
    def update(self):

        # para movimentar o buff no eixo x
        self.rect.x -= Global.velocidade_inimigo * Global.proporcao

        # mudar dimensões da imagem
        self.image = pygame.transform.scale(self.image, (320 * 0.15 * Global.proporcao, 320 * 0.15 * Global.proporcao))

class SpritesEfeito1(Buff):  # classe para efeito especiail 1
    def __init__(self):
        Buff.__init__(self, 'dados/imagens/bolas de efeito.png', ( (0, 320), (320, 320) ) )

    # fução chamada quando o player colide com o buff
    def buff(self):
        arquivo_upgrade = pandas.read_csv("dados/csvs/upgrades.csv")

        if arquivo_upgrade.iloc[0, 0] == True:
            Global.tempo_buff_velocidade = 600
        else:
            Global.tempo_buff_velocidade = 300
        


class SpritesEfeito2(Buff):  # classe para efeito especiail 2
    def __init__(self):
        Buff.__init__( self, 'dados/imagens/bolas de efeito.png', ((640, 320), (320, 320)) )

    # quando o player colide com o buff, ganha um ponto de escudo
    def buff(self):

        arquivo_upgrade = pandas.read_csv("dados/csvs/upgrades.csv")

        if arquivo_upgrade.iloc[1, 0] == True:
            Global.barreira += 2
        else:
            Global.barreira += 1

        efeito_animacao = Animacoes.AnimacaoBarreira()
        Global.todas_as_sprites.add(efeito_animacao)


class SpritesEfeito3(Buff):  # classe para efeito especiail 3 (multti projeteis)
    def __init__(self):
        Buff.__init__( self, 'dados/imagens/bolas de efeito.png', ((320 * 2, 320 * 0), (320, 320)) )

    # quando o player colide com o buff, ganha um ponto de escudo
    def buff(self):

        arquivo_upgrade = pandas.read_csv("dados/csvs/upgrades.csv")

        if arquivo_upgrade.iloc[2, 0] == True:
            Global.tempo_buff_multiplos_disparos = 300
        else:
            Global.tempo_buff_multiplos_disparos = 600


class SpritesEfeito4(Buff):  # classe para efeito especiail 4 (velocidade de disparo)
    def __init__(self):
        Buff.__init__( self, 'dados/imagens/bolas de efeito.png', ((320 * 1, 320 * 0), (320, 320)) )

    # fução chamada quando o player colide com o buff
    def buff(self):

        arquivo_upgrade = pandas.read_csv("dados/csvs/upgrades.csv")

        if arquivo_upgrade.iloc[3, 0] == True:
            Global.tempo_buff_velocidade_disparo = 600
        else:
            Global.tempo_buff_velocidade_disparo = 300


class SpritesEfeito5(Buff):  # classe para efeito especiail 5 (disparo teleguiado)
    def __init__(self):
        Buff.__init__( self, 'dados/imagens/bolas de efeito.png', ((320 * 3, 320 * 1), (320, 320)) )

    # fução chamada quando o player colide com o buff
    def buff(self):

        arquivo_upgrade = pandas.read_csv("dados/csvs/upgrades.csv")

        if arquivo_upgrade.iloc[3, 0] == True:
            Global.tempo_buff_disparo_teleguiado = 600
        else:
            Global.tempo_buff_disparo_teleguiado = 300