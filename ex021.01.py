# Tocando um MP3
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input() # Necessário para iniciar o play

