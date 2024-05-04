from funcoes_main import *
from Telas import menu_principal
from Objetos.Componentes import botoes, icones
from Telas.Tela import Tela

class TelaSair(Tela):
    def __init__(self):

        icone_de_fundo = icones.IconeBackground((0.5, 0.5), 
                                                (Global.dimensoes_janela[0] * 0.4, Global.dimensoes_janela[1] * 0.6))
        botao_sair = botoes.Botao_1("Sair", 
                                        (255, 50, 50), 
                                        (0.5, 0.35), 
                                        (300, 60))
        botao_voltar = botoes.Botao_1("Voltar",
                                        (255, 50, 50), 
                                        (0.5, 0.5), 
                                        (300, 60))
        
        Tela.__init__(self, ([botao_sair, sys.exit, True], [botao_voltar, menu_principal.MenuPrincipal, True]),
                       icones=[icone_de_fundo], fill=False, esq=menu_principal.MenuPrincipal)

        while not self.selecionou:
            self.loop()
            self.atualizar()
        del self