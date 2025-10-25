# Baixar o Pygame e Importar o Pygame
import pygame
import random

# inicia o Pygame
pygame.init()
pygame.mixer.init()
# (Encontre um som online e salve como 'acerto.wav')
som_acerto = pygame.mixer.Sound("efect.wav")

# Variáveis Relevantes para o jogo

ALTURA_TELA = 600
LARGURA_TELA = 800

tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
pygame.display.set_caption('Acerte o Alvo')

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 100, 255)

relogio = pygame.time.Clock()
rodando = True

# Largura e altura do alvo
TAMANHO_ALVO = 50
# Cria um retângulo para o alvo em uma posição fixa
alvo_rect = pygame.Rect(375, 275, TAMANHO_ALVO,TAMANHO_ALVO)

ponto = 0

font = pygame.font.SysFont('bahnschrift',35)

while rodando:
    # 1. Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if alvo_rect.collidepoint(event.pos):
                alvo_rect.x = random.randrange(0, LARGURA_TELA - TAMANHO_ALVO)
                alvo_rect.y = random.randrange(0, ALTURA_TELA - TAMANHO_ALVO)
                ponto += 1
                som_acerto.play()
        

    tela.fill(AZUL)

    pygame.draw.rect(tela, VERMELHO, alvo_rect)
    texto_pontos = font.render(f'PONTOS: {ponto}', True, BRANCO)
    tela.blit(texto_pontos,(10,10))

    


    pygame.display.flip()
    relogio.tick(60)



pygame.quit()

