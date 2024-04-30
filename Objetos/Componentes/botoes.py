from Configurações.config import *
from Configurações  import Global


class Botao(pygame.sprite.Sprite):
    def __init__(self, caminho, *superficie, dimensoes, coordenada, texto=None, cor=None):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = pygame.image.load(os.path.join(caminho)).convert_alpha()
        self.imagem = self.sprite.subsurface(superficie)

        self.dimensoes = dimensoes
        self.texto = texto
        self.cor = cor

        self.image = self.imagem
        self.image = transform.scale(self.image, (dimensoes))

        self.rect = self.image.get_rect()
        self.rect.center = (coordenada)

        if self.texto != None:
            self.texto_para_tela = fonte.render(texto, True, cor)
            self.rect_texto = self.texto_para_tela.get_rect()
            self.rect_texto.center = self.rect.center
    
    def ajustar_posicoes(self, coodenada):
        self.rect.center = (coodenada)
        if self.texto != None:
            self.rect_texto.center = self.rect.center
    
    def update(self):
        self.image = transform.scale(self.image, (self.dimensoes))
        if self.texto != None:
            Global.tela.blit(self.texto_para_tela, (self.rect_texto))


class Botao_1(Botao):
    def __init__(self, texto, cor_texto, coordenada, dimensoes):
        Botao.__init__(self, 'imagens/botao.png', ((0,0), (332, 107)), dimensoes=dimensoes, coordenada=coordenada, texto=texto, cor=cor_texto)


class BotaoUpgrade(Botao):
    def __init__(self, coordenada, dimensoes, desbloqueado, linha_coluna):
        Botao.__init__(self, 'imagens/botoes.png', ((275,70), (50, 50)), dimensoes=dimensoes, coordenada=coordenada)
        
        #self.dimensoes = dimensoes
        self.linha_coluna = linha_coluna

        self.imagem2 = self.sprite.subsurface( ((75,70), (50, 50)) )   

        if desbloqueado == False:
            self.image = self.imagem
        else:
            self.image = self.imagem2
    
    def atualizar_informacoes(self):
        self.image = self.imagem2


class BotaoSom(Botao):
    def __init__(self, coordenada, dimensoes):
        Botao.__init__(self, 'imagens/icone_som.png', ((0,0), (499, 499)), dimensoes=dimensoes, coordenada=coordenada)


botao = Botao_1("teste", (255, 50, 50), (100, 100), (200, 50))