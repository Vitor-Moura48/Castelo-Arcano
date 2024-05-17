from Configurações.config import pygame, os, numpy, uniform, velocidade_base_projetil, mouse
from Configurações import Global
from Objetos import Mobs


class Projetil(pygame.sprite.Sprite):
    def __init__(self, caminho, coordenada, perfuracao, dano, dimensoes, linha_coluna, inflar, ponto, tempo_de_vida, escala=None, desvio=0, velocidade=1):
        pygame.sprite.Sprite.__init__(self)
        Global.todas_as_sprites.add(self)

        self.sprite = pygame.image.load(os.path.join(caminho))

        self.sprites = [ self.sprite.subsurface((coluna * dimensoes[0] + linha_coluna[2][0], linha * dimensoes[1] + linha_coluna[2][1]), (dimensoes[0], dimensoes[1])) for linha in range(linha_coluna[0]) for coluna in range(linha_coluna[1]) ]
        self.sprites = [ pygame.transform.scale(imagem, escala) if escala != None else self.image for imagem in self.sprites ]
        self.sprite_index = 0

        self.image = self.sprites[self.sprite_index] 
        
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.inflate(self.rect, inflar[0], inflar[1])  
        self.rect.center = coordenada

        self.perfuracoes = perfuracao
        self.dano = dano
        self.ponto = ponto
        self.linhas = linha_coluna[0]
        self.colunas = linha_coluna[1]
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.tempo_de_vida = tempo_de_vida


        distancia_x = self.ponto[0] - self.rect.center[0]
        distancia_y = self.ponto[1] - self.rect.center[1]
        
        # calcula o angulo em radiano do click em relação ao player
        angulo_radiano = numpy.arctan2(distancia_y, distancia_x) + numpy.radians(desvio)

        # distribui a velocidade a partir do seno e cosseno
        self.forcax = numpy.cos(angulo_radiano) * velocidade_base_projetil * velocidade * Global.proporcao
        self.forcay = numpy.sin(angulo_radiano) * velocidade_base_projetil * velocidade * Global.proporcao

        self.angulo_graus_desvio = numpy.degrees(angulo_radiano) + desvio
    
    def conferir_integridade(self):
        self.tempo_de_vida -= 1
        self.kill() if self.tempo_de_vida <= 0 or self.perfuracoes <= 0 else None
    
    def contar_index(self, taxa=0.1):
        
        if self.sprite_index <= (self.linhas * self.colunas) - 1:
            self.image = self.sprites[int(self.sprite_index)]
            self.sprite_index += taxa
            return True
        else:
            return False
    
    def mover(self):
        self.velocidade_x += self.forcax
        self.velocidade_y += self. forcay

        if abs(self.velocidade_x) >= 1:
            self.rect.x += self.velocidade_x
            self.velocidade_x -= int(self.velocidade_x)
        if abs(self.velocidade_y) >= 1:
            self.rect.y += self.velocidade_y
            self.velocidade_y -= int(self.velocidade_y)


class Projetil1(Projetil):  # criar classe para projetil do player
    def __init__(self, coordenada, perfuracao, dano, desvio=0):
        Projetil.__init__(self, caminho='dados/imagens/Projeteis.png', coordenada=coordenada, perfuracao=perfuracao, desvio=desvio, tempo_de_vida=120,
                           dano=dano, ponto=mouse.get_pos(), dimensoes=(38, 38), linha_coluna=(1, 8, (3, 290)), escala=(50 * Global.proporcao, 50 * Global.proporcao),
                             inflar=(-15, -15))
    
    def direcionar(self, raio):
        if len(Global.grupo_todos_inimigos) > 0:
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
                self.forcax = numpy.cos(angulo_radiano) * velocidade_base_projetil * Global.proporcao
                self.forcay = numpy.sin(angulo_radiano) * velocidade_base_projetil * Global.proporcao

    def update(self):

        self.conferir_integridade()
        self.contar_index()
        self.mover()


class ProjetilInimigo(Projetil):  # criar classe para projetil do inimigo 3
    def __init__(self, coordenada, perfuracao, dano, desvio=0):
        Projetil.__init__( self, 'dados/imagens/projetil_inimigo3.png', coordenada=coordenada, perfuracao=perfuracao, dano=dano, tempo_de_vida=400,
                           desvio=desvio, ponto=Mobs.castelo.rect.center, velocidade=0.15, escala=(32 * Global.proporcao, 32 * Global.proporcao),
                             linha_coluna=(1, 4, (0,0)), dimensoes=(32, 32), inflar=(-10, -10) )
        
        self.sprites = [ pygame.transform.rotate(sprite, 90 - self.angulo_graus_desvio) for sprite in self.sprites]
    def update(self):

        self.conferir_integridade()
        self.contar_index()
        self.mover()
