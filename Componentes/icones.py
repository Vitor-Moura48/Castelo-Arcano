from Configurações.config import *
from Configurações  import Variaveis_globais

sprite_sheet_icone_background = pygame.image.load(os.path.join('imagens/icone_background.jpg')).convert_alpha()
rect_icone_background = sprite_sheet_icone_background.get_rect()
largura_icone_background = rect_icone_background.width
altura_icone_background = rect_icone_background.height

class IconeBackground(pygame.sprite.Sprite):
    def __init__(self, coodenada, dimensoes):
        pygame.sprite.Sprite.__init__(self)
        self.dimensoes = dimensoes

        self.image = sprite_sheet_icone_background.subsurface((0,0), (largura_icone_background, altura_icone_background))
        self.image = transform.scale(self.image, (dimensoes))

        self.rect = self.image.get_rect()
        self.rect.center = (coodenada)
       
    def update(self):
        self.image = transform.scale(self.image, (self.dimensoes))

icone_background = IconeBackground((0, 0), (0, 0))