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

        self.rect_base = self.rect

        self.rect.center = (Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2)

    # atualizar imagem
    def update(self):
        self.index_lista_mago += 10 / fps

        if self.index_lista_mago >= 8:
            self.index_lista_mago = 0

        self.image = self.sprites_mago[int(self.index_lista_mago)]

        self.image = pygame.transform.scale(self.image, (85 * 0.8 * Variaveis_globais.proporcao, 94 * 0.8 * Variaveis_globais.proporcao))

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Variaveis_globais.dimensoes_janela[0]:
            self.rect.right = Variaveis_globais.dimensoes_janela[0]
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Variaveis_globais.dimensoes_janela[1]:
            self.rect.bottom = Variaveis_globais.dimensoes_janela[1]
            


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

        self.image = pygame.transform.scale(self.image, (int(50 * Variaveis_globais.proporcao), int(50 * Variaveis_globais.proporcao)))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()
        retangulo_ajustado = pygame.Rect.inflate(self.rect, -15, -15)
        self.rect = retangulo_ajustado
        

        self.tempo_de_vida = 120

        # definir as coordenadas do projetil
        self.rect.center = (player.rect.center[0], player.rect.center[1])

        self.projetil_x = 0
        self.projetil_y = 0

    # lógica para atirar
    def atirar(self, desvio):

        # obtem as coordenadas do mouse
        posicao_mouse = mouse.get_pos()

        distancia_x = posicao_mouse[0] - self.rect.center[0]
        distancia_y = posicao_mouse[1] - self.rect.center[1]

        angulo_radiano = numpy.arctan2(distancia_y, distancia_x) + numpy.radians(desvio)

        # junta as 'mínimas partes' de forma diretamente proporcional a variavel self
        self.velocidade_x = numpy.cos(angulo_radiano) * velocidade_base_projetil * Variaveis_globais.proporcao
        self.velocidade_y = numpy.sin(angulo_radiano) * velocidade_base_projetil * Variaveis_globais.proporcao

    def update(self):

        self.tempo_de_vida -= 1

        # atualizar imagem
        self.index_lista_projetil += 10 / fps

        if self.index_lista_projetil >= 8:
            self.index_lista_projetil = 0

        self.image = self.sprites_projetil[int(self.index_lista_projetil)]
        self.image = pygame.transform.scale(self.image, (int(50 * Variaveis_globais.proporcao), int(50 * Variaveis_globais.proporcao)))


        # faz o projetil se mover de acordo com resultado da distribuição final obtida
        self.rect.left += self.velocidade_x
        self.rect.top += self.velocidade_y

        # define se o projetil saiu ou não da tela, se sim, a função update deixa de chamar essa função repetidamente
        if self.tempo_de_vida <= 0:
            self.kill() 
        


player = SpritesPlayer()

Variaveis_globais.todas_as_sprites.add(player)
projetil_player = Projetil()


