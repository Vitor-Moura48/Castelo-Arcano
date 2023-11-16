from Configurações.config import *
from Configurações  import Variaveis_globais

sprite_sheet_botao = pygame.image.load(os.path.join('imagens/botao.png')).convert_alpha()
rect_botao = sprite_sheet_botao.get_rect()
largura_botao = rect_botao.width
altura_botao = rect_botao.height

sprite_sheet_botoes = pygame.image.load(os.path.join('imagens/botoes.png')).convert_alpha()

class Botao(pygame.sprite.Sprite):
    def __init__(self, texto, cor_texto, coodenada, dimensoes):
        pygame.sprite.Sprite.__init__(self)

        self.dimensoes = dimensoes

        self.image = sprite_sheet_botao.subsurface((0,0), (largura_botao, altura_botao))
        self.image = transform.scale(self.image, (dimensoes))

        self.rect = self.image.get_rect()
        self.rect.center = (coodenada)

        self.texto_para_tela = fonte.render(texto, True, cor_texto)
        self.rect_texto = self.texto_para_tela.get_rect()
        self.rect_texto.center = self.rect.center
    
    def ajustar_posicoes(self, coodenada, dimensoes):
        self.rect.center = (coodenada)
        self.rect_texto.center = self.rect.center
    
    def update(self):
        self.image = transform.scale(self.image, (self.dimensoes))
        Variaveis_globais.tela.blit(self.texto_para_tela, (self.rect_texto))


class BotaoUpgrade(pygame.sprite.Sprite):
    def __init__(self, coodenada, dimensoes, desbloqueado, linha_coluna):
        pygame.sprite.Sprite.__init__(self)

        self.dimensoes = dimensoes
        self.linha_coluna = linha_coluna

        self.imagem_bloqueada = sprite_sheet_botoes.subsurface((275,70), (50, 50))
        self.imagem_liberada = sprite_sheet_botoes.subsurface((75,70), (50, 50))

        if desbloqueado == False:
            self.image = self.imagem_bloqueada
        else:
           self.image = self.imagem_liberada
        
        self.image = transform.scale(self.image, (dimensoes))

        self.rect = self.image.get_rect()
        self.rect.center = (coodenada)

    def ajustar_posicoes(self, coodenada, dimensoes):
        self.rect.center = (coodenada)
    
    def atualizar_informacoes(self):
        self.image = self.imagem_liberada
    
    def update(self):
        self.image = transform.scale(self.image, (self.dimensoes))


sprite_sheet_botao_som = pygame.image.load(os.path.join('imagens/icone_som.png')).convert_alpha()
rect_botao_som = sprite_sheet_botao_som.get_rect()
largura_botao_som = rect_botao_som.width
altura_botao_som = rect_botao_som.height

class BotaoSom(pygame.sprite.Sprite):
    def __init__(self, coodenada, dimensoes):
        pygame.sprite.Sprite.__init__(self)

        self.dimensoes = dimensoes

        self.image = sprite_sheet_botao_som.subsurface((0,0), (largura_botao_som, altura_botao_som))
        self.image = transform.scale(self.image, (dimensoes))

        self.rect = self.image.get_rect()
        self.rect.center = (coodenada)

    def ajustar_posicoes(self, coodenada, dimensoes):
        self.rect.center = (coodenada)

    def update(self):
        self.image = transform.scale(self.image, (self.dimensoes))

botao = Botao("teste", (255, 50, 50), (100, 100), (200, 50))