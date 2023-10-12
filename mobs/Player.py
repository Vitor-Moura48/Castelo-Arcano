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
        retangulo_ajustado = pygame.Rect.inflate(self.rect, -30, -10)
        self.rect = retangulo_ajustado

        self.rect.center = (int(largura_da_tela / 2), int(altura_da_tela / 2))

    # atualizar imagem
    def update(self):
        self.index_lista_mago += 10 / fps

        if self.index_lista_mago >= 8:
            self.index_lista_mago = 0

        self.image = self.sprites_mago[int(self.index_lista_mago)]

        self.image = pygame.transform.scale(self.image, (85 / 1.1, 94 / 1.1))

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > largura_da_tela:
            self.rect.right = largura_da_tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altura_da_tela:
            self.rect.bottom = altura_da_tela
            


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
        retangulo_ajustado = pygame.Rect.inflate(self.rect, -15, -15)
        self.rect = retangulo_ajustado
        

        self.tempo_de_vida = 120

        self.mask = pygame.mask.from_surface(self.image)

        # definir as coordenadas do projetil
        self.rect.center = (player.rect.center[0], player.rect.center[1])

        self.projetil_x = 0
        self.projetil_y = 0

    # lógica para atirar
    def atirar(self):

        # obtem as coordenadas do mouse
        posicao_mouse = mouse.get_pos()

        # obtem as diferencas entre o mouse e o projetil em cada eixo
        self.projetil_x = (posicao_mouse[0] - self.rect.center[0])
        self.projetil_y = (posicao_mouse[1] - self.rect.center[1])


        # armazena em uma variavel a 'mínima' parte da velocidade_projetil (de forma diretamente proporcional)
        distribuicao_velocidade = velocidade_base_projetil / (abs(self.projetil_x) + abs(self.projetil_y))

        # junta as 'mínimas partes' de forma diretamente proporcional a variavel self
        self.velocidade_x = distribuicao_velocidade * self.projetil_x
        self.velocidade_y = distribuicao_velocidade * self.projetil_y

    def update(self):
        self.tempo_de_vida -= 1

        # atualizar imagem
        self.index_lista_projetil += 10 / fps

        if self.index_lista_projetil >= 8:
            self.index_lista_projetil = 0

        self.image = self.sprites_projetil[int(self.index_lista_projetil)]


        # faz o projetil se mover de acordo com resultado da distribuição final obtida
        self.rect.left += self.velocidade_x
        self.rect.top += self.velocidade_y

        # define se o projetil saiu ou não da tela, se sim, a função update deixa de chamar essa função repetidamente
        if self.tempo_de_vida <= 0:
            Variaveis_globais.todas_as_sprites.remove(self)  


player = SpritesPlayer()

Variaveis_globais.todas_as_sprites.add(player)
projetil_player = Projetil()


