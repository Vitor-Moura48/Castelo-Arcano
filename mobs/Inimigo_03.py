from Configurações.config import *
from Configurações  import Variaveis_globais
from mobs import Castelo

sprite_sheet_inimigo_03 = pygame.image.load(os.path.join('imagens/inimigo3.png'))
rect_inimigo_03 = sprite_sheet_inimigo_03.get_rect()
largura_inimigo_03 = rect_inimigo_03.width
altura_inimigo_03 = rect_inimigo_03.height

sprite_sheet_projetil_inimigo_03 = pygame.image.load(os.path.join('imagens/projetil_inimigo3.png'))
rect_projetil_inimigo_03 = sprite_sheet_projetil_inimigo_03.get_rect()
largura_projetil_inimigo_03 = rect_projetil_inimigo_03.width
altura_projetil_inimigo_03 = rect_projetil_inimigo_03.height

class SpritesInimigo3(pygame.sprite.Sprite):  # criar classe de sprites para os inimigos 3
    def __init__(self, HP):
        pygame.sprite.Sprite.__init__(self)

        self.vida_restante = HP

        self.recarga_disparos = 150

        # seleciona a sprite que vai ser exibida
        self.sprites = []

        for linha in range(3):
            for coluna in range(4):
                self.sprites.append(sprite_sheet_inimigo_03.subsurface((45 * coluna, 51 * linha), (45, 51)))
        
        self.index = 0
        self.image = self.sprites[self.index]

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (largura_inimigo_03 * 0.5 * Variaveis_globais.proporcao, altura_inimigo_03 * 0.5 * Variaveis_globais.proporcao))
        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        # randomiza as coordenadas que o inimigo vai spawnar
        self.randomizar()

    def randomizar(self):

        self.rect.x = randint(Variaveis_globais.dimensoes_janela[0], Variaveis_globais.dimensoes_janela[0] + 1000)
        self.rect.y = randint(int(Variaveis_globais.dimensoes_janela[1] * 0.1), int(Variaveis_globais.dimensoes_janela[1] - self.rect.size[1]))
     
    def atirar(self):
        projetil_inimigo_03 = ProjetilInimigo(self.rect.center)
        Variaveis_globais.grupo_projeteis_inimigos.add(projetil_inimigo_03)
        Variaveis_globais.todas_as_sprites.add(projetil_inimigo_03)
        projetil_inimigo_03.atirar()

        self.recarga_disparos = 180

    # atualizar estado
    def update(self):
        self.recarga_disparos -= 1

        if self.vida_restante <= 0:
            if self.index < 11:

                self.index += 0.1     
                self.image = self.sprites[int(self.index)]
                self.image = pygame.transform.scale(self.image, (largura_inimigo_03 * 0.5 * Variaveis_globais.proporcao, altura_inimigo_03 * 0.5 * Variaveis_globais.proporcao))

            else:
                self.kill()
                Variaveis_globais.inimigos_restantes -= 1

        else:
            # mudar escala
            self.image = pygame.transform.scale(self.image, (largura_inimigo_03 * 0.5 * Variaveis_globais.proporcao, altura_inimigo_03 * 0.5 * Variaveis_globais.proporcao))

            # ajusta as dimensoes do retangulo
            self.posicao_atual_rect = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = self.posicao_atual_rect

            # movimentar no eixo x
            if self.rect.right > Variaveis_globais.dimensoes_janela[0] * 0.9:
                self.rect.x -= Variaveis_globais.velocidade_inimigo * 0.5
            # quando chegar a uma certa distancia, para no eixo x e passa a desviar do projeteis
            else:
                projetil_mais_proximo = None

                for projeil in Variaveis_globais.grupo_projeteis_aliados:

                    distancia_x = projeil.rect.center[0] - self.rect.center[0]
                    distancia_y = projeil.rect.center[1] - self.rect.center[1]
                    distancia_absoluta = (abs(distancia_x) ** 2 + abs(distancia_y) ** 2) ** 0.5

                    if projetil_mais_proximo == None or distancia_absoluta < projetil_mais_proximo[1]:
                        projetil_mais_proximo = [projeil, distancia_absoluta, distancia_x, distancia_y]
                
                if projetil_mais_proximo != None and projetil_mais_proximo[1] < 900:
                    
                    if projetil_mais_proximo[0].rect.centery < Variaveis_globais.dimensoes_janela[1] / 2:
                        self.rect.y += Variaveis_globais.velocidade_inimigo * 1.5
                    else:
                        self.rect.y -= Variaveis_globais.velocidade_inimigo * 1.5
                  
                # confere se é possível disparar algum projetil
                if self.recarga_disparos <= 0:
                    self.atirar()
            
            # define os limites de movimentação
            if self.rect.top < Variaveis_globais.dimensoes_janela[1] * 0.1:
                self.rect.top = Variaveis_globais.dimensoes_janela[1] * 0.1

            if self.rect.bottom > Variaveis_globais.dimensoes_janela[1]:
                self.rect.bottom = Variaveis_globais.dimensoes_janela[1]


class ProjetilInimigo(pygame.sprite.Sprite):  # criar classe para projetil do inimigo 3
    def __init__(self, centro_de_origem):
        pygame.sprite.Sprite.__init__(self)

        # carregar e colocar as imagens na lista de sprites do projetil
        self.sprites_projetil = []

        for sprite in range(4):
            self.sprites_projetil.append(sprite_sheet_projetil_inimigo_03.subsurface((32 * sprite, 0), (32, 32)))

        # definir a imagem que vai ser exibida
        self.index_projetil_inimigo = 0
        self.image = self.sprites_projetil[int(self.index_projetil_inimigo)]

        self.image = pygame.transform.scale(self.image, (int(32 * Variaveis_globais.proporcao), int(32 * Variaveis_globais.proporcao)))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()
        retangulo_ajustado = pygame.Rect.inflate(self.rect, -(32 * 0.3), -(32 * 0.3))
        self.rect = retangulo_ajustado

        self.tempo_de_vida = 400

        # definir as coordenadas do projetil
        self.rect.center = (centro_de_origem[0], centro_de_origem[1])

        self.acumulador_velocidade_x = 0
        self.acumulador_velocidade_y = 0

    def atirar(self):
        # obtem as coordenadas do mouse
        posicao_castelo = Castelo.castelo.rect.center

        distancia_x = posicao_castelo[0] - self.rect.center[0]
        distancia_y = posicao_castelo[1] - self.rect.center[1]
        
        # calcula o angulo em radiano do click em relação ao player
        desvio = uniform(-15, 15)

        angulo_radiano = numpy.arctan2(distancia_y, distancia_x) + numpy.radians(desvio)
      
        # distribui a velocidade a partir do seno e cosseno
        self.velocidade_x = numpy.cos(angulo_radiano) * velocidade_base_projetil * Variaveis_globais.proporcao * 0.15
        self.velocidade_y = numpy.sin(angulo_radiano) * velocidade_base_projetil * Variaveis_globais.proporcao * 0.15

        self.angulo_graus_desvio = numpy.degrees(angulo_radiano) + desvio

    def update(self):
        self.image = self.sprites_projetil[int(self.index_projetil_inimigo)]
        self.image = pygame.transform.scale(self.image, (int(32 * Variaveis_globais.proporcao), int(32 * Variaveis_globais.proporcao)))

        self.image = pygame.transform.rotate(self.image, 90 - self.angulo_graus_desvio)
    
        self.tempo_de_vida -= 1

        # ajusta as dimensoes do retangulo
        self.posicao_atual_rect = self.rect.center
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.inflate(self.rect, -(32 * 0.3), -(32 * 0.3))
        self.rect.center = self.posicao_atual_rect

        if self.index_projetil_inimigo < 3:

            self.index_projetil_inimigo += 0.1     

        else:
            self.index_projetil_inimigo = 0

        # faz o projetil se mover de acordo com resultado da distribuição final obtida
        self.acumulador_velocidade_x += self.velocidade_x
        self.acumulador_velocidade_y += self.velocidade_y

        if self.acumulador_velocidade_x >= 1:
            self.rect.x += self.acumulador_velocidade_x
            self.acumulador_velocidade_x -= round(self.acumulador_velocidade_x)

        elif self.acumulador_velocidade_x <= -1:
            self.rect.x += self.acumulador_velocidade_x
            self.acumulador_velocidade_x -= round(self.acumulador_velocidade_x)

        if self.acumulador_velocidade_y >= 1:
            self.rect.y += self.acumulador_velocidade_y
            self.acumulador_velocidade_y -= round(self.acumulador_velocidade_y)

        elif self.acumulador_velocidade_y <= -1:
            self.rect.y += self.acumulador_velocidade_y
            self.acumulador_velocidade_y -= round(self.acumulador_velocidade_y)

        # define se o projetil saiu ou não da tela, se sim, a função update deixa de chamar essa função repetidamente
        if self.tempo_de_vida <= 0:
            self.kill() 
        
        
        