import pygame
from Shot import Bala
from random import choice, randint

class Enimigo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagem = {1: pygame.image.load('imagens/sauders.png'),
                       2: pygame.image.load('imagens/sauders_left.png'),
                       3: pygame.image.load('imagens/sauders_right.png'),
                       4: pygame.image.load('imagens/sauders_down.png')}
        
        self.posImagem = 1
        self.rect = self.imagem[self.posImagem].get_rect()
        
        self.rect.left, self.rect.top = 500, 500
        self.vivo = True
        self.velocidade = 3
        self.listaBala = []
        self.lista_inimigos = []
        self.contador = 0
        self.direita, self.esquerda, self.cima, self.baixo = False, False, True, False
        
    def comportamento(self):
        if self.vivo == True:
            
            self.contador += 1
            self.__direçao()
            self.__mover()
            self.__atacar()
            
            
            if self.contador >= 60:
                self.contador = 0
        
        elif self.vivo == False:
            self.contador += 1
            if self.contador >= 3:
                self.contador = 0
                self.posImagem += 1
                if self.posImagem == 5:
                    self.vivo = None   
        
    
        
    def colocar(self, superficie):
        
        if self.vivo == True:
            superficie.blit(self.imagem[self.posImagem], [self.rect.left, self.rect.top])         
        else :
            superficie.blit(self.imagem[self.posImagem], [self.rect.left, self.rect.top])
        
    def __atacar(self):
        if (randint(0,100)) <= 2 :
            self.__disparar()
       
    def __disparar(self):
        x, y = self.rect.centerx, self.rect.centery
        bala_inimigo = Bala(self.rect.center, self.posImagem)
        self.listaBala.append(bala_inimigo)     
    
    def morrer(self):
        self.vivo = False
        self.imagem = [pygame.image.load('imagens/eplosao1.png'),
                       pygame.image.load('imagens/eplosao2.png'),
                       pygame.image.load('imagens/eplosao3.png'),
                       pygame.image.load('imagens/eplosao4.png'),
                       pygame.image.load('imagens/eplosao5.png'),
                       pygame.image.load('imagens/nave_destruida.png')]
        
        self.posImagem = 0
        self.contador = 0 
    
    def __mover(self):
        if self.contador >= 2 :
            
            if self.direita == True:
                self.rect.move_ip(self.velocidade, 0)
                self.posImagem = 3
                
            elif self.esquerda == True:
                self.rect.move_ip(- self.velocidade, 0)
                self.posImagem = 2
                 
            elif self.cima == True:
                self.rect.move_ip(0, - self.velocidade)
                self.posImagem = 1            
        
            elif self.baixo == True:
                self.rect.move_ip(0, self.velocidade)
                self.posImagem = 4
            
            elif self.esquerda and self.baixo == True:
                self.rect.move_ip(- self.velocidade, self.velocidade)
                self.posImagem = 2

            
            elif self.esquerda and self.cima == True:
                self.rect.move_ip(- self.velocidade, - self.velocidade)
                self.posImagem = 2
            
            elif self.direita and self.baixo == True:
                self.rect.move_ip(self.velocidade, self.velocidade)
                self.posImagem = 3

            
            elif self.direita and self.cima == True:
                self.rect.move_ip(self.velocidade, - self.velocidade)
                self.posImagem = 3
            
            
    def __direçao(self):
        if self.contador == 50:
            self.direita = choice([True, False])
            self.esquerda = choice([True, False])     
            self.cima = choice([True, False])     
            self.baixo = choice([True, False])
            
            
    def __adicionar_inimigos(self):
        pass
        #self.lista_inimigos.append(classe)             
             
         
         
         
         
         
         
         
         