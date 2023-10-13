from Configurações.config import *
from Configurações import Variaveis_globais



sprite_sheet_castelo = pygame.image.load(os.path.join('imagens/dark_castle.png')).convert_alpha()
rect_castelo = sprite_sheet_castelo.get_rect()
largura_castelo = rect_castelo.width
altura_castelo = rect_castelo.height


class SpritesCenario(pygame.sprite.Sprite):  # criar classe de sprites para o cenário
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # carregar e colocar as imagens na lista de sprites
        self.sprites_castelo = []

        self.img_linha1_castelo = sprite_sheet_castelo.subsurface((0, 0), (largura_castelo, altura_castelo))
        self.sprites_castelo.append(self.img_linha1_castelo)

        # definir imagem que vai ser exibida
        self.image = self.sprites_castelo[0]

        # ajustar escala da imagem
        self.image = pygame.transform.scale(self.image, (largura_castelo * Variaveis_globais.proporcao * 0.65, altura_castelo * Variaveis_globais.proporcao * 0.65))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

    # atualizar estado
    def update(self):
        # ajustar escala da imagem
        self.image = pygame.transform.scale(self.image, (largura_castelo * Variaveis_globais.proporcao * 0.65, altura_castelo * Variaveis_globais.proporcao * 0.65))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        # posicionar o fundo da imagem na parte mais 'baixa' da tela
        self.rect.bottom = pygame.display.get_surface().get_size()[1]



castelo = SpritesCenario()
Variaveis_globais.todas_as_sprites.add(castelo)