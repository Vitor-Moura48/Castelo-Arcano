from Configurações import *
import Variaveis_globais

# carrega as imagem e obtem as dimensões dela
sprite_sheet_mago = pygame.image.load(os.path.join('imagens/mago.png')).convert_alpha()
rect_mago = sprite_sheet_mago.get_rect()
largura_mago = rect_mago.width
altura_mago = rect_mago.height

class SpritesPlayer(pygame.sprite.Sprite):  # criar classe de sprites para o jogador
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # carregar e colocar as imagens na lista de sprites do mago
        self.sprites_mago = []

        for frames in range(8):
            if frames < 4:
                self.img_linha1_mago = sprite_sheet_mago.subsurface((frames *  85, 0), (85, 94))
                self.sprites_mago.append(self.img_linha1_mago)
            if 4 <= frames < 8:
                self.img_linha2_mago = sprite_sheet_mago.subsurface(((frames - 4) * 85, 0), (85, 94))
                self.sprites_mago.append(self.img_linha2_mago)

        # definir a imagem que vai ser exibida
        self.index_lista_mago = 0
        self.image = self.sprites_mago[self.index_lista_mago]

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        self.rect.center = (Variaveis_globais.x_player, Variaveis_globais.y_player)

    # atualizar imagem
    def update(self):
        global x_player, y_player

        self.index_lista_mago += 10 / fps

        if self.index_lista_mago >= 8:
            self.index_lista_mago = 0

        self.image = self.sprites_mago[int(self.index_lista_mago)]

        self.image = pygame.transform.scale(self.image, (85 / 1.1, 94 / 1.1))

        self.rect.center = (Variaveis_globais.x_player, Variaveis_globais.y_player)

        if self.rect.left < 0:
            self.rect.left = 0
            x_player = self.rect.center[0]
        if self.rect.right > largura_da_tela:
            self.rect.right = largura_da_tela
            x_player = self.rect.center[0]

        if self.rect.top < 0:
            self.rect.top = 0
            y_player = self.rect.center[1]
        if self.rect.bottom > altura_da_tela:
            self.rect.bottom = altura_da_tela
            y_player = self.rect.center[1]
