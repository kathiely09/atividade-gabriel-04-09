import pygame
import os
pygame.init()
WIDTH, HEIGHT = 1020, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame. RESIZABLE) Janela redimensionavel
pygame.display.set_caption("Mover Imagem com Setas")
BG_COLOR (193, 0, 40) # con de fundo (um tom escuro)
image_file = "player.png"#Coloque o nome correto da sua imagem aqui
if os.path.exists(image file):
img pygame.image.load(image_file).convert_alpha() # Carregar a imagem
img_rect img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) #Centraliza a imagem
else:
print("Imagem do personagem não encontradal")
img- None
img rect pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50) # Retângulo padrão para evitar erro
background file "background.png" # Caminho para sua imagem de fundo
if os.path.exists(background_file):
background_orig pygame.image.load(background_file).convert()
background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
else:
background_orig = None
background - None
print("Imagem de fundo não encontrada!")
SPEED 15 pixels por movimento
JUMP STRENGTH 30 Força do pulo (quanto maior, mais alto o pulo)
GRAVITY = 0.9 Gravidade, fazendo o personagem cair
JUMPING False # Indica se o personagem está no an
VELOCITY Y Velocidade no eiko V (inicialmente sem velocidade de pulo)
def centralize_image():
global img rect, WIDTH, HEIGHT
img rect.center (WIDTH // 2, HEIGHT // 2) Centraliza a imagem no centro da tela
last width, last height WIDTH, HEIGHT
def limit_movement():
global img rect, WIDTH, HEIGHT
if ing rect.left < 0:
img_rect.left = 0
if img_rect.right> WIDTH:
img_rect.right = WIDTH
if ing rect.top < 0:
img rect.top = e
1+ img_rect.bottom > HEIGHT:
img_rect.bottom = HEIGHT
def jump():
Blocal VELOCITY Y, JUMPING
if not JUMPING:
VELOCITY Y-JUMP STRENGTHя в ришо рага cina
JUMPING True
def update jump():
glonal VELOCITY Y, JUMPING, ing rect
1+ JUMPING:
VELOCITY Y + GRAVITY Simula a gravidade
ing_rect.y + VELOCITY_YAtualiza a posicão y de personagen
If img rect.botton > HEIGHT:
img_rect.bottom HEIGHT Garante que o personagem não passe do chão
JUMPING False
VELOCITY YB Reseta a velocidade no eίχο ν
running True
while running:
for event in pygame.event.get():
if event.type = pygame.QUIT:
running = False
current width, current neight = screen.get size()
If current width != last width or current height 1 last_height:
WIDTH, HEIGHT = current_width, current_height
centralize_image() Centraliza a inagem quando a janela mudar de tamanho
If background_orig:
background pygame.transform.scale(background_orig, (WIDTH, HEIGHT)) Redtmensiona fundo a partir da original
last width, last height current width, current_height
keys pygame.key.get_pressed()
It keys [pygame.K_LEFT]
ing rect.x SPEED Hove para a esquerda
It keys [pygame.K RIGHT):
img rect.x += SPEED Hove para a direita
1+ keys pygame. K UP]:
ing rect.y SPEED hove para сіла
if keys pygame. K DOWN]:
img rect.y + SPEED nove para baixo
If keys [pygame.K_SPACE]:
Jump() Ativa o pulo
limit_movement()
update jump()
if background:
screen.blit(background, (0, 0))
eise:
screen.+111(BG COLOR) Caso não teriha tundo, mantén a con de timido
1+1mg:
screen.blit(img, img rect.topleft)
pygame.display.flip()
pygame.quit()
