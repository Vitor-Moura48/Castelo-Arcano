from funcoes_main import *
from Telas import menu_principal
from Componentes import botoes, icones

def tela_configuracoes(): 
    selecionou = False

    while not selecionou:
        Variaveis_globais.tela.fill((000, 000, 000))

        for componente in Variaveis_globais.componentes:
            componente.kill()

        icone_de_fundo = icones.IconeBackground((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2), (Variaveis_globais.dimensoes_janela[0] * 0.4, Variaveis_globais.dimensoes_janela[1] * 0.6))
        botao_botao_tela_cheia = botoes.Botao("Tela Cheia", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 65, 190 * Variaveis_globais.proporcao), (Variaveis_globais.dimensoes_janela[0] // 2, 205 * Variaveis_globais.proporcao), (300, 60))
        botao_voltar = botoes.Botao("Voltar", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 40, 290 * Variaveis_globais.proporcao), (Variaveis_globais.dimensoes_janela[0] // 2, 305 * Variaveis_globais.proporcao), (300, 60))
        
        Variaveis_globais.componentes.add(icone_de_fundo)
        Variaveis_globais.componentes.add(botao_botao_tela_cheia)
        Variaveis_globais.componentes.add(botao_voltar)

        Variaveis_globais.componentes.draw(Variaveis_globais.tela)
        Variaveis_globais.componentes.update()

        if pygame.display.is_fullscreen():
            draw.rect(Variaveis_globais.tela, (000, 000, 255), botao_botao_tela_cheia.rect, 5)
      
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

                if botao_botao_tela_cheia.rect.collidepoint(posicao_mouse):

                    if pygame.display.is_fullscreen():
                        Variaveis_globais.tela = display.set_mode(dimensao_base, pygame.RESIZABLE)
                        Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()      

                        # MELHORAR
                        for componente in Variaveis_globais.componentes:
                            componente.kill()
                        icone_de_fundo = icones.IconeBackground((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2), (Variaveis_globais.dimensoes_janela[0] * 0.4, Variaveis_globais.dimensoes_janela[1] * 0.6))
                        botao_botao_tela_cheia = botoes.Botao("Tela Cheia", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 65, 190), (Variaveis_globais.dimensoes_janela[0] // 2, 205), (300, 60))
                        botao_voltar = botoes.Botao("Voltar", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 40, 290), (Variaveis_globais.dimensoes_janela[0] // 2, 305), (300, 60))
                        Variaveis_globais.componentes.add(icone_de_fundo)
                        Variaveis_globais.componentes.add(botao_botao_tela_cheia)
                        Variaveis_globais.componentes.add(botao_voltar)

                    else:
                        Variaveis_globais.tela = display.set_mode((informacoes_tela.current_w, informacoes_tela.current_h), pygame.FULLSCREEN, 32)
                        Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()      
                        Variaveis_globais.proporcao = Variaveis_globais.dimensoes_janela[0] / dimensao_base[0]

                        Castelo.castelo.rect_ajustado = pygame.Rect.inflate(Castelo.castelo.rect, int(Castelo.castelo.rect_base.width * Variaveis_globais.proporcao - Castelo.castelo.rect.width), int(Castelo.castelo.rect_base.height * Variaveis_globais.proporcao - Castelo.castelo.rect.height))
                        Castelo.castelo.rect = Castelo.castelo.rect_ajustado

                        retangulo_ajustado = pygame.Rect.inflate(Player.player.rect, int(Player.player.rect_base.width * Variaveis_globais.proporcao - Player.player.rect.width), int(Player.player.rect_base.height * Variaveis_globais.proporcao - Player.player.rect.height))
                        Player.player.rect = retangulo_ajustado

                        # MELHORAR
                        for componente in Variaveis_globais.componentes:
                            componente.kill()

                        icone_de_fundo = icones.IconeBackground((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2), (Variaveis_globais.dimensoes_janela[0] * 0.4, Variaveis_globais.dimensoes_janela[1] * 0.6))
                        botao_botao_tela_cheia = botoes.Botao("Tela Cheia", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 65, 285), (Variaveis_globais.dimensoes_janela[0] // 2, 300), (300, 60))
                        botao_voltar = botoes.Botao("Voltar", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 40, 385), (Variaveis_globais.dimensoes_janela[0] // 2, 400), (300, 60))
                        
                        Variaveis_globais.componentes.add(icone_de_fundo)
                        Variaveis_globais.componentes.add(botao_botao_tela_cheia)
                        Variaveis_globais.componentes.add(botao_voltar)

                if botao_voltar.rect.collidepoint(posicao_mouse):
                    selecionou = True                              
                    menu_principal.menu_principal()
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True
                    menu_principal.menu_principal()

            