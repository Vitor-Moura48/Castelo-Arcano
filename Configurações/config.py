import pandas
import pygame
from pygame import *
import sys
from random import randint, uniform
import os
import numpy
import pygbag
import asyncio

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
fonte_descritiva = pygame.font.SysFont("arial", 16, True, False)

informacoes_tela = pygame.display.Info()

dimensao_base = (informacoes_tela.current_w * 0.7, informacoes_tela.current_h * 0.7)

# para cada 1 y de altura, tem n x de alrgura
proporcao_altura_largura =  dimensao_base[0] / dimensao_base[1]

fps = 120

velocidade_base_player = 4 
velocidade_base_projetil = 16
velocidade_base_inimigo = 6

# definir título da tela
display.set_caption("Castelo Arcano")

mensagem_derrota = "você perdeu, pressione enter para continuar"
mensagem_derrota_para_tela = fonte.render(mensagem_derrota, False,  (200, 0, 0))
rect_mensagem_derrota = mensagem_derrota_para_tela.get_rect()

mensagem_vitoria = "você ganhou! pressione enter para continuar"
mensagem_vitoria_para_tela = fonte.render(mensagem_vitoria, True, (255, 255, 0))
rect_mensagem_vitoria = mensagem_vitoria_para_tela.get_rect()