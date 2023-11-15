from Configurações.config import *
from Configurações  import Variaveis_globais
from Efeitos import animacoes

sprite_sheet_efeitos = pygame.image.load(os.path.join('imagens/bolas de efeito.png')).convert_alpha()
rect_efeitos = sprite_sheet_efeitos.get_rect()
largura_efeitos = rect_efeitos.width
altura_efeitos = rect_efeitos.height

class SpritesEfeito2(pygame.sprite.Sprite):  # classe para efeito especiail 2
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # define imagem que vai ser exibida
        self.image = sprite_sheet_efeitos.subsurface((640, 320), (320, 320))

        # mudar dimensões do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.13 * Variaveis_globais.proporcao, 320 * 0.13 * Variaveis_globais.proporcao))

        # encontrar as dimensões da imagem
        self.rect = self.image.get_rect()

        # randomizar as coordenadas do spaw
        self.randomizar()

    def randomizar(self):

        self.rect.left = randint(Variaveis_globais.dimensoes_janela[0], Variaveis_globais.dimensoes_janela[0] + 500)
        self.rect.top = randint(int(Variaveis_globais.dimensoes_janela[1] * 0.14), int(Variaveis_globais.dimensoes_janela[1] * 0.84))

    # quando o player colide com o buff, ganha um ponto de escudo
    def buff(self):

        Variaveis_globais.barreira += 1

        efeito_animacao = animacoes.EfeitosAnimacao()
        Variaveis_globais.todas_as_sprites.add(efeito_animacao)

    # atualizar estado
    def update(self):

        # movimentar buff no eixo x
        self.rect.x -= Variaveis_globais.velocidade_inimigo  * Variaveis_globais.proporcao

        # mudar escala do sprite
        self.image = pygame.transform.scale(self.image, (320 * 0.13 * Variaveis_globais.proporcao, 320 * 0.13 * Variaveis_globais.proporcao))


efeito_buff2 = SpritesEfeito2()
