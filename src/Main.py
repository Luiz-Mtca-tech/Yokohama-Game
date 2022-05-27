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
    
    jogador = Jogador(45, 20)
    velocidadex = 0
    velocidadey = 0
    render_sprite = None
    movendo_jogador = None
    
    enimigos = []#Enimigo(750, 100), Enimigo(750, 550)]
    #enimigo = Enimigo()
    
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
        objetos.colocar(tela,mapa.posicaoX,mapa.posicaoY)
        jogador.colocar(tela, render_sprite)

        print(f'x: {jogador.posX}, y: {jogador.posY}')
        jogador.posX += velocidadey
        jogador.posY += velocidadey
        if jogador.posX > 380:
            if jogador.FimDeJogo == False:
                mapa.mover_mapa(-velocidadex, -velocidadey)
        if jogador.posY > 280:
            if jogador.FimDeJogo == False:
                mapa.mover_mapa(-velocidadex, -velocidadey)           
        if jogador.posY > 280 or jogador.posX > 380:
            if jogador.FimDeJogo == False:
                mapa.mover_mapa(-velocidadex, -velocidadey)
        
        else :
            mapa.posicaoX = mapa.posicaoX
            mapa.posicaoY = mapa.posicaoY
            jogador.mover(velocidadex, velocidadey)
        
        for i in enimigos:
            i.colocar(tela, mapa.posicaoX,mapa.posicaoY)
            i.comportamento()      
        

        if len(jogador.listaBalas) > 0:
            for x in jogador.listaBalas :
                x.colocar(tela)
                x.trejetoria()
                for i in enimigos :
                    if x.rect.colliderect(i.rect):
                        if i.vivo == True:
                            i.morrer()
                        
                if x.rect.left <= 0 or x.rect.left >= largura or x.rect.top <= 0 or x.rect.top >= altura:
                    jogador.listaBalas.remove(x) 
            
        for i in enimigos:    
            if len(i.listaBala) > 0:
                for x in i.listaBala:
                    x.colocar(tela)
                    x.trejetoria()
                    if x.rect.colliderect(jogador.rect):
                        jogador.perdeu()
                    
                    if x.rect.left <= 0 or x.rect.left >= largura or x.rect.top <= 0 or x.rect.top >= altura:
                        i.listaBala.remove(x)

        pygame.display.update()        
Main()    



