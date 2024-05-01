from funcoes_main import *
import funcoes_main

class Tela():
    def __init__(self, componentes=None, esq=None, fill=True): # componente = objeto,função

        self.selecionou = False
        self.componentes = componentes
        self.esq = esq
        
        for componente in Global.componentes:
            componente.kill()
        
        if self.componentes:
            for componente in self.componentes:
                Global.componentes.add(componente[0])
                Global.componente_botao.add(componente[0]) if componente[3] else None

        Global.tela.fill((000, 000, 000)) if fill else None

    def loop(self):
        self.posicao_mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                funcoes_main.ajustar_tela()
                for componente in self.componentes:
                    componente[0].ajustar_posicoes(componente[0].coordenada)

            if self.componentes:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    for componente in self.componentes:
                        if componente[3]:
                            if componente[0].rect.collidepoint(self.posicao_mouse):
                                componente[1]()
                                self.selecionou = True if componente[2] == True else None
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    self.selecionou = True
                    self.esq() if self.esq != None else None 

    def atualizar(self):
        Global.componentes.draw(Global.tela)
        Global.componentes.update()
        display.flip()
        