import pygame
pygame.init()
x = 430
y = 570
velocidade = 10
fundo = pygame.image.load('tela.png')
carro = pygame.image.load('carrinho.png')

# Cria uma janela de resolução 628x628
janela = pygame.display.set_mode((625, 625))
pygame.display.set_caption("Criando jogo com Python")

# Faz com que a janela do game fique aberta até ocorrer um evento
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade

    janela.blit(fundo, (0,0))
    janela.blit(carro, (x, y))
    # janela.fill(fundo, (0,0)) Fundo preto

    # Método que desenha algo na tela (parâmetros => janela, cor, localização, raio)         
    # pygame.draw.circle(janela, (255,105,180), (x, y), (20))
    pygame.display.update()

pygame.quit()