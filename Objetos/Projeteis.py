from Configurações.config import pygame, os, numpy, uniform, velocidade_base_projetil, mouse
from Configurações import Global
from Objetos import Mobs

sprite_sheet_projetil_inimigo_03 = pygame.image.load(os.path.join('imagens/projetil_inimigo3.png'))
rect_projetil_inimigo_03 = sprite_sheet_projetil_inimigo_03.get_rect()
largura_projetil_inimigo_03 = rect_projetil_inimigo_03.width
altura_projetil_inimigo_03 = rect_projetil_inimigo_03.height

class ProjetilInimigo(pygame.sprite.Sprite):  # criar classe para projetil do inimigo 3
    def __init__(self, centro_de_origem, perfuracao, dano):
        pygame.sprite.Sprite.__init__(self)

        self.perfuracoes_restantes = perfuracao
        self.dano = dano

        # carregar e colocar as imagens na lista de sprites do projetil
        self.sprites_projetil = []

        for sprite in range(4):
            self.sprites_projetil.append(sprite_sheet_projetil_inimigo_03.subsurface((32 * sprite, 0), (32, 32)))

        # definir a imagem que vai ser exibida
        self.index_projetil_inimigo = 0
        self.image = self.sprites_projetil[int(self.index_projetil_inimigo)]

        self.image = pygame.transform.scale(self.image, (int(32 * Global.proporcao), int(32 * Global.proporcao)))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()
        retangulo_ajustado = pygame.Rect.inflate(self.rect, -(32 * 0.3), -(32 * 0.3))
        self.rect = retangulo_ajustado

        self.tempo_de_vida = 400

        # definir as coordenadas do projetil
        self.rect.center = (centro_de_origem[0], centro_de_origem[1])

        self.velocidade_x = 0
        self.velocidade_y = 0

    def atirar(self):
        # obtem as coordenadas do mouse
        posicao_castelo = Mobs.castelo.rect.center

        distancia_x = posicao_castelo[0] - self.rect.center[0]
        distancia_y = posicao_castelo[1] - self.rect.center[1]
        
        # calcula o angulo em radiano do click em relação ao player
        desvio = uniform(-15, 15)
        angulo_radiano = numpy.arctan2(distancia_y, distancia_x) + numpy.radians(desvio)
      
        # distribui a velocidade a partir do seno e cosseno
        self.eixo_x = numpy.cos(angulo_radiano) * velocidade_base_projetil * Global.proporcao * 0.15
        self.eixo_y = numpy.sin(angulo_radiano) * velocidade_base_projetil * Global.proporcao * 0.15

        self.angulo_graus_desvio = numpy.degrees(angulo_radiano) + desvio
    
    def update(self):

        if self.perfuracoes_restantes <= 0:
            self.kill()
        if self.tempo_de_vida <= 0:
            self.kill() 

        self.image = self.sprites_projetil[int(self.index_projetil_inimigo)]
        self.image = pygame.transform.scale(self.image, (int(32 * Global.proporcao), int(32 * Global.proporcao)))

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
        self.velocidade_x += self.eixo_x
        self.velocidade_y += self.eixo_y

        if abs(self.velocidade_x) >= 1:
            self.rect.x += self.velocidade_x
            self.velocidade_x -= int(self.velocidade_x)
        if abs(self.velocidade_y) >= 1:
            self.rect.y += self.velocidade_y
            self.velocidade_y -= int(self.velocidade_y)

        
sprite_sheet_projeteis = pygame.image.load(os.path.join('imagens/Projeteis.png')).convert_alpha()
rect_projeteis = sprite_sheet_projeteis.get_rect()
largura_projeteis = rect_projeteis.width
altura_projeteis = rect_projeteis.height

class Projetil(pygame.sprite.Sprite):  # criar classe para projetil do player
    def __init__(self, perfuracao, dano):
        pygame.sprite.Sprite.__init__(self)

        self.perfuracoes_restantes = perfuracao
        self.dano = dano

        # carregar e colocar as imagens na lista de sprites do projetil
        self.sprites_projetil = []

        for frame in range(8):

            self.img_linha9_projetil = sprite_sheet_projeteis.subsurface((215, 310), (50, 50))
            self.sprites_projetil.append(self.img_linha9_projetil)

        # definir a imagem que vai ser exibida
        self.index_lista_projetil = 0
        self.image = self.sprites_projetil[int(self.index_lista_projetil)]

        self.image = pygame.transform.scale(self.image, (int(50 * Global.proporcao), int(50 * Global.proporcao)))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()
        retangulo_ajustado = pygame.Rect.inflate(self.rect, -(50 * 0.3), -(50 * 0.3))
        self.rect = retangulo_ajustado

        self.tempo_de_vida = 120

        # definir as coordenadas do projetil
        self.rect.center = (Mobs.player.rect.center[0], Mobs.player.rect.center[1])

    # lógica para atirar
    def atirar(self, desvio):

        # obtem as coordenadas do mouse
        posicao_mouse = mouse.get_pos()

        distancia_x = posicao_mouse[0] - self.rect.center[0]
        distancia_y = posicao_mouse[1] - self.rect.center[1]
        
        # calcula o angulo em radiano do click em relação ao player
        angulo_radiano = numpy.arctan2(distancia_y, distancia_x) + numpy.radians(desvio)

        # distribui a velocidade a partir do seno e cosseno
        self.velocidade_x = numpy.cos(angulo_radiano) * velocidade_base_projetil * Global.proporcao
        self.velocidade_y = numpy.sin(angulo_radiano) * velocidade_base_projetil * Global.proporcao
    
    def direcionar(self, raio):
        inimigo_mais_proximo = None

        for inimigo in Global.grupo_todos_inimigos:

            distancia_x = inimigo.rect.center[0] - self.rect.center[0]
            distancia_y = inimigo.rect.center[1] - self.rect.center[1]
            distancia_absoluta = (abs(distancia_x) ** 2 + abs(distancia_y) ** 2) ** 0.5

            if inimigo_mais_proximo == None or distancia_absoluta < inimigo_mais_proximo[1]:
                inimigo_mais_proximo = [inimigo, distancia_absoluta, distancia_x, distancia_y]
        
        if inimigo_mais_proximo[1] < raio:
            
            distancia_x = inimigo_mais_proximo[2]
            distancia_y = inimigo_mais_proximo[3]
            
            # calcula o angulo em radiano do inimigo em relação ao player
            angulo_radiano = numpy.arctan2(distancia_y, distancia_x)

            # distribui a velocidade a partir do seno e cosseno
            self.velocidade_x = numpy.cos(angulo_radiano) * velocidade_base_projetil * Global.proporcao
            self.velocidade_y = numpy.sin(angulo_radiano) * velocidade_base_projetil * Global.proporcao

    def update(self):

        if self.perfuracoes_restantes <= 0:
            self.kill()
        if self.tempo_de_vida <= 0:
            self.kill() 

        self.image = pygame.transform.scale(self.image, (int(50 * Global.proporcao), int(50 * Global.proporcao)))

        # ajusta as dimensoes do retangulo
        self.posicao_atual_rect = self.rect.center
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.inflate(self.rect, -(50 * 0.3), -(50 * 0.3))
        self.rect.center = self.posicao_atual_rect

        self.tempo_de_vida -= 1

        # atualizar imagem
        self.index_lista_projetil += 0.1

        if self.index_lista_projetil >= 8:
            self.index_lista_projetil = 0

        self.image = self.sprites_projetil[int(self.index_lista_projetil)]

        # faz o projetil se mover de acordo com resultado da distribuição final obtida
        self.rect.left += self.velocidade_x
        self.rect.top += self.velocidade_y
