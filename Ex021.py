#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()#inicializando o pygame
pygame.mixer.music.load('one.mp3')    #carregando o audio q ira tocar
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
print('One piece é bom!:)')
#primeira vez q executei fiquei surdo XD