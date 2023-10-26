from Configurações.config import *
from Configurações  import Variaveis_globais

sprite_sheet_botao = pygame.image.load(os.path.join('imagens/botao.png')).convert_alpha()
rect_botao = sprite_sheet_botao.get_rect()
largura_botao = rect_botao.width
altura_botao = rect_botao.height

class Botao(pygame.sprite.Sprite):
    def __init__(self, texto, cor_texto, coordenada_texto, coodenada, dimensoes):
        pygame.sprite.Sprite.__init__(self)
        self.dimensoes = dimensoes
        self.coordenada_texto = coordenada_texto

        self.image = sprite_sheet_botao.subsurface((0,0), (largura_botao, altura_botao))
        self.image = transform.scale(self.image, (dimensoes))

        self.rect = self.image.get_rect()
        self.rect.center = (coodenada)

        self.texto_para_tela = fonte.render(texto, True, cor_texto)
        
    
    def update(self):
        self.image = transform.scale(self.image, (self.dimensoes))
        Variaveis_globais.tela.blit(self.texto_para_tela, (self.coordenada_texto))


botao = Botao("teste", (255, 50, 50), (100, 100), (100, 100), (200, 50))