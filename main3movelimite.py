Import pygane
Import as
Inicializando Pygane
pygame.init()
Definindo o tamanho de janela padrão
WIDTH, HEIGHT 500, 600
screen pygame.display.set_mode ((MITH, HEIGHT), рудаве. RESIZABLE) Sanela redimensionável
pygame.display.set caption("Hover Imagen con setas")
Definindo a cor de fundo
BG COLOR (193, 6, 40) cor de fundo (us ton escuro)
Corregar Inagen
image file "GAME\\player.png" Coloque o nome correto da sua imagen aqua
If os.path.exists(image file):
ing pygane. Imagr.lond(image file).convert_alpha() Carregar a inagon
ing recting.get rect(center (WIDTH // 2, HEIGHT // 2)) Centraliza a inages
#iser
print("Inagem não encontrada!")
velocidade Ar
SPEED 1 pixels por cimento
Função para centralizar a imagen conforme o tamanho da tela
def centralize_image():
global ing rect, WIDTH, HEIGHT
ing rect.center (WIDTH // 2, HEIGHT // 2) Centraliza a imagen no centro da tela
varláveis para controle de redimensionamento
last width, last height WIΟΤΗ, ΜΕΣΘΗΤ
Linite de movimento para que personages não saia de tela
def limit novement():
global ing rect, MIOTH, HEIGHT
Linita posição da imagen para não sair de tela
if ing rect.left
ing rect.left
fing rect.right:
ing rect.right WIDTH
if ing rect.tope
ing rect.top-0
If ing rect.bottom HEIGHT:
ing rect.botton = HEIGHT
Loop principal do jago
running Trut
while running:
for event. In pygame.event.get():
If event.type pygame.QUIT
running False
Verifica se o tamanno da janela foi alterada
current width, current height screen.get.size()
se a janela foi redimensionado, centraliza a imagen
If current width last width or current height last height:
WIDTH, HEIGHT current width, current height
centralize image() Centraliza a Leagem quando a janela mudar de tamanho
last width, last height current width, current height
a Pega as teclas pressionadas
keys pygame.key.get pressed()
* Harimentação da imagen
1 keys [pygame.K LEFT]:
ing rect.x SPEED ove para a esquerda
keys[pygame.K_RIGHT]:
ing rect.xSPEED ove para a direita
If keys [pygame.K_UP]:
ing rect.y- SPEED nove para cina
14 keys [pygame. Down]:
ing rect.ySPEED Hove para baixo
Linita o novimento para não sair da tela
linit novement().
Preencher funde
screen.111(04 COLOR)
Desenhar a Langen na tela
screen.bitt(img, ing rect.topleft)
Atualizar a tela
pygame.display.flip()
Finalizar o Рудне
pygame.quit()
