from funcoes_main import *
import funcoes_main
from Telas import menu_principal
from Componentes import botoes, icones

def tela_configuracoes(): 
    selecionou = False

    for componente in Global.componentes:
        componente.kill()

    icone_de_fundo = icones.IconeBackground((Global.dimensoes_janela[0] // 2, Global.dimensoes_janela[1] // 2), (Global.dimensoes_janela[0] * 0.4, Global.dimensoes_janela[1] * 0.6))
    botao_botao_tela_cheia = botoes.Botao_1("Tela Cheia",
                                        (255, 50, 50),
                                        (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.30)),
                                        (300, 60))
    botao_voltar = botoes.Botao_1("Voltar", 
                                (255, 50, 50), 
                                (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.45)),
                                (300, 60))
    botao_som = botoes.BotaoSom((Global.dimensoes_janela[0] * 0.9, (Global.dimensoes_janela[1] * 0.1)),
                                (50, 50))
    
    Global.componentes.add(icone_de_fundo)
    Global.componentes.add(botao_botao_tela_cheia)
    Global.componentes.add(botao_voltar)
    Global.componentes.add(botao_som)

    def ajustar_componenstes():
        icone_de_fundo.ajustar_posicoes(( int( Global.dimensoes_janela[0] * 0.5 ), int( Global.dimensoes_janela[1] * 0.5) ),
                                        ( int( Global.dimensoes_janela[0] * 0.4 ), int( Global.dimensoes_janela[1] * 0.6 ) ))
        botao_botao_tela_cheia.ajustar_posicoes(( int( Global.dimensoes_janela[0] * 0.5 ) , int( Global.dimensoes_janela[1] * 0.30 )  ))
        botao_voltar.ajustar_posicoes(( int( Global.dimensoes_janela[0] * 0.5 ), int( Global.dimensoes_janela[1] * 0.45) ))
        botao_som.ajustar_posicoes(( int( Global.dimensoes_janela[0] * 0.9 ), int( Global.dimensoes_janela[1] * 0.1 )  ))

    while not selecionou:
        Global.tela.fill((000, 000, 000))

        Global.componentes.draw(Global.tela)
        Global.componentes.update()

        if pygame.display.is_fullscreen():
            draw.rect(Global.tela, (000, 000, 255), botao_botao_tela_cheia.rect, 5)

        if Global.som_ligado:
            draw.rect(Global.tela, (000, 000, 255), botao_som.rect, 5)
        else:
            draw.rect(Global.tela, (255, 000, 000), botao_som.rect, 5)
      
        display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                funcoes_main.ajustar_tela()
                ajustar_componenstes()
        
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                posicao_mouse = pygame.mouse.get_pos()

                if botao_botao_tela_cheia.rect.collidepoint(posicao_mouse):

                    if pygame.display.is_fullscreen():
                        Global.tela = display.set_mode(dimensao_base, pygame.RESIZABLE)
                        Global.dimensoes_janela = pygame.display.get_surface().get_size()      

                    else:
                        Global.tela = display.set_mode((informacoes_tela.current_w, informacoes_tela.current_h), pygame.FULLSCREEN, 32)
                        Global.dimensoes_janela = pygame.display.get_surface().get_size()      
                        Global.proporcao = Global.dimensoes_janela[0] / dimensao_base[0]

                        Castelo.castelo.rect_ajustado = pygame.Rect.inflate(Castelo.castelo.rect, int(Castelo.castelo.rect_base.width * Global.proporcao - Castelo.castelo.rect.width), int(Castelo.castelo.rect_base.height * Global.proporcao - Castelo.castelo.rect.height))
                        Castelo.castelo.rect = Castelo.castelo.rect_ajustado

                        retangulo_ajustado = pygame.Rect.inflate(Player.player.rect, int(Player.player.rect_base.width * Global.proporcao - Player.player.rect.width), int(Player.player.rect_base.height * Global.proporcao - Player.player.rect.height))
                        Player.player.rect = retangulo_ajustado
                    
                    ajustar_componenstes()

                if botao_voltar.rect.collidepoint(posicao_mouse):
                    selecionou = True                              
                    menu_principal.menu_principal()
                
                if botao_som.rect.collidepoint(posicao_mouse):
                    if Global.som_ligado:
                        Global.som_ligado = False
                        pygame.mixer.stop()
                        pygame.mixer_music.stop()
                    else:
                        Global.som_ligado = True
                        pygame.mixer.music.set_volume(0.5)
                        musica_fundo = pygame.mixer.music.load("sons/musica de fundo.wav")
                        pygame.mixer.music.play(-1)

            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True
                    menu_principal.menu_principal()

            