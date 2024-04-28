from funcoes_main import *
from Telas import escolha_dificuldade, tela_configuracao, tela_upgrade
from Componentes import botoes
import funcoes_main

def menu_principal():    
    selecionou = False

    for componente in Global.componentes:
        componente.kill()

    # fazer uma tela inicial
    botao_jogar = botoes.Botao("Iniciar", 
                                (255, 50, 50), 
                                (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.25)), 
                                (300, 60))
    botao_upgrade = botoes.Botao("Upgrade", 
                                        (255, 50, 50), 
                                        (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.40) ), 
                                        (300, 60))
    botao_configuracoes = botoes.Botao("Configuracoes", 
                                        (255, 50, 50), 
                                        (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.55) ), 
                                        (300, 60))
    
    Global.componentes.add(botao_jogar)
    Global.componentes.add(botao_upgrade)
    Global.componentes.add(botao_configuracoes)

    while not selecionou:
        Global.tela.fill((000, 000, 000))

        posicao_mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                funcoes_main.ajustar_tela()

                botao_jogar.ajustar_posicoes((Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.25)))
                botao_upgrade.ajustar_posicoes((Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.40)))
                botao_configuracoes.ajustar_posicoes((Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.55)))

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if botao_jogar.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    escolha_dificuldade.iniciar_jogo()
                
                if botao_upgrade.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    tela_upgrade.tela_upgrade()

                if botao_configuracoes.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    tela_configuracao.tela_configuracoes()
    
        Global.componentes.draw(Global.tela)
        Global.componentes.update()

        display.flip()

