from funcoes_main import Global, draw, dimensao_base, informacoes_tela
from Telas import menu_principal
from Objetos.Componentes import botoes, icones
from Telas.Tela import *

class TelaComfiguracoes(Tela): 
    def __init__(self):

        icone_de_fundo = icones.IconeBackground((0.5, 0.5), (Global.dimensoes_janela[0] * 0.4, Global.dimensoes_janela[1] * 0.6))
        botao_tela_cheia = botoes.Botao_1("Tela Cheia",
                                            (255, 50, 50),
                                            (0.5, 0.30),
                                            (300, 60))
        botao_voltar = botoes.Botao_1("Voltar", 
                                    (255, 50, 50), 
                                    (0.5, 0.45),
                                    (300, 60))
        botao_som = botoes.BotaoSom(coordenada=(0.9, 0.1), dimensoes=(50, 50))
        
        Tela.__init__(self, ([botao_tela_cheia, self.tela_cheia, False], [botao_voltar, menu_principal.MenuPrincipal, True], [botao_som, self.som, False]),
                      icones=[icone_de_fundo], esq=menu_principal.MenuPrincipal)

        while not self.selecionou:

            draw.rect(Global.tela, (000, 000, 255), botao_som.rect, int(5 * Global.proporcao)) if Global.som_ligado else draw.rect(Global.tela, (255, 000, 000), botao_som.rect, int(5 * Global.proporcao))
            self.loop()
            self.atualizar()
        
        del self

    def tela_cheia(self): # altera o estado
        Global.tela = display.set_mode(dimensao_base, pygame.RESIZABLE) if pygame.display.is_fullscreen() else display.set_mode((informacoes_tela.current_w, informacoes_tela.current_h), pygame.FULLSCREEN, 32) 
        funcoes_main.ajustar_tela()

    def som(self):
        if Global.som_ligado:
            Global.som_ligado = False
            pygame.mixer.stop()
            pygame.mixer_music.stop()
        else:
            Global.som_ligado = True
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
