#07.06.25
#PYGAME - 01
#ESTUDO PYGAME - 01

import pygame # biblioteca pygame : jogos

# inicializar o jogo
# _________________________________________________________________________________________________________________

pygame.init() # iniciar a janela

tamanho = (800, 800) # para o tamanho da janela/tela # var

tela = pygame.display.set_mode(tamanho)  # janela/tela do game # var

pygame.display.set_caption('Quebrando_Blocos.py') # titulo da janela/tela do game

# _________________________________________________________________________________________________________________

tamanho_bola = 15 # o tamanho da bola #var

bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola) # criando a bola dentro do game

tamanho_jogador = 100 # tamanho do jogador # var

jogador = pygame.Rect(0, 750, tamanho_jogador, 15) # criando o jogador dentro do game

# _________________________________________________________________________________________________________________

qt_blocos_linha = 8 # definindo a quantidade de blocos por linhas # var

qtd_linhas_blocos = 5 # definindo a quantidade de linhas por blocos # var

qt_total_blocos = qt_blocos_linha * qtd_linhas_blocos # quantidade total de blocos no game # var

# _________________________________________________________________________________________________________________

def criar_blocos(qt_blocos_linha, qtd_linhas_blocos): # criando os blocos dentro do game

    distancia = 5 # distancia entre cada bloco # var

    largura_tela = tamanho[0] # posição dos blocos # var

    altura_tela = tamanho[1] # posição dos blocos # var

    largura_blocos = largura_tela / 8 - distancia # largura de cada bloco # var

    altura_blocos = 15 # altura de cada bloco # var

    distancia_entre_linhas = altura_blocos + 10 # distancia entre cada linha de blocos # var

    blocos = [] # quantidade de blocos do game preenchida "automáticamente"

    for j in range(qtd_linhas_blocos): # para cada bloco nas linhas de blocos # loop

        for i in range(qt_blocos_linha): # para cada bloco por linha # loop

            bloco = pygame.Rect(i * (largura_blocos + distancia), j * distancia_entre_linhas, largura_blocos, altura_blocos) # dita a quantidade de blocos baseado na largura, distancia, altura
            blocos.append(bloco) # adiciona os blocos a lista

    return blocos
# _________________________________________________________________________________________________________________

cores = {'white': (255,255,255),'black': (0,0,0),'red': (255,0,0),'yellow': (255,255,0),'blue': (0,0,255)} # cores que serão utilizadas no game # var

fim_jogo = False # determina quando o jogo acaba # var

pontuacao = 0 # pontuação # var

movimento_bola = [1,-1] # movimento da bola em pixels # var

# desenhar coisas na tela
# _________________________________________________________________________________________________________________

def desenhar_jogo(): # criando os elementos dentro do jogo

    tela.fill(cores['black']) # definindo/criando a tela e a cor da tela

    pygame.draw.rect(tela, cores['white'], jogador) # definindo/criando o jogador e a cor do jogador

    pygame.draw.rect(tela, cores['yellow'], bola) # definindo/criando a bola e a cor da bola

# _________________________________________________________________________________________________________________

def desenhar_blocos(blocos): # criando os blocos dentro do game

    for bloco in blocos: # para cada bloco dentro da lista blocos
        pygame.draw.rect(tela, cores['red'], bloco) # definindo/ criando os blocos e suas cores

# funções do jogo
# _________________________________________________________________________________________________________________

def movimentar_jogador(event): # criando o movimento do jogador # para o jogador não sair da tela

    if event.type == pygame.KEYDOWN: # se o "evento" é teclar

        if event.key == pygame.K_RIGHT: # se o "evento" é teclar a seta para direita

            if (jogador.x + tamanho_jogador) < tamanho[0]: # se a posição do jogador + o tamanho do jogador for menor que a tela # para o jogador não sair da tela

             jogador.x = jogador.x + 1 # o jogador se move no eixo x 1 pixel direita

        if event.key == pygame.K_LEFT: # se o "evento" é teclar a seta para esquerda

            if jogador.x > 0: # se a posição do jogador for maior que 0 (o ponto inicial da tela) # para o jogador não sair da tela

                jogador.x = jogador.x - 1 # o jogador se move no eixo x 1 pixel esquerda

# _________________________________________________________________________________________________________________

def movimentar_bola(bola): # criando o movimento da bola # para a bola não sair da tela

    movimento = movimento_bola # var
    bola.x = bola.x + movimento[0] # bola no eixo x se move 1 pixel (direita / esquerda)
    bola.y = bola.y + movimento[1] # bola no eixo y se move 1 pixel (direita / esquerda)

    if bola.x <= 0: # se bola no eixo x for menor ou igual a 0 (o ponto inicial da tela)
        movimento[0] = - movimento[0] # movimenta 1 pixel

    if bola.y <= 0: # se bola no eixo y for menor ou igual a 0 (o ponto inicial da tela)
        movimento[1] = - movimento[1] # movimenta 1 pixel

    if bola.x + tamanho_bola >= tamanho[0]: # se bola no eixo x + tamanho da bola for maior ou igual a tela # para a bola não sair da tela
        movimento[0] = - movimento[0] # movimenta 1 pixel

    if bola.y + tamanho_bola >= tamanho[1]: # se bola no eixo y + tamanho da bola for maior ou igual a tela # para a bola não sair da tela
        movimento = None # movimenta 1 pixel
        #movimento[1] = - movimento[1]

    if jogador.collidepoint(bola.x, bola.y): # se jogador colidir com a bola

        movimento[1] = - movimento[1]

    for bloco in iniciar_blocos:

        if bloco.collidepoint(bola.x, bola.y): # declarar a colisão da bola

            iniciar_blocos.remove(bloco) # quando a bola colidi com um bloco ele será "removido"
            movimento[1] = - movimento[1] # e a bola irá se movimentar após a colisão

    return bola
# _________________________________________________________________________________________________________________

def atualizar_pontuacao(pontuacao): # criando a pontuação

    fonte = pygame.font.Font(None, 30) # declarando a fonte e tamnho do texto

    texto = fonte.render(f'Pontuação: {pontuacao}', 1, cores['blue']) # texto de pontuação a ser exibido

    tela.blit(texto, (0, 780)) # posição onde o texto ficará dentro da tela

    if pontuacao >= qt_total_blocos: # se pontuação for maior que a quantidade total de blocos
        return True # retorna o valor da pontuação

    else: # se não
        return False # retorna o valor da pontuação

iniciar_blocos = criar_blocos(qt_total_blocos, qtd_linhas_blocos)

# loop infinito até o jogo ser "fechado"
# _________________________________________________________________________________________________________________

while not fim_jogo: # loop do jogo tudo declarado deve estar dentro do loop

    desenhar_jogo() # criação dos objetos do jogo (jogador e bola)

    desenhar_blocos(iniciar_blocos) # criação dos objetos do jogo (blocos)

    fim_jogo = atualizar_pontuacao(qt_total_blocos - len(iniciar_blocos)) # criação da pontuação

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            fim_jogo = True

    movimentar_jogador(event) # movimentação do jogador

    movimentar_bola(bola) # movimentação da bola

    if not movimentar_bola:
        fim_jogo = True

    pygame.time.wait(1)

    pygame.display.flip()

# _________________________________________________________________________________________________________________

pygame.quit() # fim da janela

# _________________________________________________________________________________________________________________
# finalizar do jogo
