from funcoes_main import *
import funcoes_main
from Telas import menu_principal
from Componentes import botoes, icones

def tela_configuracoes(): 
    selecionou = False

    for componente in Variaveis_globais.componentes:
        componente.kill()

    icone_de_fundo = icones.IconeBackground((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2), (Variaveis_globais.dimensoes_janela[0] * 0.4, Variaveis_globais.dimensoes_janela[1] * 0.6))
    botao_botao_tela_cheia = botoes.Botao("Tela Cheia",
                                        (255, 50, 50),
                                        (Variaveis_globais.dimensoes_janela[0] // 2, (Variaveis_globais.dimensoes_janela[1] * 0.30)),
                                        (300, 60))
    botao_voltar = botoes.Botao("Voltar", 
                                (255, 50, 50), 
                                (Variaveis_globais.dimensoes_janela[0] // 2, (Variaveis_globais.dimensoes_janela[1] * 0.45)),
                                (300, 60))
    
    Variaveis_globais.componentes.add(icone_de_fundo)
    Variaveis_globais.componentes.add(botao_botao_tela_cheia)
    Variaveis_globais.componentes.add(botao_voltar)

    while not selecionou:
        Variaveis_globais.tela.fill((000, 000, 000))

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
                funcoes_main.ajustar_tela()

                icone_de_fundo.ajustar_posicoes((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2),
                                                (Variaveis_globais.dimensoes_janela[0] * 0.4, Variaveis_globais.dimensoes_janela[1] * 0.6))
                botao_botao_tela_cheia.ajustar_posicoes((Variaveis_globais.dimensoes_janela[0] // 2, (Variaveis_globais.dimensoes_janela[1] * 0.30)))
                botao_voltar.ajustar_posicoes((Variaveis_globais.dimensoes_janela[0] // 2, (Variaveis_globais.dimensoes_janela[1] * 0.45)))
        
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                posicao_mouse = pygame.mouse.get_pos()

                if botao_botao_tela_cheia.rect.collidepoint(posicao_mouse):

                    if pygame.display.is_fullscreen():
                        Variaveis_globais.tela = display.set_mode(dimensao_base, pygame.RESIZABLE)
                        Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()      

                    else:
                        Variaveis_globais.tela = display.set_mode((informacoes_tela.current_w, informacoes_tela.current_h), pygame.FULLSCREEN, 32)
                        Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()      
                        Variaveis_globais.proporcao = Variaveis_globais.dimensoes_janela[0] / dimensao_base[0]

                        Castelo.castelo.rect_ajustado = pygame.Rect.inflate(Castelo.castelo.rect, int(Castelo.castelo.rect_base.width * Variaveis_globais.proporcao - Castelo.castelo.rect.width), int(Castelo.castelo.rect_base.height * Variaveis_globais.proporcao - Castelo.castelo.rect.height))
                        Castelo.castelo.rect = Castelo.castelo.rect_ajustado

                        retangulo_ajustado = pygame.Rect.inflate(Player.player.rect, int(Player.player.rect_base.width * Variaveis_globais.proporcao - Player.player.rect.width), int(Player.player.rect_base.height * Variaveis_globais.proporcao - Player.player.rect.height))
                        Player.player.rect = retangulo_ajustado
                    
                    icone_de_fundo.ajustar_posicoes((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2),
                                                (Variaveis_globais.dimensoes_janela[0] * 0.4, Variaveis_globais.dimensoes_janela[1] * 0.6))
                    botao_botao_tela_cheia.ajustar_posicoes((Variaveis_globais.dimensoes_janela[0] // 2, (Variaveis_globais.dimensoes_janela[1] * 0.30)))
                    botao_voltar.ajustar_posicoes((Variaveis_globais.dimensoes_janela[0] // 2, (Variaveis_globais.dimensoes_janela[1] * 0.45)))

                if botao_voltar.rect.collidepoint(posicao_mouse):
                    selecionou = True                              
                    menu_principal.menu_principal()
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True
                    menu_principal.menu_principal()

            