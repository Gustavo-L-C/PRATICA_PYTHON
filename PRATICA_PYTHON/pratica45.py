#07.06.25
#PYGAME - 01
#ESTUDO PYGAME - 01

import pygame

# inicializar o jogo
# _________________________________________________________________________________________________________________
pygame.init()

tamanho = (800, 800)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption('Quebrando_Blocos.py')
# _________________________________________________________________________________________________________________
tamanho_bola = 15
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0, 750, tamanho_jogador, 15)
# _________________________________________________________________________________________________________________
qt_blocos_linha = 8
qtd_linhas_blocos = 5
qt_total_blocos = qt_blocos_linha * qtd_linhas_blocos
# _________________________________________________________________________________________________________________
def criar_blocos(qt_blocos_linha, qtd_linhas_blocos):

    distancia = 5
    largura_tela = tamanho[0]
    altura_tela = tamanho[1]
    largura_blocos = largura_tela / 8 - distancia
    altura_blocos = 15
    distancia_entre_linhas = altura_blocos + 10

    blocos = []

    for j in range(qtd_linhas_blocos):

        for i in range(qt_blocos_linha):

            bloco = pygame.Rect(i * (largura_blocos + distancia), j * distancia_entre_linhas, largura_blocos, altura_blocos)
            blocos.append(bloco)

    return blocos
# _________________________________________________________________________________________________________________
cores = {'white': (255,255,255),'black': (0,0,0),'red': (255,0,0),'yellow': (255,255,0),'blue': (0,0,255)}

fim_jogo = False
pontuacao = 0
movimento_bola = [1,-1]

# desenhar coisas na tela
# _________________________________________________________________________________________________________________
def desenhar_jogo():

    tela.fill(cores['black'])
    pygame.draw.rect(tela, cores['white'], jogador)
    pygame.draw.rect(tela, cores['yellow'], bola)
# _________________________________________________________________________________________________________________
def desenhar_blocos(blocos):

    for bloco in blocos:
        pygame.draw.rect(tela, cores['red'], bloco)

# funções do jogo
# _________________________________________________________________________________________________________________
def movimentar_jogador(event):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if (jogador.x + tamanho_jogador) < tamanho[0]:
             jogador.x = jogador.x + 1

        if event.key == pygame.K_LEFT:
            if jogador.x > 0:
                jogador.x = jogador.x - 1
# _________________________________________________________________________________________________________________
def movimentar_bola(bola):

    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = - movimento[0]

    if bola.y <= 0:
        movimento[1] = - movimento[1]

    if bola.x + tamanho_bola >= tamanho[0]:
        movimento[0] = - movimento[0]

    if bola.y + tamanho_bola >= tamanho[1]:
        movimento = None

    if jogador.collidepoint(bola.x, bola.y):

        movimento[1] = - movimento[1]

    for bloco in iniciar_blocos:

        if bloco.collidepoint(bola.x, bola.y):

            iniciar_blocos.remove(bloco)
            movimento[1] = - movimento[1]

    return bola
# _________________________________________________________________________________________________________________
def atualizar_pontuacao(pontuacao):

    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f'Pontuação: {pontuacao}', 1, cores['blue'])
    tela.blit(texto, (0, 780))

    if pontuacao >= qt_total_blocos:
        return True

    else:
        return False

iniciar_blocos = criar_blocos(qt_total_blocos, qtd_linhas_blocos)

# loop infinito até o jogo ser "fechado"
# _________________________________________________________________________________________________________________
while not fim_jogo:

    desenhar_jogo()
    desenhar_blocos(iniciar_blocos)
    fim_jogo = atualizar_pontuacao(qt_total_blocos - len(iniciar_blocos))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            fim_jogo = True

    movimentar_jogador(event)
    movimentar_bola(bola)

    if not movimento_bola:
        fim_jogo = True

    pygame.time.wait(1)
    pygame.display.flip()
# _________________________________________________________________________________________________________________
pygame.quit()
# finalizar do jogo
# estudo do código completo 08.06.25 hj to ocupado pelo menos terminei ele :)