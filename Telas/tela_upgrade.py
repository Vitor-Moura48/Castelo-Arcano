from funcoes_main import *
import funcoes_main
from Telas import menu_principal
from Componentes import botoes, icones

def tela_upgrade(): 
    selecionou = False

    for componente in Variaveis_globais.componentes:
        componente.kill()

    arquivo_upgrades = pandas.read_csv("csvs/upgrades.csv")

    icone_de_fundo = icones.IconeBackground((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2), (Variaveis_globais.dimensoes_janela[0] * 0.9, Variaveis_globais.dimensoes_janela[1] * 0.9))
    Variaveis_globais.componentes.add(icone_de_fundo)
    
    for linha in range(5):
        for coluna in range(3):
            botao_upgrade = botoes.BotaoUpgrade((Variaveis_globais.dimensoes_janela[0] * (0.2 + coluna * 0.1), (Variaveis_globais.dimensoes_janela[1] * (0.20 + linha * 0.15)) ), 
                                    (70, 70),
                                    arquivo_upgrades.iloc[linha, coluna],
                                    (linha, coluna))
            Variaveis_globais.componentes.add(botao_upgrade)
            Variaveis_globais.componente_botao.add(botao_upgrade)
    
    while not selecionou:

        arquivo_recursos = pandas.read_csv("csvs/recursos.csv")
        arquivo_upgrades = pandas.read_csv("csvs/upgrades.csv")

        Variaveis_globais.tela.fill((000, 000, 000))

        Variaveis_globais.componentes.draw(Variaveis_globais.tela)
        Variaveis_globais.componentes.update()

        texto_para_tela = fonte.render(f"Cristais: {arquivo_recursos['cristais'].loc[0]}", True, (200, 200, 255))
        rect_texto = texto_para_tela.get_rect()
        rect_texto.center = (Variaveis_globais.dimensoes_janela[0] * 0.76, Variaveis_globais.dimensoes_janela[1] * 0.15)
        Variaveis_globais.tela.blit(texto_para_tela, (rect_texto))

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                funcoes_main.ajustar_tela()
 
                icone_de_fundo.ajustar_posicoes((Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2), (Variaveis_globais.dimensoes_janela[0] * 0.9, Variaveis_globais.dimensoes_janela[1] * 0.9))
                # percorre todos os componentes e atualiza a posição e dimensoes (ajusta a linha e coluna de acordo com os argumentos iniciais)
                for botao in Variaveis_globais.componente_botao:
                    botao.ajustar_posicoes((Variaveis_globais.dimensoes_janela[0] * (0.2 + 0.1 * botao.linha_coluna[1]), (Variaveis_globais.dimensoes_janela[1] * (0.20 + 0.15 * botao.linha_coluna[0]))),
                                            (70, 70))
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                posicao_mouse = pygame.mouse.get_pos()
      
                for botao in Variaveis_globais.componente_botao:
                    if botao.rect.collidepoint(posicao_mouse):
                        if arquivo_upgrades.iloc[botao.linha_coluna] == False:  

                            if arquivo_recursos["cristais"].loc[0] >= 3:
                                arquivo_recursos["cristais"] -= 3

                                arquivo_upgrades.iloc[linha, coluna] = True

                                arquivo_recursos.to_csv("csvs/recursos.csv", index=False)
                                arquivo_upgrades.to_csv("csvs/upgrades.csv", index=False)
                                botao.atualizar_informacoes()

                        icone_de_fundo_descritivo = icones.IconeBackground((Variaveis_globais.dimensoes_janela[0] * 0.67, Variaveis_globais.dimensoes_janela[1]* 0.53), (Variaveis_globais.dimensoes_janela[0] * 0.35, Variaveis_globais.dimensoes_janela[1] * 0.64))
                        Variaveis_globais.componentes.add(icone_de_fundo_descritivo)
                
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True
                    menu_principal.menu_principal()
        
        display.flip()

            