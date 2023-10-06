import pandas
import pygame
from pygame import *
import sys
from random import randint
import os
import numpy


# iniciar o pygame
pygame.init()

# iniciar joisticks
pygame.joystick.init()

# variáveis
plano_de_fundo = pygame.image.load("imagens/cenário.jpg")
plano_de_fundo = pygame.transform.scale(plano_de_fundo, (3000, 1000))

pygame.mixer.music.set_volume(0.9)
musica_fundo = pygame.mixer.music.load("sons/musica de fundo.wav")
pygame.mixer.music.play(-1)

efeito_explosao = pygame.mixer.Sound("sons/explosão.wav")
efeito_morte = pygame.mixer.Sound("sons/morte inimigos.wav")
efeito_vitoria = pygame.mixer.Sound('sons/vitoria.wav')
efeito_derrota = pygame.mixer.Sound('sons/derrota.wav')
efeito_defesa = pygame.mixer.Sound('sons/defesa mágica.wav')

efeito_derrota.set_volume(0.1)
efeito_explosao.set_volume(0.5)
efeito_vitoria.set_volume(0.7)


fonte = pygame.font.SysFont("arial", 30, True, False)


largura_da_tela = 1500
altura_da_tela = 500

proporcao = largura_da_tela * altura_da_tela / 750000

fps = 120

velocidade_projetil = 10
velocidade_inimigo = 10

dificuldade = 0


# obter a resulução da tela do pc
informacao_da_tela = pygame.display.Info()

largura_da_tela = informacao_da_tela.current_w * 0.9
altura_da_tela = informacao_da_tela.current_h * 0.65

# criar a tela
tela = display.set_mode((largura_da_tela, altura_da_tela))


# definir cor da tela
tela.fill((000, 000, 000))

# definir título da tela
display.set_caption("teste jogo 01")