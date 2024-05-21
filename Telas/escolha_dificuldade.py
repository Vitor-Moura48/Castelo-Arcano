from funcoes_main import *
from Telas import menu_principal
from Objetos.Componentes import botoes, Texto
from Objetos import Mobs
from Telas.Tela import Tela

# função para definir o modo de jogo e outras coisas
class EscolhaDificuldade(Tela):
    def __init__(self):

        # fazer uma tela inicial
        mensagem_dificuldade = Texto.Texto('Selecione a dificuldade', (255, 000, 000), 30, (0.355, 0.12), 0.7, 5)
        botao_facil = botoes.Botao_1("Fácil", 
                                    (255, 50, 50), 
                                    (0.5, 0.25), 
                                    (300, 60))
        botao_normal = botoes.Botao_1("Normal", 
                                    (255, 50, 50), 
                                    (0.5, 0.4), 
                                    (300, 60))
        botao_dificil = botoes.Botao_1("Dificil", 
                                        (255, 50, 50),
                                        (0.5, 0.55), 
                                        (300, 60))
    
        Tela.__init__(self, ([botao_facil, self.facil, True], [botao_normal, self.medio, True], [botao_dificil, self.dificil, True]), textos=[mensagem_dificuldade], esq=menu_principal.MenuPrincipal)

        while not self.selecionou:
            self.loop()
            self.atualizar()
        del self
    
    def iniciar(self):
        Global.ganhou = False
        Global.perdeu = False
        Global.barreira = 0
        Global.contador_de_bosses = 0
        Global.tempo_de_recarga_disparo = 0
        Global.tempo_buff_multiplos_disparos = 0
        Global.tempo_buff_velocidade_disparo = 0
        Global.tempo_buff_disparo_teleguiado = 0

        for sprite in Global.todas_as_sprites:
            sprite.kill()

        Mobs.player = Mobs.SpritesPlayer(5, 1)
        Global.todas_as_sprites.add(Mobs.player)
        Mobs.castelo = Mobs.SpriteCastelo(10)
        Global.todas_as_sprites.add(Mobs.castelo)

        if Global.dificuldade == 1:

            Global.inimigos_totais = 60
            Global.inimigos_restantes = Global.inimigos_totais
            Global.velocidade_inimigo = velocidade_base_inimigo * 0.70 * Global.proporcao
        if Global.dificuldade == 2:

            Global.inimigos_totais = 80
            Global.inimigos_restantes = Global.inimigos_totais
            Global.velocidade_inimigo = velocidade_base_inimigo * Global.proporcao

        if Global.dificuldade == 3:

            Global.inimigos_totais = 120
            Global.inimigos_restantes = Global.inimigos_totais
            Global.velocidade_inimigo = velocidade_base_inimigo * 1.15 * Global.proporcao

        if Global.som_ligado:
            pygame.mixer_music.play(-1)

    def facil(self):
        Global.dificuldade = 1
        self.iniciar()
    def medio(self):
        Global.dificuldade = 2
        self.iniciar()
    def dificil(self):
        Global.dificuldade = 3
        self.iniciar()

