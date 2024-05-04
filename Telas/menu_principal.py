from funcoes_main import *
from Telas import escolha_dificuldade, tela_configuracao, tela_upgrade, Tela_sair
from Objetos.Componentes import botoes, Texto
from Telas.Tela import Tela

class MenuPrincipal(Tela):    
    def __init__(self):

        # fazer uma tela inicial
        botao_jogar = botoes.Botao_1("Iniciar", 
                                    (255, 50, 50), 
                                    (0.5, 0.25), 
                                    (300, 60))
        botao_upgrade = botoes.Botao_1("Upgrade", 
                                            (255, 50, 50), 
                                            (0.5, 0.4), 
                                            ( 300, 60))
        botao_configuracoes = botoes.Botao_1("Configuracoes", 
                                            (255, 50, 50), 
                                            (0.5, 0.55), 
                                            (300, 60))

        Tela.__init__(self, ([botao_jogar, escolha_dificuldade.EscolhaDificuldade, True], [botao_upgrade, tela_upgrade.TelaUpgrade, True], [botao_configuracoes, tela_configuracao.TelaComfiguracoes, True]), esq=Tela_sair.TelaSair)

        while not self.selecionou:
            self.loop()
            self.atualizar()
        del self


   