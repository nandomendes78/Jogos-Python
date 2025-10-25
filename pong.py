import pygame
import random

pygame.init()

LARGURA_TELA = 800
ALTURA_TELA = 600

tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
pygame.display.set_caption('Pong')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Pontuação
# --- NOVO: Fontes ---
fonte_pontos = pygame.font.Font(None, 74) # Fonte padrão, tamanho 74

# --- NOVO: Variáveis do Jogo ---
pontos_1 = 0
pontos_2 = 0

# Raquete
LARGURA_RAQUETE = 15
ALTURA_RAQUETE = 100

# Classe: Bloco de código
# Método: (Molde) - Ações que Realiza
class Raquete:
    # O 'construtor': é chamado quando criamos uma Raquete
    # 'self' se refere ao próprio objeto
    # Função - init fala o que vai acontecer quando eu criar uma raquete
    def __init__(self, x, y):
         # O 'rect' armazena a posição (x,y) e o tamanho
        self.rect = pygame.Rect(x, y, LARGURA_RAQUETE, ALTURA_RAQUETE)

    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)

    def mover(self,tecla_cima, tecla_baixo):

        teclas = pygame.key.get_pressed()

        # Para subir
        if teclas[tecla_cima] and self.rect.top > 0:
            self.rect.y -= 8
        if teclas[tecla_baixo] and self.rect.bottom < 600:
            self.rect.y += 8

raquete1 = Raquete(10, 300)
raquete2 = Raquete(780, 300)


# --- NOVO: Constantes da Bola ---
RAIO_BOLA = 10
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5

# --- NOVO: Classe Bola ---
class Bola:
    # ... (init, desenhar, mover, verificar_colisao) ...
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - RAIO_BOLA, y - RAIO_BOLA, RAIO_BOLA * 2, RAIO_BOLA * 2)
        # Inicia com velocidade aleatória para X e Y
        self.vel_x = VELOCIDADE_BOLA_X * random.choice((1, -1))
        self.vel_y = VELOCIDADE_BOLA_Y * random.choice((1, -1))

    def desenhar(self, tela):
        pygame.draw.ellipse(tela, BRANCO, self.rect) # Desenha um círculo

    def mover(self):
        # Atualiza a posição X e Y com base na velocidade
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def verificar_colisao(self, raquete1, raquete2):
        # Se a bola bateu na parede
        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            self.vel_y *= -1

        # Se a bola bateu na raquete    
        if self.rect.colliderect(raquete1) or self.rect.colliderect(raquete2):
            self.vel_x *= -1



     # --- NOVO ---
    def resetar(self):
        # Move a bola de volta ao centro
        self.rect.x = LARGURA_TELA / 2 - RAIO_BOLA
        self.rect.y = ALTURA_TELA / 2 - RAIO_BOLA
        # Inverte a direção (para quem pontuou sacar) e dá uma pausa
        self.vel_x *= -1
        self.vel_y = VELOCIDADE_BOLA_Y * random.choice((1, -1))
        pygame.time.delay(1000) # Pausa por 1 seg


# --- Objetos do Jogo ---
# ... (raquetes) ...

# --- NOVO ---
bola = Bola(LARGURA_TELA / 2, ALTURA_TELA / 2)

relogio = pygame.time.Clock()

rodando = True
while rodando:

    # 1. Eventos
    # 1. Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)
    raquete1.desenhar(tela)
    raquete1.mover(pygame.K_w, pygame.K_s)
    raquete2.desenhar(tela)
    raquete2.mover(pygame.K_UP, pygame.K_DOWN)
    
    bola.mover()
    bola.desenhar(tela)

    # --- NOVO ---
    # Passamos os 'rects' das raquetes para a bola checar
    bola.verificar_colisao(raquete1.rect, raquete2.rect)

    if bola.rect.left < 0:
            pontos_2 += 1 
            bola.resetar()

    if bola.rect.right > LARGURA_TELA:
            pontos_1 += 1 
            bola.resetar()
    pygame.display.flip()

    relogio.tick(60)

pygame.quit()