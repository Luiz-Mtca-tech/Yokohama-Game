import pygame
#from Enemy import Enimigo
#from random import randint

class Objetos_Mapa(pygame.sprite.Sprite):
    def __init__(self):
        self.imagem = [pygame.image.load('imagens/home1.png'),
                       pygame.image.load('imagens/arvore.png'),
                       pygame.image.load('imagens/moita.png'),
                       pygame.image.load('imagens/home1.png'),
                       pygame.image.load('imagens/arvore.png'),
                       pygame.image.load('imagens/moita.png'),
                       pygame.image.load('imagens/home1.png'),
                       pygame.image.load('imagens/arvore.png'),
                       pygame.image.load('imagens/moita.png'),
                       pygame.image.load('imagens/home1.png'),
                       pygame.image.load('imagens/arvore.png'),
                       pygame.image.load('imagens/moita.png')]#12, 4 casas, 4 moitas, 4 arvores
        
        self.lista_objtos = []
        
    def colocar(self, superficie):
            
            
            superficie.blit(self.imagem[0], [77, 32])
            superficie.blit(self.imagem[1], [239, 41])
            superficie.blit(self.imagem[2], [155, 32])
            superficie.blit(self.imagem[3], [167, 347])
            superficie.blit(self.imagem[4], [180, 100])
            '''superficie.blit(self.imagem[5], [140, 100])
            superficie.blit(self.imagem[6], [120, 100])
            superficie.blit(self.imagem[7], [400, 100])
            superficie.blit(self.imagem[8], [250, 100])
            superficie.blit(self.imagem[9], [90, 100])
            superficie.blit(self.imagem[10], [100, 100])
            superficie.blit(self.imagem[11], [100, 100])'''
                
    # esta função vai mnover todos os objetos do jogo
    # para a direção apontada
    def mover(lista_objetos):
        pass
                
            
    def destruido(self):
        pass
    
    