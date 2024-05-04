from Configurações.config import *
from Configurações  import Global


class Botao(pygame.sprite.Sprite):
    def __init__(self, caminho, *superficie, dimensoes, coordenada, texto=None, cor=None):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = pygame.image.load(os.path.join(caminho)).convert_alpha()
        self.imagem = self.sprite.subsurface(superficie)

        self.dimensoes = dimensoes
        self.coordenada = coordenada
        self.texto = texto
        self.cor = cor

        self.ajustar_posicoes()
    
    def ajustar_posicoes(self):
        self.image = self.imagem
        self.image = transform.scale( self.image, (int(self.dimensoes[0] * Global.proporcao), int(self.dimensoes[1] * Global.proporcao)) ) 
        self.rect = self.image.get_rect()
        self.rect.center = ( int(Global.dimensoes_janela[0] * self.coordenada[0]), int(Global.dimensoes_janela[1] * self.coordenada[1]) )

        if self.texto != None:
            self.texto_para_tela = pygame.font.SysFont("arial", int(30 * Global.proporcao), True, False).render(self.texto, True, self.cor)
            self.rect_texto = self.texto_para_tela.get_rect()
            self.rect_texto.center = self.rect.center
    
    def update(self):
        if self.texto != None:
            Global.tela.blit(self.texto_para_tela, (self.rect_texto))


class Botao_1(Botao):
    def __init__(self, texto, cor_texto, coordenada, dimensoes):
        Botao.__init__(self, 'dados/imagens/botao.png', ((0,0), (332, 107)), dimensoes=dimensoes, coordenada=coordenada, texto=texto, cor=cor_texto)


class BotaoUpgrade(Botao):
    def __init__(self, coordenada, dimensoes, desbloqueado, linha_coluna):
        Botao.__init__(self, 'dados/imagens/botoes.png', ((275,70), (50, 50)), dimensoes=dimensoes, coordenada=coordenada)

        self.linha_coluna = linha_coluna

        self.imagem2 = self.sprite.subsurface( ((75,70), (50, 50)) )    # verde
        self.imagem = self.imagem2 if desbloqueado else self.imagem

        self.ajustar_posicoes() 
    
    def atualizar_informacoes(self):
        self.image = self.imagem2


class BotaoSom(Botao):
    def __init__(self, coordenada, dimensoes):
        Botao.__init__(self, 'dados/imagens/icone_som.png', ((0,0), (499, 499)), dimensoes=dimensoes, coordenada=coordenada)

