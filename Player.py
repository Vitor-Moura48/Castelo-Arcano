from Configurações.config import *
from Configurações import Variaveis_globais


# carrega as imagem e obtem as dimensões dela
sprite_sheet_mago = pygame.image.load(os.path.join('imagens/mago.png')).convert_alpha()
rect_mago = sprite_sheet_mago.get_rect()
largura_mago = rect_mago.width
altura_mago = rect_mago.height


sprite_sheet_projeteis = pygame.image.load(os.path.join('imagens/Projeteis.png')).convert_alpha()
rect_projeteis = sprite_sheet_projeteis.get_rect()
largura_projeteis = rect_projeteis.width
altura_projeteis = rect_projeteis.height



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


class Projetil(pygame.sprite.Sprite):  # criar classe para projetil do player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # carregar e colocar as imagens na lista de sprites do projetil
        self.sprites_projetil = []

        for frame in range(8):

            self.img_linha9_projetil = sprite_sheet_projeteis.subsurface((215, 310), (50, 50))
            self.sprites_projetil.append(self.img_linha9_projetil)

        # definir a imagem que vai ser exibida
        self.index_lista_projetil = 0
        self.index_lista_projetil += 1
        self.image = self.sprites_projetil[int(self.index_lista_projetil)]

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # definir as coordenadas do projetil
        self.rect.center = (Variaveis_globais.x_player - 12, Variaveis_globais.y_player - 7)

        # para disparar projetil
        self.clicou = False
        self.contador = 0

        self.projetil_x = 0
        self.projetil_y = 0

    # lógica para atirar
    def atirar(self):

        # obtem as coordenadas do mouse
        posicao_mouse = mouse.get_pos()

        # obtem as diferencas entre o mouse e o projetil em cada eixo
        if self.contador == 0:
            self.projetil_x = (posicao_mouse[0] - self.rect.center[0])
            self.projetil_y = (posicao_mouse[1] - self.rect.center[1])
            self.contador += 1

        # armazena em uma variavel a 'mínima' parte da velocidade_projetil (de forma diretamente proporcional)
        distribuicao_velocidade = velocidade_projetil / (abs(self.projetil_x) + abs(self.projetil_y))

        # junta as 'mínimas partes' de forma diretamente proporcional a variavel self
        velocidade_x = distribuicao_velocidade * self.projetil_x
        velocidade_y = distribuicao_velocidade * self.projetil_y

        # faz o projetil se mover de acordo com resultado da distribuição final obtida
        self.rect.left += velocidade_x
        self.rect.top += velocidade_y

        # define se o projetil saiu ou não da tela, se sim, a função update deixa de chamar essa função repetidamente
        if self.rect.right > 1500 or self.rect.left < 0 or self.rect.top > 500 or self.rect.bottom < 0:
            self.clicou = False

    def update(self):

        # atualizar imagem
        self.index_lista_projetil += 10 / fps

        if self.index_lista_projetil >= 8:
            self.index_lista_projetil = 0

        self.image = self.sprites_projetil[int(self.index_lista_projetil)]

        # confere se o jogador clicou para disparar
        if self.clicou:
            self.atirar()
        # senão o projetil vai ficar "atrás" do mago (jogador)
        else:
            self.rect.center = (Variaveis_globais.x_player - 12, Variaveis_globais.y_player - 7)
            self.contador = 0




projetil_player = Projetil()
Variaveis_globais.todas_as_sprites.add(projetil_player)

player = SpritesPlayer()
Variaveis_globais.todas_as_sprites.add(player)