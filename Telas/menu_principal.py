from funcoes_main import *
from Telas import escolha_dificuldade, tela_configuracao
from Componentes import botoes
import funcoes_main

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
                funcoes_main.ajustar_tela()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                posicao_mouse = pygame.mouse.get_pos()

                if botao_jogar.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    escolha_dificuldade.iniciar_jogo()

                if botao_configuracoes.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    tela_configuracao.tela_configuracoes()
