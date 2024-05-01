from funcoes_main import *
from Telas import menu_principal
from Objetos.Componentes import botoes, icones
from Telas.Tela import Tela

class TelaComfiguracoes(Tela): 
    def __init__(self):

        icone_de_fundo = icones.IconeBackground((Global.dimensoes_janela[0] // 2, Global.dimensoes_janela[1] // 2), (Global.dimensoes_janela[0] * 0.4, Global.dimensoes_janela[1] * 0.6))
        botao_tela_cheia = botoes.Botao_1("Tela Cheia",
                                            (255, 50, 50),
                                            (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.30)),
                                            (300, 60))
        botao_voltar = botoes.Botao_1("Voltar", 
                                    (255, 50, 50), 
                                    (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.45)),
                                    (300, 60))
        botao_som = botoes.BotaoSom((Global.dimensoes_janela[0] * 0.9, (Global.dimensoes_janela[1] * 0.1)),
                                    (50, 50))
        
        Tela.__init__(self, ([botao_tela_cheia, self.tela_cheia, False, True], [botao_voltar, menu_principal.MenuPrincipal, True, True], [botao_som, self.som, False, True]), esq=menu_principal.MenuPrincipal)

        while not self.selecionou:

            draw.rect(Global.tela, (000, 000, 255), botao_tela_cheia.rect, 5) if pygame.display.is_fullscreen() else None
            draw.rect(Global.tela, (000, 000, 255), botao_som.rect, 5) if Global.som_ligado else draw.rect(Global.tela, (255, 000, 000), botao_som.rect, 5)

            self.loop()
            self.atualizar()
        
        del self

    def tela_cheia(self):
        if pygame.display.is_fullscreen():
            Global.tela = display.set_mode(dimensao_base, pygame.RESIZABLE)
            Global.dimensoes_janela = pygame.display.get_surface().get_size()      

        else:
            Global.tela = display.set_mode((informacoes_tela.current_w, informacoes_tela.current_h), pygame.FULLSCREEN, 32)
            Global.dimensoes_janela = pygame.display.get_surface().get_size()      
            Global.proporcao = Global.dimensoes_janela[0] / dimensao_base[0]

    def som(self):
        if Global.som_ligado:
            Global.som_ligado = False
            pygame.mixer.stop()
            pygame.mixer_music.stop()
        else:
            Global.som_ligado = True
            pygame.mixer.music.set_volume(0.5)
            musica_fundo = pygame.mixer.music.load("dados/sons/musica de fundo.wav")
            pygame.mixer.music.play(-1)
