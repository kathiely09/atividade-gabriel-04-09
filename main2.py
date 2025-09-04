import pygame
import os

#inicializando o Pygame 
pygame.init()

#definindo o tamanho da janela 
WIDTH, HEIGHT=800, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Janela com Imagem") 

# Definindo a cor do fundo
BG_COLOR = (30, 30, 40)
#loop principal do jogo  # cor de fundo (um tom escuro)

# Carregar a imagem
imagem_file = "player.png" # coloque o nome da sua imagem
if os.path.exists(imagem_file):
    Img = pygame.image.load(image_file).convert_alpha()
    Img_rect = img.get_rect(center=(WIDTH// 2, HEIGHT// 2 )) #centraliza a imagem
else:
    print("Imagem Não encontrada !")

#loop principal do jogo 
running= True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

# Preencher o fundo 
  screen.fill(BG_COLOR)

# Desenhar a imagem da tela
  screen.blit
    #Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()
