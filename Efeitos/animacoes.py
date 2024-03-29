from Configurações.config import *
from Configurações import Variaveis_globais
from mobs import Castelo

sprite_sheet_barreira = pygame.image.load(os.path.join('imagens/efeito barreira.png')).convert_alpha()
rect_barreira = sprite_sheet_barreira.get_rect()
largura_barreirra = rect_barreira.width
altura_barreira = rect_barreira.height

class EfeitosAnimacao(pygame.sprite.Sprite):  # classe de efeitos diversos que acontecem as vezes
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # carregar e colocar as imagens na lista de sprites
        self.sprites_efeito_barreira = []

        for frame in range(6):
            self.img_linha2 = sprite_sheet_barreira.subsurface((frame * 102, 100), (102, 245))
            self.sprites_efeito_barreira.append(self.img_linha2)

        # definir imagem que vai ser exibida
        self.index_barreira = 0
        self.image = self.sprites_efeito_barreira[self.index_barreira]

        #  mudar dimensões da imagem
        self.image = pygame.transform.scale(self.image, (102 * 3.5 * Variaveis_globais.proporcao, 308 * 3.5 * Variaveis_globais.proporcao))

        # encontrar as dimensoes da imagem
        self.rect = self.image.get_rect()

        # posicionar sprite
        self.rect.centerx = Castelo.castelo.rect.centerx
        self.rect.bottom = Variaveis_globais.dimensoes_janela[1]

    # atualizar estado
    def update(self):

        # condição para executar animação
        if self.index_barreira < 6:
            
            # atualizar imagem
            self.image = self.sprites_efeito_barreira[int(self.index_barreira)]   
            self.index_barreira += 0.1

            # ajustar dimensões do sprite
            self.image = pygame.transform.scale(self.image, (102 * 3.5 * Variaveis_globais.proporcao, 308 * 3.5 * Variaveis_globais.proporcao))
        else:
            self.kill()


        

