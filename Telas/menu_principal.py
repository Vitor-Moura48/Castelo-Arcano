from funcoes_main import *
from Telas import escolha_dificuldade, tela_configuracao
from Componentes import botoes

def menu_principal():    
    selecionou = False

    while not selecionou:
        Variaveis_globais.tela.fill((000, 000, 000))

        for componente in Variaveis_globais.componentes:
            componente.kill()

        # fazer uma tela inicial
        botao_jogar = botoes.Botao("Iniciar", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 40, 145 * Variaveis_globais.proporcao), (Variaveis_globais.dimensoes_janela[0] // 2, 160 * Variaveis_globais.proporcao), (300, 60))
        botao_configuracoes = botoes.Botao("Configuracoes", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 95, 245 * Variaveis_globais.proporcao), (Variaveis_globais.dimensoes_janela[0] // 2, 260 * Variaveis_globais.proporcao), (300, 60))
        
        Variaveis_globais.componentes.add(botao_jogar)
        Variaveis_globais.componentes.add(botao_configuracoes)

        Variaveis_globais.componentes.draw(Variaveis_globais.tela)
        Variaveis_globais.componentes.update()

        display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()

                # se o x for muito maior que o y
                if Variaveis_globais.dimensoes_janela[0] / Variaveis_globais.dimensoes_janela[1] > proporcao_altura_largura:

                    # se eu diminui o y
                    if Variaveis_globais.dimensoes_janela[0] * Variaveis_globais.dimensoes_janela[1] / (dimensao_base[0] * dimensao_base[1]) < Variaveis_globais.proporcao:
                        Variaveis_globais.tela = display.set_mode((Variaveis_globais.dimensoes_janela[1] * proporcao_altura_largura, Variaveis_globais.dimensoes_janela[1]), pygame.RESIZABLE)
                    # se eu aumentei o x
                    else:
                        Variaveis_globais.tela = display.set_mode((Variaveis_globais.dimensoes_janela[0], Variaveis_globais.dimensoes_janela[0] / proporcao_altura_largura), pygame.RESIZABLE)
                    
                    Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()

                # se o y for muito maior que o x
                elif Variaveis_globais.dimensoes_janela[0] / Variaveis_globais.dimensoes_janela[1] < proporcao_altura_largura:

                    # se eu diminui o x
                    if Variaveis_globais.dimensoes_janela[0] * Variaveis_globais.dimensoes_janela[1] / (dimensao_base[0] * dimensao_base[1]) < Variaveis_globais.proporcao:
                        Variaveis_globais.tela = display.set_mode((Variaveis_globais.dimensoes_janela[0], Variaveis_globais.dimensoes_janela[0] / proporcao_altura_largura), pygame.RESIZABLE)
                    # se eu aumentei o y
                    else:
                        Variaveis_globais.tela = display.set_mode((Variaveis_globais.dimensoes_janela[1] * proporcao_altura_largura, Variaveis_globais.dimensoes_janela[1]), pygame.RESIZABLE)
                    
                    Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()

                Variaveis_globais.proporcao = Variaveis_globais.proporcao = Variaveis_globais.dimensoes_janela[0] / dimensao_base[0]

                Castelo.castelo.rect_ajustado = pygame.Rect.inflate(Castelo.castelo.rect, int(Castelo.castelo.rect_base.width * Variaveis_globais.proporcao - Castelo.castelo.rect.width), int(Castelo.castelo.rect_base.height * Variaveis_globais.proporcao - Castelo.castelo.rect.height))
                Castelo.castelo.rect = Castelo.castelo.rect_ajustado

                retangulo_ajustado = pygame.Rect.inflate(Player.player.rect, int(Player.player.rect_base.width * Variaveis_globais.proporcao - Player.player.rect.width), int(Player.player.rect_base.height * Variaveis_globais.proporcao - Player.player.rect.height))
                Player.player.rect = retangulo_ajustado
        

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                posicao_mouse = pygame.mouse.get_pos()

                if botao_jogar.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    escolha_dificuldade.iniciar_jogo()

                if botao_configuracoes.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    tela_configuracao.tela_configuracoes()
