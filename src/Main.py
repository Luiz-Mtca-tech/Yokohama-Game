import pygame, sys
from Player import Jogador
from Enemy import Enimigo
from map import Mapa
from Entities import Objetos_Mapa

global altura, largura
altura, largura = 600, 800


def Main():
    pygame.init()# iniciando o pygame
    
    tela = pygame.display.set_mode(size=(largura, altura))# criando tela
    pygame.display.set_caption('Yokohama Game') #titulo da tela
    
    relogio = pygame.time.Clock() # criando fps
    
    mapa = Mapa()
    
    objetos = Objetos_Mapa()
    
    jogador = Jogador(altura / 2, largura / 2)
    velocidadex = 0
    velocidadey = 0
    render_sprite = None
    movendo_jogador = None
    
    enimigo = Enimigo()
    
    while True :
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if evento.type == pygame.KEYDOWN:
                
                if evento.key == pygame.K_a:
                    velocidadex = -5
                    render_sprite = 2
                    jogador.posImagem = 2
                    movendo_jogador = True
                    
                if evento.key == pygame.K_s:
                    velocidadey = 5
                    render_sprite = 4
                    jogador.posImagem = 4
                    movendo_jogador = True
                    
                
                if evento.key == pygame.K_d:
                    velocidadex = 5
                    render_sprite = 3
                    jogador.posImagem = 3
                    movendo_jogador = True
                
                if evento.key == pygame.K_w:
                    velocidadey = -5
                    render_sprite = 1
                    jogador.posImagem = 1
                    movendo_jogador = True
                
                if evento.key == pygame.K_SPACE:
                    jogador.disparar()
                
            if evento.type == pygame.KEYUP:
                
                if evento.key == pygame.K_a:
                    velocidadex = 0
                    movendo_jogador = False
                
                if evento.key == pygame.K_s:
                    velocidadey = 0
                    movendo_jogador = False
                
                if evento.key == pygame.K_d:
                    velocidadex = 0
                    movendo_jogador = False
                
                if evento.key == pygame.K_w:
                    velocidadey = 0
                    movendo_jogador = False
        
        relogio.tick(60)        
        tela.fill((0,0,0)) 
         
        #aqui estão todas funções relacionadas ao jogador
        #aos enimigos e os demais objetos
        mapa.colocar(tela)
        mapa.mover_mapa(velocidadex, velocidadey)
        
        objetos.colocar(tela)
        
        #jogador.mover(velocidadex, velocidadey)      
        jogador.colocar(tela, render_sprite)
        
        enimigo.colocar(tela)
        enimigo.comportamento()        
        
        
        if len(jogador.listaBalas) > 0:
            for x in jogador.listaBalas :
                x.colocar(tela)
                x.trejetoria()
                if x.rect.colliderect(enimigo.rect):
                    if enimigo.vivo == True:
                        enimigo.morrer()
                        
                if x.rect.left <= 0 or x.rect.left >= largura or x.rect.top <= 0 or x.rect.top >= altura:
                    jogador.listaBalas.remove(x) 
            
            
        if len(enimigo.listaBala) > 0:
            for x in enimigo.listaBala:
                x.colocar(tela)
                x.trejetoria()
                if x.rect.colliderect(jogador.rect):
                    jogador.perdeu()
                
                if x.rect.left <= 0 or x.rect.left >= largura or x.rect.top <= 0 or x.rect.top >= altura:
                    enimigo.listaBala.remove(x)

        pygame.display.update()        
Main()    



