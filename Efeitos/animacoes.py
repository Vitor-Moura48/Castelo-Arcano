from Configurações.config import *
from Configurações import Variaveis_globais



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
            self.img_linha2 = sprite_sheet_barreira.subsurface((frame * 102, 100), (102, 308))
            self.sprites_efeito_barreira.append(self.img_linha2)

        # definir imagem que vai ser exibida
        self.index_barreira = 0
        self.image = self.sprites_efeito_barreira[self.index_barreira]

        #  mudar dimensões da imagem
        self.image = pygame.transform.scale(self.image, (102 * 4, 308 * 4))

        # encontrar as dimensoes da imagem
        self.rect = self.image.get_rect()

        # posicionar sprite
        self.rect.left = 75
        self.rect.bottom = altura_da_tela

        # variavel para ajudar na execução do efeito de animação
        self.ativar = False

    def animar1(self):
        self.ativar = True

    # atualizar estado
    def update(self):

        # condição para executar animação
        if self.ativar:
            

            self.index_barreira += 10 / fps

            self.rect.center = (125, 215)
            
           
            # manter loop de animação
            if self.index_barreira >= 6:
                self.index_barreira = 0
                self.ativar = False

            # atualizar imagem
            self.image = self.sprites_efeito_barreira[int(self.index_barreira)]

            # ajustar dimensões do sprite
            self.image = pygame.transform.scale(self.image, (102 * 4, 308 * 4))
        else:
            Variaveis_globais.todas_as_sprites.remove(self)


        

