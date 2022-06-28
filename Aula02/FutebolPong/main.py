import pygame

#inicializa a biblioteca PyGame
pygame.init()
#configura o tamanho da janela
janela = pygame.display.set_mode([1280,720])
#configura um texto para a barra de titulo da janela
titulo = pygame.display.set_caption('Pong')
#importa a imagem de fundo de nosso futpong
campoJogo = pygame.image.load("assets/campo.png")
#vencedor
venceu = pygame.image.load("assets/vencedor.png")
#placar
placar1=0
placar1_img = pygame.image.load("assets/pontos/0.png")
placar2=0
placar2_img = pygame.image.load("assets/pontos/0.png")
#inserindo os jogadores na tela
jogador1 = pygame.image.load("assets/jogador1.png")
jogador1_y = 310
jogador1_moveup = False
jogador1_movedown = False
jogador2 = pygame.image.load("assets/jogador2.png")
jogador2_y = 310
#inserindo a bola
bola = pygame.image.load("assets/bola.png")
bola_x = 617
bola_y = 337
bola_direcao = -10
bola_direcao_y = 1

def desenho():
    if placar1 or placar2 < 9:
        janela.blit(campoJogo, (0, 0))
        # posiciona a img a partir do canto superior esquerdo
        janela.blit(jogador1, (50,jogador1_y))
        janela.blit(jogador2, (1150, jogador2_y))
        janela.blit(bola, (bola_x,bola_y)) #centralizada no campo
        janela.blit(placar1_img, (500,50))
        janela.blit(placar2_img, (710,50))
        movimenta_bola()  # faz a movimentação da bola
        movimenta_jogador()  # movimenta o jogador
        movimenta_jogador2()  # movimenta o jogador
    else:
        janela.blit(venceu, (300,330))

def movimenta_bola():
    global bola_x
    global bola_y
    global bola_direcao
    global bola_direcao_y
    global placar1
    global placar1_img
    global placar2
    global placar2_img

    bola_x+=bola_direcao
    bola_y+=bola_direcao_y

    if bola_x < 120: #verifica colisao jogador1
        if jogador1_y < bola_y+23:
            if jogador1_y+146 > bola_y:
                bola_direcao*=-1

    if bola_x > 1100: #verifica colisão jogador2
        if jogador2_y < bola_y+23:
            if jogador2_y+146 > bola_y:
                bola_direcao*=-1

    if bola_y > 685: #limita o mov. bola nas laterais
        bola_direcao_y*=-1
    elif bola_y <= 0:
        bola_direcao_y*=-1

    if bola_x < -50:
        bola_x = 617
        bola_y = 337
        bola_direcao_y *= -1
        bola_direcao *= -1
        placar2 += 1
        placar2_img = pygame.image.load("assets/pontos/"+str(placar2)+".png")
    elif bola_x > 1320:
        bola_x = 617
        bola_y = 337
        bola_direcao_y *= -1
        bola_direcao *= -1
        placar1 += 1
        placar1_img = pygame.image.load("assets/pontos/" + str(placar1) + ".png")

def movimenta_jogador():
    global jogador1_y

    if jogador1_moveup:
        jogador1_y -= 5
    else:
        jogador1_y += 0

    if jogador1_movedown:
        jogador1_y += 5
    else:
        jogador1_y += 0

    if jogador1_y <= 0:
        jogador1_y = 0
    elif jogador1_y >= 575:
        jogador1_y = 575

def movimenta_jogador2():
    global jogador2_y
    jogador2_y=bola_y

#--------- main ----------
executa = True
while executa: #laço permanece em execução enquanto executa for igual a True
    for eventos in pygame.event.get():
        #captura o evento de clicar no "X" da janela para fecha-la
        if eventos.type == pygame.QUIT:
            executa = False
        if eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_w:
                jogador1_moveup = True
            if eventos.key == pygame.K_s:
                jogador1_movedown = True
        if eventos.type == pygame.KEYUP:
            if eventos.key == pygame.K_w:
                jogador1_moveup = False
            if eventos.key == pygame.K_s:
                jogador1_movedown = False

    desenho() #chama a função q desenha os elementos na tela
    pygame.display.update() #mantem a janela do jogo em execução constante
