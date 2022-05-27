import pygame

class Bala(pygame.sprite.Sprite):
    def __init__(self, posiçao, trajeto):
        
        self.imagem = [pygame.image.load('imagens/bala.png'),
                       pygame.image.load('imagens/bala2.png')]
        self.posbala = 0
        self.rect = self.imagem[self.posbala].get_rect()

    
        self.rect.left, self.rect.top = posiçao[0], posiçao[1]
        
        self.velocidadeBala = 10
        self.trajeto = trajeto
        
        
    def trejetoria(self):
            
        if self.trajeto == 1 :
            self.rect.move_ip(0, - self.velocidadeBala)
            self.posbala = 0
                
        elif self.trajeto == 2:
            self.rect.move_ip(- self.velocidadeBala, 0)
            self.posbala = 1
            
        elif self.trajeto == 3:
            self.rect.move_ip(self.velocidadeBala, 0)
            self.posbala = 1
                
        elif self.trajeto == 4:
            self.rect.move_ip(0, self.velocidadeBala)
            self.posbala = 0
        
            
    def colocar(self, superficie):
        superficie.blit(self.imagem[self.posbala], [self.rect.left, self.rect.top])
        
        
        
        
        
        
        
        
        
        
        
        
        