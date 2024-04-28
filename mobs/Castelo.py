from Configurações.config import *
from Configurações import Global

sprite_sheet_castelo = pygame.image.load(os.path.join('imagens/dark_castle.png')).convert_alpha()
rect_castelo = sprite_sheet_castelo.get_rect()
largura_castelo = rect_castelo.width
altura_castelo = rect_castelo.height

class SpriteCastelo(pygame.sprite.Sprite):  # criar classe de sprites para o cenário
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # carregar e colocar as imagens na lista de sprites
        self.sprites_castelo = []

        self.img_linha1_castelo = sprite_sheet_castelo.subsurface((0, 0), (largura_castelo, altura_castelo))
        self.sprites_castelo.append(self.img_linha1_castelo)

        # definir imagem que vai ser exibida
        self.image = self.sprites_castelo[0]

        # ajustar escala da imagem
        self.image = pygame.transform.scale(self.image, (largura_castelo * Global.proporcao * 0.65, altura_castelo * Global.proporcao * 0.65))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()
        self.rect_base = self.rect

    # atualizar estado
    def update(self):
        # ajustar escala da imagem
        self.image = pygame.transform.scale(self.image, (largura_castelo * Global.proporcao * 0.65, altura_castelo * Global.proporcao * 0.65))

        # posicionar o fundo da imagem na parte mais 'baixa' da tela
        self.rect.bottom = Global.dimensoes_janela[1]

        self.rect.left = 0

castelo = SpriteCastelo()
Global.todas_as_sprites.add(castelo)