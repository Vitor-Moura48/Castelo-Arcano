from Configurações.config import *
from Configurações import Global
from Objetos import Mobs, Projeteis

class Animacao(pygame.sprite.Sprite):
    def __init__(self, caminho, linhas_colunas, dimensoes, inflar, escala=None, soma_dimensao=(0, 0)):
        pygame.sprite.Sprite.__init__(self)

        Global.todas_as_sprites.add(self)

        self.sprite = pygame.image.load(os.path.join(caminho)).convert_alpha()

        self.sprites = [ self.sprite.subsurface((coluna * dimensoes[0] + soma_dimensao[0], linha * dimensoes[1] + soma_dimensao[1]), (dimensoes[0], dimensoes[1])) for linha in range(linhas_colunas[0]) for coluna in range(linhas_colunas[1]) ] # pega os sprites
        self.sprites = [pygame.transform.scale(imagem, escala) if escala != None else self.image for imagem in self.sprites] # transforma cada sprite se necessário
        self.sprite_index = 0

        self.image = self.sprites[self.sprite_index]

        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.inflate(self.rect, inflar[0], inflar[1])

        self.linhas = linhas_colunas[0]
        self.colunas = linhas_colunas[1]
    
    def contar_index(self, taxa=0.1):
        if self.sprite_index < ( self.linhas * self.colunas ) - 1:
            self.image = self.sprites[int(self.sprite_index)]
            self.sprite_index += taxa
            return True
        else:
            return False

class AnimacaoBarreira(Animacao):  # classe de efeitos diversos que acontecem as vezes
    def __init__(self):
        Animacao.__init__(self, 'dados/imagens/efeito barreira.png', (1, 6), (102, 245), (0, 0), escala=( 357 * Global.proporcao, 1058 * Global.proporcao ), soma_dimensao=(0, 100) )

        # posicionar sprite
        self.rect.centerx = Mobs.castelo.rect.centerx
        self.rect.bottom = Global.dimensoes_janela[1]

    # atualizar estado
    def update(self):
        self.kill() if not self.contar_index() else None

class AnimacaoTarget(Animacao):
    def __init__(self, alvo):
        Animacao.__init__(self, 'dados/imagens/target.png', (1, 5), (13, 13), (0, 0), (40 * Global.proporcao, 40 * Global.proporcao))

        self.rect.center = alvo
    
    def update(self):
        if not self.contar_index(0.03):
            projetil = Projeteis.ProjetilTarget(self.rect.center, 1)
            Global.grupo_projeteis_inimigos.add(projetil)
            self.kill()