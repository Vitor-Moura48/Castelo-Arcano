from Configurações.config import *
from Configurações import Global

# aplica o efeito de buff e começa a contar o tempo para parar o efeito (aumenta a velocidade do player)
def conferir_buffs():

    if Global.tempo_buff_velocidade > 0:

        arquivo_upgrade = pandas.read_csv("dados/csvs/upgrades.csv")
        if arquivo_upgrade.iloc[0, 1]:
            Global.velocidade_player = velocidade_base_player * 1.5 * Global.proporcao
        else:
            Global.velocidade_player = velocidade_base_player * 1.25 * Global.proporcao

    else:
         Global.velocidade_player = velocidade_base_player  * Global.proporcao
    

    if Global.tempo_buff_disparo_teleguiado > 0:
        for projetil in Global.grupo_projeteis_aliados:

            arquivo_upgrade = pandas.read_csv("dados/csvs/upgrades.csv")
            if arquivo_upgrade.iloc[3, 1]:
                raio = 400
            else: 
                raio = 200
            projetil.direcionar(raio)
    