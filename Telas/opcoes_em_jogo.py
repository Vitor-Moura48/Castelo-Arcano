from funcoes_main import *
from Telas import menu_principal
from Objetos.Componentes import botoes, icones
from Telas.Tela import Tela

class TelaOpcoes(Tela):
    def __init__(self):

        icone_de_fundo = icones.IconeBackground((0.5, 0.5), 
                                                (Global.dimensoes_janela[0] * 0.4, Global.dimensoes_janela[1] * 0.6))
        botao_continuar = botoes.Botao_1("Continuar", 
                                        (255, 50, 50), 
                                        (0.5, 0.30), 
                                        (300, 60))
        botao_reiniciar = botoes.Botao_1("Reiniciar",
                                        (255, 50, 50), 
                                        (0.5, 0.45), 
                                        (300, 60))
        botao_menu = botoes.Botao_1("Menu Principal", 
                                    (255, 50, 50), 
                                    (0.5, 0.60), 
                                    (300, 60))
        
        Tela.__init__(self, ([botao_continuar, lambda:None, True], [botao_reiniciar, self.reiniciar, True], [botao_menu, menu_principal.MenuPrincipal, True]),
                       icones=[icone_de_fundo], fill=False)

        while not self.selecionou:
            self.loop()
            self.atualizar()
        del self
    
    def reiniciar(self):

        Global.ganhou = False
        Global.perdeu = False
        Global.barreira = 0
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

        pygame.mixer_music.play(-1) if Global.som_ligado else None


        
  