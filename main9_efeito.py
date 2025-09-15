Import pygan
Import os
Import time Para controlar o tempo de dano
#Inicializando o Pyga
pygane.init()
Defininde tamanho de janela padrão
MIDTH, HEIGHT 720, 420
screen pygame.display.set_mode((WIDTH, HEIGHT), Pygame. RESIZABLE)
Janela redimensionävel
11 pygame.display.set_caption("Rover Imagen con Setas")
12
13 Definindo a cor de fundo (usada se não houver Leugen de fundo)
14 BG COLOR (193, 0, 40) cor de fundo (um tom escuro)
13
16 Tamanho das imagens dos personagens
17 PLAYER WIDTH, PLAYER HEIGHT 225, 225 Tasarño do jogador
18 TARGET MIDTH, TARGET HEIGHT 225, 225 Tamanho do alvo
Carregar a inagne do personages principal (jogador)
image file "player.png"
22 if os.path.exists(image file);
Sng pygame.image.load(Snuge file).convert_alpha()
ing pygame.transform.scale(img, (PLAYER MIDTH, PLAYER HEIGHT))
RedLensions Leagen
ing recting.get rect(midbotton (MIDTH // 2, HEIGHT)) # inicia no chân
print("Imagen do personagse não encontradal")
Segane
ing rect pygame. Rect(MIDTH // 2, HEIGHT 58, PLAYER MIDTH, PLAYER HEIGHT)
hack no châu
Carregar Iладке dо регsonages alvu (para ser chutado)
target file "patrick.png"
target injured file "target injured.png Inagus nachucada do alvo
If os.path.exists(target_file):
target ing pygane, Image.load(target file).convert alpha()
target ing pygame.transform.scale(targeting, (TARGET MIDTH, TARGET_HEIGHT))
Redlimensiona a twagen
target rect target ing-get_rect(midbotton-(WIDTH //2 200, HEIGHT))
aise:
print("Imagen do personagem alve não encontrada!")
40 target ing None
41 target rect pygame. Rect (WIDTH // 2200, HEIGHT 50, TARGET WIDTH, TARGET HEIGHT)
42
#fallhack no chân
43 Carregar a imagne de fundo
44 Background file "background.png"
45 if os.path.exists(background_file):
background orig pygame.image.load(background_file).cowert()
background pygame.transform.scale(background orig, (WIDTH, HEIGHT))
AT
wlser
background orig - Noon
background None
53
print("Imagen de fundo não encontradal")
53 Velocidade de movimento do jogador
54 SPEED-3
55 JUMP STRENGTH 18
50 GRAVITY.5D a gravidade para que a queda saja mais rápida
57 APPING False
VELOCITY Y
59
50 Variáveis para o alvo chuta
61 target velocity_x
target velocity y
63 target Jumping False
target gravity GRAVITY
65
ontrate
last width, last height WIDTH, HEIGHT
Variavels para controle do dano
target damaged False
71 danage tine tempo en que a imagen sachicade foi exibida
72
73 Limitar sovimento para não sair da tela
24 de limit movement (rect):
75 if rect.left:
76 rect.left-
37 if rect.right> WIDTH:
76 rect.right WIDTH
If rect.top :
rect.top
If rect.bottom> HEIGHT:
81 rect.bottom HEIGHT
Funcão para pular do Jogador
def jump()1
lobal VELOCITY Y, JUMPING
if not. JUMPING:
VELOCITY Y-JUMP STRENGTH
89 JUMPING Trum
91 Atualiza a palo do jogador
def update Jump():
global VELOCITY Y, JUMPING, ing rect, GRAVITY
JAPPING:
ing rect.y + VELOCITY Y
VELOCITY Y GRAVITY
97 if ing rect.bottom HEIGHT:
ing rect.bottom- HEIGHT
APPING False
100 VELOCITY Y
103
102 # Atuuliza o pulo/quada do alve chutado
103 def update_target_physics();
global target velocity x, target velocity y, target jumping, targut rect, targut gravity 164
If target Jumping: 106
105
107 target_velocity_y target gravity
targut rect.x target velocity x
199
target rect.y + target_velocity_y
if target rect.bottom > HEIGHT:
112
118 target jumping = False
114
target nect.bottom- HEIGHT
115 target velocity ye
target velocityx6
136
137 target velocity x 0.95
118
137 Funcilo para "chutar alve
120 def kick():
123 global target velocity x, target_velocity y, target jumping, target rect, ing rect,
dist ytarget_rect.centerying rect.centery 124
target damaged, damage time
122
123 dist x-target_rect.contorxing rect.contarx
224
distancia (dist x2 dist y** 2)* 0.5 125
127 if distancia < 150:
128 target_velocity x 20 if dist x > # else -20
119 targut velocity y-20
133 target damaged True Marca que o alvo fol nachucado
130 target jumping True
132 damage time pygase.tise.get_ticks()Marcas tempo atual
253
134 Detectar colisão entre o jogador e alvo
13 de detect collision():
136 global targeting, target damaged, damage tine
137
134 if target damaged:
#58 0 alvo está danificado, sostrar a Isagam machucada
139
140 if uygame.time.get ticks() damage time 1000:
if os.path.exists(target injured_file):
targeting pygame.image.load(target Injured File).comvert alpha()
target ing pygame.transfors.scale(targeting, (TARGET WIDTH, TARGET HEIGHT
144
else:
145
146
147
LAB
Depois de segundo, retorna à Imagen normal
If os.path.exists(target_file):
141
142
143
target ing pygame.isage.load(target file).convert alpha()
target ing pygame.transfors.scale(targeting, (TARGET MIDTH, TARGET HEIGHT
149
158
target damaged False Reseta o estado de lano
151 Loop principal de jog
152 running True
113 while running:
154 for event in pygame.event.gut():
156
157
158
160
162
163
If event.typerygame.QUIT
running False
Detectar redimensionamento
current width, current height screen.get size()
If current width - last width or current height - last height:
MIDTH, HEIGHT current width, current height
#santer personagens no chão
164 ing rect.botton HEIGHT
145
target rect.bottom HEIGHT
147
170
If background_orig:
background pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
last width, last height current width, current_height
171 Teclas pressionadas
172 keys pyganowy.gut pressed()
173
174 if keys[pygane.K_LEFT]:
175
183
183
184
ing rect.x SPEED
If keys (pygame.K_RIGHT):
ing rect.x SPEED
if keys [pygane.K_UP):
ing rect.y SPEED
if keys [nygan.K DOWN]:
ing rect.y + SPEED
Jump()
if keys [pygane.K_SPACE]:
if keys [pygane.K_f]:
kick()
187 Limit rovement (ing rect)
limit rovement(target_rect)
150
update jump() Atualiza apenas o palo do jilgador principal
update target physics()Atualiza a fisica do alvo chutado
#Detectar colisão
detect collision()
It background:
screen.biit(background, (0, 0))
else:
screen. Fill (BG_COLOR)
if ing:
screen.blit(ing, ing rect.topleft)
else:
pygame.draw.rect(screen, (255, 0, 0), ing rect)
if target ing:
screen.blit(targeting, target rect.topleft)
else:
pygase.draw.rect(screen, (, 255, 0), target_rect)
pygame.display.flip()
pygame.quit()
