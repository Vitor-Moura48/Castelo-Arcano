from Configurações.config import *
from Configurações import Variaveis_globais, Controles
from mobs import Player, Inimigo_01, Inimigo_02, Inimigo_03, Castelo, Boss_01
from Efeitos import buff_01, buff_02, buff_03, buff_04, buff_05
from Verificações import Colisoes
from Telas import menu_principal, escolha_dificuldade, opcoes_em_jogo

def conferir_arquivos_csv():
    if not os.path.exists("csvs/upgrades.csv"):
        arquivo = pandas.DataFrame({'coluna1': [False, False, False, False, False],
                                    'coluna2': [False, False, False, False, False],
                                    'coluna3': [False, False, False, False, False]})
        arquivo.to_csv("csvs/upgrades.csv", index=False)
    
    if not os.path.exists("csvs/recursos.csv"):
        arquivo = pandas.DataFrame({'cristais': [0]})
        arquivo.to_csv("csvs/recursos.csv", index=False)

def chamar_menu_principal():
    menu_principal.menu_principal()

def adicioanr_objetos():

    # adicionar objetos
    if Variaveis_globais.inimigos_restantes < (Variaveis_globais.inimigos_totais * 0.1) and Variaveis_globais.contador_de_bosses == 0 and len(Variaveis_globais.grupo_todos_inimigos) < Variaveis_globais.inimigos_restantes:
        for i in range(1):
            boss_01 = Boss_01.SpritesBoss1(10, 5)
            Variaveis_globais.todas_as_sprites.add(boss_01)
            Variaveis_globais.grupo_todos_inimigos.add(boss_01)
            Variaveis_globais.grupo_todos_bosses.add(boss_01)
            Variaveis_globais.contador_de_bosses += 1

    if len(Variaveis_globais.grupo_inimigos1) < 2 and len(Variaveis_globais.grupo_todos_inimigos) < Variaveis_globais.inimigos_restantes:
        for i in range(1):
            inimigo1 = Inimigo_01.SpritesInimigo1(1, 1)
            Variaveis_globais.todas_as_sprites.add(inimigo1)
            Variaveis_globais.grupo_inimigos1.add(inimigo1)
            Variaveis_globais.grupo_todos_inimigos.add(inimigo1)

    if len(Variaveis_globais.grupo_inimigos2) < 1 and len(Variaveis_globais.grupo_todos_inimigos) < Variaveis_globais.inimigos_restantes:
        for i in range(1):
            inimigo2 = Inimigo_02.SpritesInimigo2(1, 1)
            Variaveis_globais.todas_as_sprites.add(inimigo2)
            Variaveis_globais.grupo_inimigos2.add(inimigo2)
            Variaveis_globais.grupo_todos_inimigos.add(inimigo2)
    
    if len(Variaveis_globais.grupo_inimigos3) < 1 and len(Variaveis_globais.grupo_todos_inimigos) < Variaveis_globais.inimigos_restantes:
        for i in range(1):
            inimigo3 = Inimigo_03.SpritesInimigo3(3, 5)
            Variaveis_globais.todas_as_sprites.add(inimigo3)
            Variaveis_globais.grupo_inimigos3.add(inimigo3)
            Variaveis_globais.grupo_todos_inimigos.add(inimigo3)
    
    # porcentagem de aparecimento a cada iteração
    chance = 0.05
    chance1 = uniform(0, 100)

    if len(Variaveis_globais.grupo_todos_efeitos) < 2 and chance1 <= chance:
        efeito_buff1 = buff_01.SpritesEfeito1()
        Variaveis_globais.todas_as_sprites.add(efeito_buff1)
        Variaveis_globais.grupo_efeito1.add(efeito_buff1)
        Variaveis_globais.grupo_todos_efeitos.add(efeito_buff1)

    chance2 = uniform(0, 100)

    if len(Variaveis_globais.grupo_todos_efeitos) < 2 and chance2 <= chance:
        efeito_buff2 = buff_02.SpritesEfeito2()
        Variaveis_globais.todas_as_sprites.add(efeito_buff2)
        Variaveis_globais.grupo_efeito2.add(efeito_buff2)
        Variaveis_globais.grupo_todos_efeitos.add(efeito_buff2)
    
    chance3 = uniform(0, 100)

    if len(Variaveis_globais.grupo_todos_efeitos) < 2 and chance3 <= chance:
        efeito_buff3 = buff_03.SpritesEfeito3()
        Variaveis_globais.todas_as_sprites.add(efeito_buff3)
        Variaveis_globais.grupo_efeito3.add(efeito_buff3)
        Variaveis_globais.grupo_todos_efeitos.add(efeito_buff3)

    chance4 = uniform(0, 100)
    
    if len(Variaveis_globais.grupo_todos_efeitos) < 2 and chance4 <= chance:
        efeito_buff4 = buff_04.SpritesEfeito4()
        Variaveis_globais.todas_as_sprites.add(efeito_buff4)
        Variaveis_globais.grupo_efeito4.add(efeito_buff4)
        Variaveis_globais.grupo_todos_efeitos.add(efeito_buff4)
    
    chance5 = uniform(0, 100)
    
    if len(Variaveis_globais.grupo_todos_efeitos) < 2 and chance5 <= chance:
        efeito_buff5 = buff_05.SpritesEfeito5()
        Variaveis_globais.todas_as_sprites.add(efeito_buff5)
        Variaveis_globais.grupo_efeito5.add(efeito_buff5)
        Variaveis_globais.grupo_todos_efeitos.add(efeito_buff5)

    # adiconar objetos sprites na tela
    Variaveis_globais.todas_as_sprites.draw(Variaveis_globais.tela)
    Variaveis_globais.todas_as_sprites.update()


def verificar_colisoes():
    Colisoes.colisoes.colisao_com_player()
    Colisoes.colisoes.colisao_com_castelo()
    Colisoes.colisoes.colisao_com_projetil_player()
    Colisoes.colisoes.saiu_do_mapa()


def criar_texto_na_janela():
    
    mensagem_kills = f"inimigos restantes: {Variaveis_globais.inimigos_restantes}"
    mensagem_kills_para_tela = fonte.render(mensagem_kills, True, (80, 80, 255))

    mensagem_vidas_castelo = f"vidas restantes: {Variaveis_globais.vidas_castelo}"
    mensagem_vidas_castelo_para_tela = fonte.render(mensagem_vidas_castelo, True, (247, 24, 14))

    mensagem_barreira = f'defesa: {Variaveis_globais.barreira}'
    mensagem_barreira_para_tela = fonte.render(mensagem_barreira, True, (255, 100, 20))

    # colocar o texto na janela
    Variaveis_globais.tela.blit(mensagem_kills_para_tela, (Variaveis_globais.dimensoes_janela[0] * 0.7, Variaveis_globais.dimensoes_janela[1] * 0.02))
    Variaveis_globais.tela.blit(mensagem_vidas_castelo_para_tela, (Variaveis_globais.dimensoes_janela[0] * 0.02, Variaveis_globais.dimensoes_janela[1] * 0.02))
    if Variaveis_globais.barreira > 0:
        Variaveis_globais.vidas_castelo
        Variaveis_globais.tela.blit(mensagem_barreira_para_tela, (Variaveis_globais.dimensoes_janela[0] * 0.08, Variaveis_globais.dimensoes_janela[1] * 0.08))

def contabilizar_tempo_recargas():
    Variaveis_globais.tempo_de_recarga_disparo -= 1
    Variaveis_globais.tempo_buff_3_projeteis -= 1
    Variaveis_globais.tempo_buff_velocidade_disparo -= 1
    Variaveis_globais.tempo_buff_disparo_teleguiado -= 1

def responder_a_eventos():
    # responder a eventos
    for event in pygame.event.get():

        if event.type == QUIT:
            print("game over")
            quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and Variaveis_globais.tempo_de_recarga_disparo <= 0:

            if Variaveis_globais.tempo_buff_3_projeteis > 0:
                    
                    arquivo_upgrade = pandas.read_csv("csvs/upgrades.csv")

                    if arquivo_upgrade.iloc[2, 1] == True:
                        quantidade_projeteis = 5
                    else:
                        quantidade_projeteis = 3

                    amplitude_entre_projeteis = (Variaveis_globais.amplitude_projeteis * 2) / (quantidade_projeteis - 1) # amplitude positiva e negativa, dividido pela quantidade de projeteis menos 1
                    somador_amplitude = -Variaveis_globais.amplitude_projeteis
 
                    for i in range(quantidade_projeteis):
                        projetil_player = Player.Projetil(1, 1)
                        Variaveis_globais.grupo_projeteis_aliados.add(projetil_player)
                        Variaveis_globais.todas_as_sprites.add(projetil_player)
                        projetil_player.atirar(somador_amplitude)

                        
                        Variaveis_globais.tempo_de_recarga_disparo = 60
                        # aumenta em 10 x a velocidade de disparo
                        if Variaveis_globais.tempo_buff_velocidade_disparo >= 0:
                            Variaveis_globais.tempo_de_recarga_disparo *= 0.1
               
                        somador_amplitude += amplitude_entre_projeteis

            else:
                
                projetil_player = Player.Projetil(1, 1)
                Variaveis_globais.grupo_projeteis_aliados.add(projetil_player)
                Variaveis_globais.todas_as_sprites.add(projetil_player)
                projetil_player.atirar(0)

                Variaveis_globais.tempo_de_recarga_disparo = 60
                # aumenta em 10 x a velocidade de disparo
                if Variaveis_globais.tempo_buff_velocidade_disparo >= 0:
                    arquivo_upgrade = pandas.read_csv("csvs/upgrades.csv")

                    if arquivo_upgrade.iloc[3, 1] == True:
                        Variaveis_globais.tempo_de_recarga_disparo *= 0.05
                    else:
                        Variaveis_globais.tempo_de_recarga_disparo *= 0.1

        # responde aos eventos do controle
        if event.type == JOYDEVICEADDED:
            Controles.controle.__init__()

        if event.type == pygame.JOYAXISMOTION:
            Controles.controle.movimento(event)
        
        if event.type == pygame.VIDEORESIZE:
            ajustar_tela()
    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                opcoes_em_jogo.tela_opcoes()

def gerenciar_waves(): 
    if Variaveis_globais.inimigos_restantes <= Variaveis_globais.inimigos_totais * 0.8 and not Variaveis_globais.mudanca_de_velocidade[0]:
            Variaveis_globais.velocidade_inimigo *= 1.04
            Variaveis_globais.mudanca_de_velocidade[0] = True

    elif Variaveis_globais.inimigos_restantes <= Variaveis_globais.inimigos_totais * 0.6 and not Variaveis_globais.mudanca_de_velocidade[1]:
        Variaveis_globais.velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[1] = True

    elif Variaveis_globais.inimigos_restantes <= Variaveis_globais.inimigos_totais * 0.4 and not Variaveis_globais.mudanca_de_velocidade[2]:
        Variaveis_globais.velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[2] = True

    elif Variaveis_globais.inimigos_restantes <= Variaveis_globais.inimigos_totais * 0.2 and not Variaveis_globais.mudanca_de_velocidade[3]:
        Variaveis_globais.velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[3] = True

def verificar_derrota_vitoria():
    if Player.player.vida_restante <= 0:
        responder_a_derrota()

    if Variaveis_globais.vidas_castelo <= 0:
        responder_a_derrota()

    # resposta para vitória
    if Variaveis_globais.inimigos_restantes <= 0:
        responder_a_vitoria()

    
def responder_a_derrota():
    Variaveis_globais.perdeu = True
    if Variaveis_globais.som_ligado:
        efeito_derrota.play()

    while Variaveis_globais.perdeu:
        rect_mensagem_derrota.center = (Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2)
        Variaveis_globais.tela.blit(mensagem_derrota_para_tela, rect_mensagem_derrota)
        display.flip()

        pygame.mixer_music.fadeout(100) 

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    escolha_dificuldade.iniciar_jogo()


def responder_a_vitoria():
    Variaveis_globais.ganhou = True
    if Variaveis_globais.som_ligado:
        efeito_vitoria.play()

    if Variaveis_globais.dificuldade == 1:

        novo_dataframe = pandas.DataFrame(data=[Variaveis_globais.vidas_castelo], columns=['Recorde'])
        novo_dataframe.to_csv('csvs/recorde_fácil.csv', mode='a', index=False, header=False)

        arquivo_recursos = pandas.read_csv("csvs/recursos.csv")
        arquivo_recursos['cristais'] += 1
        arquivo_recursos.to_csv("csvs/recursos.csv", index=False)

    if Variaveis_globais.dificuldade == 2:

        novo_dataframe = pandas.DataFrame(data=[Variaveis_globais.vidas_castelo], columns=['Recorde'])
        novo_dataframe.to_csv('csvs/recorde_médio.csv', mode='a', index=False, header=False)

        arquivo_recursos = pandas.read_csv("csvs/recursos.csv")
        arquivo_recursos['cristais'] += 2
        arquivo_recursos.to_csv("csvs/recursos.csv", index=False)

    if Variaveis_globais.dificuldade == 3:

        novo_dataframe = pandas.DataFrame(data=[Variaveis_globais.vidas_castelo], columns=['Recorde'])
        novo_dataframe.to_csv('csvs/recorde_difícil.csv', mode='a', index=False, header=False)

        arquivo_recursos = pandas.read_csv("csvs/recursos.csv")
        arquivo_recursos['cristais'] += 3
        arquivo_recursos.to_csv("csvs/recursos.csv", index=False)

    while Variaveis_globais.ganhou:
        rect_mensagem_vitoria.center = (Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2)
        Variaveis_globais.tela.blit(mensagem_vitoria_para_tela, rect_mensagem_vitoria)
        display.flip()

        pygame.mixer_music.fadeout(100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    escolha_dificuldade.iniciar_jogo()

def ajustar_tela():
    Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()

    # se o x for muito maior que o y
    if Variaveis_globais.dimensoes_janela[0] / Variaveis_globais.dimensoes_janela[1] > proporcao_altura_largura:

        # se eu reduzir o y
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

    Variaveis_globais.proporcao = Variaveis_globais.dimensoes_janela[0] / dimensao_base[0]

    Castelo.castelo.rect_ajustado = pygame.Rect.inflate(Castelo.castelo.rect, int(Castelo.castelo.rect_base.width * Variaveis_globais.proporcao - Castelo.castelo.rect.width), int(Castelo.castelo.rect_base.height * Variaveis_globais.proporcao - Castelo.castelo.rect.height))
    Castelo.castelo.rect = Castelo.castelo.rect_ajustado

    retangulo_ajustado = pygame.Rect.inflate(Player.player.rect, int(Player.player.rect_base.width * Variaveis_globais.proporcao - Player.player.rect.width), int(Player.player.rect_base.height * Variaveis_globais.proporcao - Player.player.rect.height))
    Player.player.rect = retangulo_ajustado

# criar um clock de atualização em fps
clock = time.Clock()

    
