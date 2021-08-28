import pygame
from Shot import Bala


class Jogador(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        
        self.posX = posX
        self.posY = posY
        
        self.listaImagens = {1: pygame.image.load('imagens/yokohama.png'),
                             2: pygame.image.load('imagens/yokohama_left.png'),
                             3: pygame.image.load('imagens/yokohama_right.png'),
                             4: pygame.image.load('imagens/yokohama_down.png')}
        
        self.posImagem = 4
        
        self.rect = self.listaImagens[self.posImagem].get_rect()
        self.rect.left, self.rect.top = self.posX / 2, self.posY / 2
        
        self.velocidade = 0.5
        self.listaBalas = []
        self.FimDeJogo = False
        self.contador = 0
        
        
    def colocar(self, superficie, index):
        if self.FimDeJogo == False:
            superficie.blit(self.listaImagens[self.posImagem], [self.rect.left, self.rect.top])
            
        elif self.FimDeJogo == True :
            self.contador += 1
            superficie.blit(self.listaImagens[self.posImagem], [self.rect.left, self.rect.top])
            if self.contador >= 3:
                self.contador = 0
                self.posImagem += 1
                if self.posImagem == 5:
                    self.FimDeJogo = None    
                
    def mover(self, vx, vy):
        if self.FimDeJogo == False:
            self.rect.move_ip(vx, vy)
        
    def disparar(self):
        if self.FimDeJogo == False:
            bala = Bala(self.rect.center, self.posImagem)
            self.listaBalas.append(bala)
        
    def perdeu(self):
        if self.FimDeJogo == False:
            self.FimDeJogo = True
            self.listaImagens = [pygame.image.load('imagens/eplosao1.png'),
                                 pygame.image.load('imagens/eplosao2.png'),
                                 pygame.image.load('imagens/eplosao3.png'),
                                 pygame.image.load('imagens/eplosao4.png'),
                                 pygame.image.load('imagens/eplosao5.png'),
                                 pygame.image.load('imagens/moita.png')]
            self.posImagem = 0        
           
            
            
            
            
            
    
    