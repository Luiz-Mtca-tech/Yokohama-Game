import pygame
from Entities import Objetos_Mapa

class Mapa(pygame.surface.Surface):
    def __init__(self):
        self.imagem = pygame.image.load('imagens/map.png')
        self.posicaoX = 0
        self.posicaoY = 0
        
        self.limiteX = 1000
        self.limiteY = 1000
        
        self.rect = self.imagem.get_rect()
        
    def colocar(self, superficie):
        superficie.blit(self.imagem, (self.posicaoX, self.posicaoY))
            
    def mover_mapa(self, velocidadex, velocidadey):
        self.rect.move_ip(velocidadex, velocidadey)
        self.posicaoX += velocidadex
        self.posicaoY += velocidadey
        #self.__limite()
        print(f'X: {self.posicaoX} -- Y: {self.posicaoY}')
        
    
    def limite(self):
        if self.posicaoX >= self.limite:
            print('passou do limite')                     
        
