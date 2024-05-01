from Configurações.config import *
from Configurações import Controles, Global
from Objetos import Mobs, Projeteis, Buffs
from Verificações import Colisoes
from Telas import menu_principal, escolha_dificuldade, opcoes_em_jogo

def conferir_arquivos_csv():
    if not os.path.exists("dados/csvs/upgrades.csv"):
        arquivo = pandas.DataFrame({'coluna1': [False, False, False, False, False],
                                    'coluna2': [False, False, False, False, False],
                                    'coluna3': [False, False, False, False, False]})
        arquivo.to_csv("dados/csvs/upgrades.csv", index=False)
    
    if not os.path.exists("dados/csvs/recursos.csv"):
        arquivo = pandas.DataFrame({'cristais': [0]})
        arquivo.to_csv("dados/csvs/recursos.csv", index=False)

def chamar_menu_principal():
    menu_principal.MenuPrincipal()

def adicioanr_objetos():

    # adicionar objetos
    if Global.inimigos_restantes < (Global.inimigos_totais * 0.1) and Global.contador_de_bosses == 0 and len(Global.grupo_todos_inimigos) < Global.inimigos_restantes:
        for i in range(1):
            boss_01 = Mobs.SpritesBoss1(10, 5)
            Global.grupo_todos_inimigos.add(boss_01)
            Global.grupo_todos_bosses.add(boss_01)
            Global.contador_de_bosses += 1

    if len(Global.grupo_inimigos1) < 2 and len(Global.grupo_todos_inimigos) < Global.inimigos_restantes:
        for i in range(1):
            inimigo1 = Mobs.SpritesInimigo1(1, 1)
            Global.grupo_inimigos1.add(inimigo1)
            Global.grupo_todos_inimigos.add(inimigo1)

    if len(Global.grupo_inimigos2) < 1 and len(Global.grupo_todos_inimigos) < Global.inimigos_restantes:
        for i in range(1):
            inimigo2 = Mobs.SpritesInimigo2(1, 1)
            Global.grupo_inimigos2.add(inimigo2)
            Global.grupo_todos_inimigos.add(inimigo2)
    
    if len(Global.grupo_inimigos3) < 1 and len(Global.grupo_todos_inimigos) < Global.inimigos_restantes:
        for i in range(1):
            inimigo3 = Mobs.SpritesInimigo3(3, 5)
            Global.grupo_inimigos3.add(inimigo3)
            Global.grupo_todos_inimigos.add(inimigo3)
    
    # porcentagem de aparecimento a cada iteração
    if len(Global.grupo_efeitos) < 2 and uniform(0, 100) <= 0.05:
        Buffs.SpritesEfeito1()
    if len(Global.grupo_efeitos) < 2 and uniform(0, 100) <= 0.05:
        Buffs.SpritesEfeito2()
    if len(Global.grupo_efeitos) < 2 and uniform(0, 100) <= 0.05:
        Buffs.SpritesEfeito3()
    if len(Global.grupo_efeitos) < 2 and uniform(0, 100) <= 0.05:
        Buffs.SpritesEfeito4()
    if len(Global.grupo_efeitos) < 2 and uniform(0, 100) <= 0.05:
        Buffs.SpritesEfeito5()

    # adiconar objetos sprites na tela
    Global.todas_as_sprites.draw(Global.tela)
    Global.todas_as_sprites.update()


def verificar_colisoes():
    Colisoes.colisoes.colisao_com_player()
    Colisoes.colisoes.colisao_com_castelo()
    Colisoes.colisoes.colisao_com_projetil_player()
    Colisoes.colisoes.saiu_do_mapa()


def criar_texto_na_janela():
    
    mensagem_kills = f"inimigos restantes: {Global.inimigos_restantes}"
    mensagem_kills_para_tela = fonte.render(mensagem_kills, True, (80, 80, 255))

    mensagem_vidas_castelo = f"vidas restantes: {Mobs.castelo.vida}"
    mensagem_vidas_castelo_para_tela = fonte.render(mensagem_vidas_castelo, True, (247, 24, 14))

    mensagem_barreira = f'defesa: {Global.barreira}'
    mensagem_barreira_para_tela = fonte.render(mensagem_barreira, True, (255, 100, 20))

    # colocar o texto na janela
    Global.tela.blit(mensagem_kills_para_tela, (Global.dimensoes_janela[0] * 0.7, Global.dimensoes_janela[1] * 0.02))
    Global.tela.blit(mensagem_vidas_castelo_para_tela, (Global.dimensoes_janela[0] * 0.02, Global.dimensoes_janela[1] * 0.02))
    if Global.barreira > 0:
        Global.tela.blit(mensagem_barreira_para_tela, (Global.dimensoes_janela[0] * 0.08, Global.dimensoes_janela[1] * 0.08))

def contabilizar_tempo_recargas():
    Global.tempo_de_recarga_disparo -= 1
    Global.tempo_buff_multiplos_disparos -= 1
    Global.tempo_buff_velocidade_disparo -= 1
    Global.tempo_buff_disparo_teleguiado -= 1

def responder_a_eventos():
    # responder a eventos
    for event in pygame.event.get():

        if event.type == QUIT:
            print("game over")
            quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and event.button == 1 and Global.tempo_de_recarga_disparo <= 0:

            if Global.tempo_buff_multiplos_disparos > 0:
                    
                    arquivo_upgrade = pandas.read_csv("dados/csvs/upgrades.csv")
                    if arquivo_upgrade.iloc[2, 1] == True:
                        quantidade_projeteis = 5
                    else:
                        quantidade_projeteis = 3

                    amplitude_entre_projeteis = (Global.amplitude_projeteis * 2) / (quantidade_projeteis - 1) # amplitude positiva e negativa, dividido pela quantidade de projeteis menos 1
                    somador_amplitude = -Global.amplitude_projeteis
 
                    for i in range(quantidade_projeteis):
                        projetil_player = Projeteis.Projetil1(Mobs.player.rect.center, 1, 1, desvio=somador_amplitude)
                        Global.grupo_projeteis_aliados.add(projetil_player)


                        
                        Global.tempo_de_recarga_disparo = 60
                        # aumenta em 10 x a velocidade de disparo
                        if Global.tempo_buff_velocidade_disparo >= 0:
                            Global.tempo_de_recarga_disparo *= 0.1
               
                        somador_amplitude += amplitude_entre_projeteis

            else:
                
                projetil_player = Projeteis.Projetil1(Mobs.player.rect.center, 1, 1)
                Global.grupo_projeteis_aliados.add(projetil_player)

                Global.tempo_de_recarga_disparo = 60
                # aumenta em 10 x a velocidade de disparo
                if Global.tempo_buff_velocidade_disparo >= 0:
                    arquivo_upgrade = pandas.read_csv("dados/csvs/upgrades.csv")

                    if arquivo_upgrade.iloc[3, 1] == True:
                        Global.tempo_de_recarga_disparo *= 0.05
                    else:
                        Global.tempo_de_recarga_disparo *= 0.1
        
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            Mobs.player.trocar_modo()

        # responde aos eventos do controle
        if event.type == JOYDEVICEADDED:
            Controles.controle.__init__()

        if event.type == pygame.JOYAXISMOTION:
            Controles.controle.movimento(event)
        
        if event.type == pygame.VIDEORESIZE:
            ajustar_tela()
    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                opcoes_em_jogo.TelaOpcoes()

def gerenciar_waves(): 
    if Global.inimigos_restantes <= Global.inimigos_totais * 0.8 and not Global.mudanca_de_velocidade[0]:
            Global.velocidade_inimigo *= 1.04
            Global.mudanca_de_velocidade[0] = True

    elif Global.inimigos_restantes <= Global.inimigos_totais * 0.6 and not Global.mudanca_de_velocidade[1]:
        Global.velocidade_inimigo *= 1.04
        Global.mudanca_de_velocidade[1] = True

    elif Global.inimigos_restantes <= Global.inimigos_totais * 0.4 and not Global.mudanca_de_velocidade[2]:
        Global.velocidade_inimigo *= 1.04
        Global.mudanca_de_velocidade[2] = True

    elif Global.inimigos_restantes <= Global.inimigos_totais * 0.2 and not Global.mudanca_de_velocidade[3]:
        Global.velocidade_inimigo *= 1.04
        Global.mudanca_de_velocidade[3] = True

def verificar_derrota_vitoria():

    if Mobs.player.vida <= 0 or Mobs.castelo.vida <= 0:
        responder_a_derrota()

    elif Global.inimigos_restantes <= 0:
        responder_a_vitoria()

    
def responder_a_derrota():

    Global.perdeu = True
    if Global.som_ligado:
        efeito_derrota.play()

    while Global.perdeu:
        rect_mensagem_derrota.center = (Global.dimensoes_janela[0] // 2, Global.dimensoes_janela[1] // 2)
        Global.tela.blit(mensagem_derrota_para_tela, rect_mensagem_derrota)
        display.flip()

        pygame.mixer_music.fadeout(100) 

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    escolha_dificuldade.EscolhaDificuldade()


def responder_a_vitoria():

    Global.ganhou = True
    if Global.som_ligado:
        efeito_vitoria.play()

    if Global.dificuldade == 1:

        novo_dataframe = pandas.DataFrame(data=[Mobs.castelo.vida], columns=['Recorde'])
        novo_dataframe.to_csv('dados/csvs/recorde_fácil.csv', mode='a', index=False, header=False)

        arquivo_recursos = pandas.read_csv("dados/csvs/recursos.csv")
        arquivo_recursos['cristais'] += 1
        arquivo_recursos.to_csv("dados/csvs/recursos.csv", index=False)

    if Global.dificuldade == 2:

        novo_dataframe = pandas.DataFrame(data=[Mobs.castelo.vida], columns=['Recorde'])
        novo_dataframe.to_csv('dados/csvs/recorde_médio.csv', mode='a', index=False, header=False)

        arquivo_recursos = pandas.read_csv("dados/csvs/recursos.csv")
        arquivo_recursos['cristais'] += 2
        arquivo_recursos.to_csv("dados/csvs/recursos.csv", index=False)

    if Global.dificuldade == 3:

        novo_dataframe = pandas.DataFrame(data=[Mobs.castelo.vida], columns=['Recorde'])
        novo_dataframe.to_csv('dados/csvs/recorde_difícil.csv', mode='a', index=False, header=False)

        arquivo_recursos = pandas.read_csv("dados/csvs/recursos.csv")
        arquivo_recursos['cristais'] += 3
        arquivo_recursos.to_csv("dados/csvs/recursos.csv", index=False)

    while Global.ganhou:
        rect_mensagem_vitoria.center = (Global.dimensoes_janela[0] // 2, Global.dimensoes_janela[1] // 2)
        Global.tela.blit(mensagem_vitoria_para_tela, rect_mensagem_vitoria)
        display.flip()

        pygame.mixer_music.fadeout(100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    escolha_dificuldade.EscolhaDificuldade()

def ajustar_tela():
    Global.dimensoes_janela = pygame.display.get_surface().get_size()

    # se o x for muito maior que o y
    if Global.dimensoes_janela[0] / Global.dimensoes_janela[1] > proporcao_altura_largura:

        # se eu reduzir o y
        if Global.dimensoes_janela[0] * Global.dimensoes_janela[1] / (dimensao_base[0] * dimensao_base[1]) < Global.proporcao:
            Global.tela = display.set_mode((Global.dimensoes_janela[1] * proporcao_altura_largura, Global.dimensoes_janela[1]), pygame.RESIZABLE)
        # se eu aumentei o x
        else:
            Global.tela = display.set_mode((Global.dimensoes_janela[0], Global.dimensoes_janela[0] / proporcao_altura_largura), pygame.RESIZABLE)
        
        Global.dimensoes_janela = pygame.display.get_surface().get_size()

    # se o y for muito maior que o x
    elif Global.dimensoes_janela[0] / Global.dimensoes_janela[1] < proporcao_altura_largura:

        # se eu diminui o x
        if Global.dimensoes_janela[0] * Global.dimensoes_janela[1] / (dimensao_base[0] * dimensao_base[1]) < Global.proporcao:
            Global.tela = display.set_mode((Global.dimensoes_janela[0], Global.dimensoes_janela[0] / proporcao_altura_largura), pygame.RESIZABLE)
        # se eu aumentei o y
        else:
            Global.tela = display.set_mode((Global.dimensoes_janela[1] * proporcao_altura_largura, Global.dimensoes_janela[1]), pygame.RESIZABLE)
        
        Global.dimensoes_janela = pygame.display.get_surface().get_size()

    Global.proporcao = Global.dimensoes_janela[0] / dimensao_base[0]


# criar um clock de atualização em fps
clock = time.Clock()

    
