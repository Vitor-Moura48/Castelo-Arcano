from funcoes_main import *
from Telas import menu_principal
from Objetos.Componentes import botoes, icones
from Telas.Tela import Tela

class TelaUpgrade(Tela): 
    def __init__(self):

        self.arquivo_upgrades = pandas.read_csv("dados/csvs/upgrades.csv")
        self.arquivo_recursos = pandas.read_csv("dados/csvs/recursos.csv")

        icone_de_fundo = icones.IconeBackground((Global.dimensoes_janela[0] // 2, Global.dimensoes_janela[1] // 2), (Global.dimensoes_janela[0] * 0.9, Global.dimensoes_janela[1] * 0.9))
        
        componentes = [botoes.BotaoUpgrade((Global.dimensoes_janela[0] * (0.2 + coluna * 0.1), (Global.dimensoes_janela[1] * (0.20 + linha * 0.15)) ), 
                                (70, 70),
                                self.arquivo_upgrades.iloc[linha, coluna],
                                (linha, coluna))
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
                    ajustar_tela()
                    for componente in self.componentes:
                        componente[0].ajustar_posicoes(componente[0].coordenada)

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
            self.atualizar_mensagem()
            display.flip()          

    def conferir(self, botao):    
    
        if self.arquivo_upgrades.iloc[botao.linha_coluna] == False:  
            if self.arquivo_recursos["cristais"].loc[0] >= 3:
                self.arquivo_recursos["cristais"] -= 3
                self.arquivo_upgrades.iloc[botao.linha_coluna] = True

                self.arquivo_recursos.to_csv("dados/csvs/recursos.csv", index=False)
                self.arquivo_upgrades.to_csv("dados/csvs/upgrades.csv", index=False)
                botao.atualizar_informacoes()

        icone_de_fundo_descritivo = icones.IconeBackground((Global.dimensoes_janela[0] * 0.67, Global.dimensoes_janela[1]* 0.53), (Global.dimensoes_janela[0] * 0.35, Global.dimensoes_janela[1] * 0.64))
        Global.componentes.add(icone_de_fundo_descritivo)
    
    def atualizar_mensagem(self):
        texto_para_tela = fonte.render(f"Cristais: {self.arquivo_recursos['cristais'].loc[0]}", True, (200, 200, 255))
        rect_texto = texto_para_tela.get_rect()
        rect_texto.center = (Global.dimensoes_janela[0] * 0.76, Global.dimensoes_janela[1] * 0.15)

        Global.tela.blit(texto_para_tela, (rect_texto))

   
                