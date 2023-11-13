from funcoes_main import *
import funcoes_main
from Telas import menu_principal
from Componentes import botoes, icones

def tela_upgrade(): 
    selecionou = False

    while not selecionou:
        Variaveis_globais.tela.fill((000, 000, 000))

        for componente in Variaveis_globais.componentes:
            componente.kill()

        icone_de_fundo = icones.IconeBackground((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2), (Variaveis_globais.dimensoes_janela[0] * 0.9, Variaveis_globais.dimensoes_janela[1] * 0.9))
        
        texto_para_tela = fonte.render('teste', True, (255, 255, 255))
        rect_texto = texto_para_tela.get_rect()
        rect_texto.center = (Variaveis_globais.dimensoes_janela[0] // 3, (Variaveis_globais.dimensoes_janela[1] * 0.20))
        Variaveis_globais.tela.blit(texto_para_tela, (rect_texto))
        
        botao_tempo_buff_01 = botoes.Botao("Velocidade de Movimento",
                                            (255, 50, 50),
                                            (Variaveis_globais.dimensoes_janela[0] // 3, (Variaveis_globais.dimensoes_janela[1] * 0.20)),
                                            (450, 60))
        botao_tempo_buff_02 = botoes.Botao("Barreira",
                                            (255, 50, 50),
                                            (Variaveis_globais.dimensoes_janela[0] // 3, (Variaveis_globais.dimensoes_janela[1] * 0.35)),
                                            (450, 60))
        botao_tempo_buff_03 = botoes.Botao("Multi Projeteis",
                                            (255, 50, 50),
                                            (Variaveis_globais.dimensoes_janela[0] // 3, (Variaveis_globais.dimensoes_janela[1] * 0.50)),
                                            (450, 60))
        botao_tempo_buff_04 = botoes.Botao("Velocidade de Disparo",
                                            (255, 50, 50),
                                            (Variaveis_globais.dimensoes_janela[0] // 3, (Variaveis_globais.dimensoes_janela[1] * 0.65)),
                                            (450, 60))
        botao_tempo_buff_05 = botoes.Botao("Projeteis Teleguiados",
                                            (255, 50, 50),
                                            (Variaveis_globais.dimensoes_janela[0] // 3, (Variaveis_globais.dimensoes_janela[1] * 0.80)),
                                            (450, 60))
        
        Variaveis_globais.componentes.add(icone_de_fundo)
        Variaveis_globais.componentes.add(botao_tempo_buff_01)
        Variaveis_globais.componentes.add(botao_tempo_buff_02)
        Variaveis_globais.componentes.add(botao_tempo_buff_03)
        Variaveis_globais.componentes.add(botao_tempo_buff_04)
        Variaveis_globais.componentes.add(botao_tempo_buff_05)

        Variaveis_globais.componentes.draw(Variaveis_globais.tela)
        Variaveis_globais.componentes.update()

        display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                funcoes_main.ajustar_tela()
        
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                posicao_mouse = pygame.mouse.get_pos()

                if botao_tempo_buff_01.rect.collidepoint(posicao_mouse):
                    pass
                if botao_tempo_buff_02.rect.collidepoint(posicao_mouse):
                    pass
                if botao_tempo_buff_03.rect.collidepoint(posicao_mouse):
                    pass
                if botao_tempo_buff_04.rect.collidepoint(posicao_mouse):
                    pass
                if botao_tempo_buff_05.rect.collidepoint(posicao_mouse):
                    pass
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True
                    menu_principal.menu_principal()

            