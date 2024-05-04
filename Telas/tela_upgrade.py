from funcoes_main import pandas
from Telas import menu_principal
from Objetos.Componentes import botoes, icones, Texto
from Telas.Tela import *

class TelaUpgrade(Tela): 
    def __init__(self):

        self.arquivo_upgrades = pandas.read_csv("dados/csvs/upgrades.csv")
        self.arquivo_recursos = pandas.read_csv("dados/csvs/recursos.csv")

        icone_de_fundo = icones.IconeBackground((0.5, 0.5), (Global.dimensoes_janela[0] * 0.9, Global.dimensoes_janela[1] * 0.9))
        
        componentes = [botoes.BotaoUpgrade( coordenada=((0.2 + coluna * 0.1), (0.20 + linha * 0.15)), 
                                            dimensoes=(70, 70),
                                            desbloqueado=self.arquivo_upgrades.iloc[linha, coluna],
                                            linha_coluna=(linha, coluna))
                                            for linha in range(5) for coluna in range(3)]
        
        Tela.__init__(self, esq=menu_principal.MenuPrincipal)
        
        Global.componentes.add(icone_de_fundo)
        for componente in componentes:
            Global.componentes.add(componente) 
            Global.componente_botao.add(componente)
        
        while not self.selecionou:

            self.posicao_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                    sys.exit()
                
                if event.type == pygame.VIDEORESIZE:
                    funcoes_main.ajustar_tela()
                    for componente in Global.componentes:
                        componente.ajustar_posicoes()

                if event.type == MOUSEBUTTONDOWN and event.button == 1:       
                    for componente in Global.componente_botao:
                        if componente.rect.collidepoint(self.posicao_mouse):
                            self.conferir(componente)    

                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.selecionou = True
                        self.esq()

            Global.componentes.draw(Global.tela)
            Global.componentes.update()
            update = [texto.update() for texto in Global.textos]
            Texto.Texto(f"Cristais: {self.arquivo_recursos['cristais'].loc[0]}", (200, 200, 255), 30,  (0.7, 0.13), 0.95)
            display.flip()          

    def conferir(self, botao):    
    
        if self.arquivo_upgrades.iloc[botao.linha_coluna] == False:  
            if self.arquivo_recursos["cristais"].loc[0] >= 3:
                self.arquivo_recursos["cristais"] -= 3
                self.arquivo_upgrades.iloc[botao.linha_coluna] = True

                self.arquivo_recursos.to_csv("dados/csvs/recursos.csv", index=False)
                self.arquivo_upgrades.to_csv("dados/csvs/upgrades.csv", index=False)
                botao.atualizar_informacoes()
        
        Global.textos = [Texto.Texto(pandas.read_csv("dados/csvs/descricao_upgrades.csv").iloc[botao.linha_coluna], (200, 200, 255), 25, (0.57, 0.3), 0.77)]

        icone_de_fundo_descritivo = icones.IconeBackground((0.67, 0.53), (Global.dimensoes_janela[0] * 0.35, Global.dimensoes_janela[1] * 0.64))
        Global.componentes.add(icone_de_fundo_descritivo)
    