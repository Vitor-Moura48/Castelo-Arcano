from Configurações.config import *
from Configurações import Global

class Icone(pygame.sprite.Sprite):
    def __init__(self, caminho, superficie, coordenada, dimensoes):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = pygame.image.load(os.path.join(caminho)).convert_alpha()
        self.imagem = self.sprite.subsurface(superficie)

        self.superficie = superficie
        self.coordenada = coordenada
        self.dimensoes = dimensoes

        self.ajustar_posicoes()

    def ajustar_posicoes(self):
        self.image = self.imagem.subsurface(self.superficie)
        self.image = transform.scale(self.image, (int(self.dimensoes[0] * Global.proporcao), int(self.dimensoes[1] * Global.proporcao)))
        self.rect = self.image.get_rect()
        self.rect.center = ( int(Global.dimensoes_janela[0] * self.coordenada[0]), int(Global.dimensoes_janela[1] * self.coordenada[1]) )

class IconeBackground(Icone):
    def __init__(self, coordenada, dimensoes):
        Icone.__init__(self, caminho='dados/imagens/icone_background.jpg', superficie=((0,0), (408, 612)), coordenada=coordenada, dimensoes=dimensoes)
    
    
        