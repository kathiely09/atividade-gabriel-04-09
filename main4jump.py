Import pygane
Import os
Inicializando o Pygam
pygame.init
()
Definindo o tamanho da janela padra
WIDTH, HEIGHT 800, 600
screen pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # Janela redimensionáve
pygane.display.set_caption "Mover Imagen com Seta)
Derinindo a cor de tund
BG COLOR (193, 6, 40)cor de fundo (un tom escur
A Carnegara inage
image file "player.pn #Coloque o nome correto da sua imagen aqu
If os.path.exists(image_fil
eling pygane.image.load(image_file).convert_alpha() Carregar a inage
ing recting.get rect center (WIDTH // 2, HEIGHT //2)) Centraliza a image
else:
print("Imagem não encontrad
al"
Velocidade do novinent
JUMP STRENGTH 20 Forca do pulo (quanto mator, mais alto o pul
SPEED 2 pixels por noviment
GRAVITY 0.3 Gravidade, fazendo o personagen cal
JUMPING = Falser Indica se o personagen está no a
VELOCITY Y frVelocidade no elko V (Inicialmente sem velocidade de pul
# Furição para centralizar a imagem conforme o tamanho da tel
det centralize_imag():
global img_rect, WIDTH, HEIGH
ingreft.center (WIDTH // 2, HEIGHT // 2) #Centraliza a imagen no centro da tel
Varláveis para controle de redimensionament
last width, last height WIDTH, HEIGH
T
#Linite de movimento para que o personages não saia de te
def limit movemen ():
glonal img rect, WIDTH, HEIGH
#Limita a posição da imagen para não sair da tol
if img_rect.left < :
ing rect.left = 8
if ing rect.right > WIDTH:
img rect.right = WIDTH
it-img.rect.top < 0:
ing rect.top
if img_rect.botton > HEIGHT:
ing rect.bottom HEIGHT
Função para realizar o pul
def jump():
global VELOCITY Y, JUMPIN
11 notGJUMPING:
VELOCITY Y-JUMP STRENGTH #Inicia o polo para cim
JUMPING True
Função para atualizar o novinento do puš
def update Jump():
gional VELOCITY Y, JUMPING, img rec
1f-JUMPING:
VELOCITY Y + GRAVITY Simula a gravidad
img_rect.y + VELOCITY V Atualiza a posição V do personage
#Se o personagen estiver tocando o chão novamente, para o bul
af img rect.bottom> HEIGHT:
ing rect.bottom = HEIGHT Garante que o personagem não passe do chã
JUMPING = False
VELOCITY Y8 Beseta a velocidade no elad
# Loop principal do jog
ounning True
while running:
Y
for event in pygame.event.get
If event(type pygame.QUIT:
running = False
#Verifica se o tamanho da janela foi alterad
current width, current height screen.get size
()
Se a janela foi redimensionada, centraliza a image
dit current_width != last_width or current_height = last_height:
WIDTH, HEIGHT current_width, current_heigh
centralize image() #Centraliza a imagem quando a janela mudar de ta
last width, last height current width, current_heigh
Pega as teclas pressionada
keys pygame.key.get_pressed
()
Movimentação da image
if keys [pygame.K LEF
Timg_rect.x SPEED Move para a esquerd
t
a it keys[pygame.K_RIGH
T]img_rect.x + SPEED Move para a direit
if keys [pygame.K_U
Pling rect.y SPEED Move para cim
if keys [pygame.K DOW
N]img_rect.y + SPEED Move para baix
Pulo (tecla Spac
Ef keys [pygame.K SPAC
Eljump() #Ativa o pul
0
#Limita o novimento para não sair da tel
limit_movement
()
#Atualiza a fisica do pul
update jump
()
Preencher o fund
screen.f111(BG_COLO
R)
Desenhar a imagem na tel
screen.blit(img, img rect.toplef
t)
Atualizar a tel
pygame.display.flip
Finalizar o Pygam
pygame.quit
()
