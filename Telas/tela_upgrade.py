from funcoes_main import *
import funcoes_main
from Telas import menu_principal
from Componentes import botoes, icones

def tela_upgrade(): 
    selecionou = False

    for componente in Variaveis_globais.componentes:
        componente.kill()

    upgrades_desbloqueadas = []
    arquivo_upgrades = pandas.read_csv("csvs/upgrades.csv")
    for _,linha in arquivo_upgrades.iterrows():
        for upgrade in linha:
            upgrades_desbloqueadas.append(upgrade)

    icone_de_fundo = icones.IconeBackground((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2), (Variaveis_globais.dimensoes_janela[0] * 0.9, Variaveis_globais.dimensoes_janela[1] * 0.9))

    botao_upgrade_01 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.2, (Variaveis_globais.dimensoes_janela[1] * 0.20) ), 
                                    (70, 70),
                                    upgrades_desbloqueadas[0])
    botao_upgrade_02 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.2, (Variaveis_globais.dimensoes_janela[1] * 0.35) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[3])
    botao_upgrade_03 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.2, (Variaveis_globais.dimensoes_janela[1] * 0.50) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[6])
    botao_upgrade_04 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.2, (Variaveis_globais.dimensoes_janela[1] * 0.65) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[9])
    botao_upgrade_05 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.2, (Variaveis_globais.dimensoes_janela[1] * 0.80) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[12])
    
    
    botao_upgrade_06 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.3, (Variaveis_globais.dimensoes_janela[1] * 0.20) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[1])
    botao_upgrade_07 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.3, (Variaveis_globais.dimensoes_janela[1] * 0.35) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[4])
    botao_upgrade_08 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.3, (Variaveis_globais.dimensoes_janela[1] * 0.50) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[7])
    botao_upgrade_09 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.3, (Variaveis_globais.dimensoes_janela[1] * 0.65) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[10])
    botao_upgrade_10 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.3, (Variaveis_globais.dimensoes_janela[1] * 0.80) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[13])
    
    
    botao_upgrade_11 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.4, (Variaveis_globais.dimensoes_janela[1] * 0.20) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[2])
    botao_upgrade_12 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.4, (Variaveis_globais.dimensoes_janela[1] * 0.35) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[5])
    botao_upgrade_13 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.4, (Variaveis_globais.dimensoes_janela[1] * 0.50) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[8])
    botao_upgrade_14 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.4, (Variaveis_globais.dimensoes_janela[1] * 0.65) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[11])
    botao_upgrade_15 = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * 0.4, (Variaveis_globais.dimensoes_janela[1] * 0.80) ), 
                                    (70, 70), 
                                    upgrades_desbloqueadas[14])

    Variaveis_globais.componentes.add(icone_de_fundo)
    Variaveis_globais.componentes.add(botao_upgrade_01)
    Variaveis_globais.componentes.add(botao_upgrade_02)
    Variaveis_globais.componentes.add(botao_upgrade_03)
    Variaveis_globais.componentes.add(botao_upgrade_04)
    Variaveis_globais.componentes.add(botao_upgrade_05)
    Variaveis_globais.componentes.add(botao_upgrade_06)
    Variaveis_globais.componentes.add(botao_upgrade_07)
    Variaveis_globais.componentes.add(botao_upgrade_08)
    Variaveis_globais.componentes.add(botao_upgrade_09)
    Variaveis_globais.componentes.add(botao_upgrade_10)
    Variaveis_globais.componentes.add(botao_upgrade_11)
    Variaveis_globais.componentes.add(botao_upgrade_12)
    Variaveis_globais.componentes.add(botao_upgrade_13)
    Variaveis_globais.componentes.add(botao_upgrade_14)
    Variaveis_globais.componentes.add(botao_upgrade_15)

    while not selecionou:

        Variaveis_globais.tela.fill((000, 000, 000))

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

                if botao_upgrade_01.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_02.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_03.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_04.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_05.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_06.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_07.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_08.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_09.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_10.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_11.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_12.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_13.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_14.rect.collidepoint(posicao_mouse):
                    pass
                if botao_upgrade_15.rect.collidepoint(posicao_mouse):
                    pass
                
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True
                    menu_principal.menu_principal()

            