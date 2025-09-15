1 import pygame
2 import os
3
4 # Inicializando o Pygame
5 pygame.init()
6
7 # Definindo o tamanho da janela padrão
8 WIDTH, HEIGHT = 720, 420
9 screen pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
# Janela redimensionável
10 pygame.display.set_caption("Mover Imagem com Setas")
11
12 # Definindo a cor de fundo (usada se não houver imagem de fundo)
13 BG_COLOR (193, 0, 40) # cor de fundo (um tom escuro)
14
15 # Tamanho das imagens dos personagens
16 PLAYER WIDTH, PLAYER_HEIGHT = 50, 50 # Tamanho do jogador
17 TARGET_WIDTH, TARGET_HEIGHT = 50, 50# Tamanho do alvo
18
19 # Carregar a imagem do personagem principal (jogador)
20 image_file "player.png"
21. if os.path.exists(image_file):
22 img pygame.image.load(image_file).convert_alpha()
23 img pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
#Redimensiona a imagem
24 img_rect = img.get_rect(midbottom=(WIDTH // 2, HEIGHT)) # inicia no chão
25 else:
26 print("Imagem do personagem não encontrada!")
27 img = None
28 img_rect pygame. Rect(WIDTH // 2, HEIGHT 50, PLAYER_WIDTH, PLAYER_HEIGHT)
29
#fallback no chão
30 # Carregar a imagem do personagem alvo (para ser chutado)
31 target_file = "patrick.png"
32 if os.path.exists(target_file):
33 target_img = pygame.image.load(target_file).convert_alpha()
34 target_img = pygame.transform.scale(target_img, (TARGET_WIDTH, TARGET_HEIGHT))
#Redimensiona a imagem
35 target_rect=target_img.get_rect(midbottom=(WIDTH // 2 + 200, HEIGHT))
#também no chão
36 else:
37 print("Imagem do personagem alvo não encontrada!")
target_img = None 38
39 target_rect = pygame.Rect (WIDTH // 2 + 200, HEIGHT 50, TARGET_WIDTH, TARGET_HEIGHT)
#fallback no chão
40
41# Carregar a imagem de fundo
42 background_file = "background.png"
43 if os.path.exists(background_file):
background_orig pygame.image.load(background_file).convert() 44
background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT)) 45
46 else:
47 background_orig = None
48 background = None
49 print("Imagem de fundo não encontrada!")
50
51# Velocidade de movimento do jogador
52 SPEED = 3
53 JUMP STRENGTH = 18
54 GRAVITY = 0.3
55 JUMPING = False
56 VELOCITY Y = 0
57
58 # Variáveis para o alvo chutado
59 target_velocity_x = 0
60 target_velocity_y = 0
61 target jumping = False
62 target gravity = GRAVITY
63
64 # Controle redimensionamento
65 last_width, last_height = WIDTH, HEIGHT
66
67 # Limitar movimento para não sair da tela
68 def limit_movement(rect):
69 if rect.left < 0:
70 rect.left = 0
71 if rect.right > WIDTH:
72 rect.right = WIDTH
73 if rect.top < 0:
74 rect.top = 0
75 if rect.bottom > HEIGHT:
76 rect.bottom = HEIGHT
77
78 # Função para pular do jogador
79 def jump():
80 global VELOCITY_Y, JUMPING
01 if not JUMPING
81 if not JUMPING:
82 VELOCITY V-JUMP STRENGTH
83 JUMPING True
85
85 Atualiza o pulo do jogador
86 def update jump():
87 global VELOCITY Y, JUMPING, img rect, GRAVITY
89 VELOCITY Y + GRAVITY
00 img_rect.y += VELOCITY_Y
91 if img_rect.bottom = HEIGHT:
92
img_rect.bottom = HEIGHT
JUMPING False
94 VELOCITY y = 0
95
if JUMPING:
06 # Atualiza o pulo / queda do alvo chutado
97 def update_target_physics():
global target_velocity_x, target_velocity_y, target_jumping, target_rect, target_gravity 08
If target jumping: 100
target velocity y target gravity
target_rect.y += target_velocity_y 103
99
101
102
target rect.x + target velocity x
104
if target_rect.bottom = HEIGHT:
205
106
target rect.bottom HEIGHT
107
target jumping - False
108
target_velocity xe
109
target_velocity_y = 0
110
else:
111
target_velocity_x = 0.95
112
113 # Função para "chutar o alvo
114 def kick():
global target_velocity_x, target_velocity_y, target_jumping, target_rect, img_rect 115
116
target_rect.centerx img rect.centerx dist_x
117
target_rect.centery img rect.centery 118 dist y
119
distancia (dist x2 dist y2)**8.5
120
121 if distancia < 150:
122 target_velocity_x 20 if dist x > 0 else -20
123 target_velocity y -20
125
124 target jumping True
126 Loop principal do fogo
127 running = True
128 while running:
for event in pygame.event.get():
129
132
it event.type == pygame.QUIT: 130
running = False 131
#Detectar redimensionamento 133
current width, current height screen.get_size() 134
if current width I last width or current height 1 last height: 135
136
137
WIDTH, HEIGHT current width, current height
138 #manter personagens no chão
139 img_rect.bottom = HEIGHT
140
141
target_rect.bottom = HEIGHT
142
if background_orig:
143
background pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
144
last width, last height current width, current height
ma
145
146 #Teclas pressionadas
147 keys pygame,key.get pressed()
1148
1149
1+ keys[pygame.K_LEFT]:
158
img_rect.x= SPEED
151
1+ keys[pygame.K_RIGHT]:
152
img rect.x + SPEED
153
if keys [pygame.K_UP]:
154
155
img rect.y-- SPEED
If keys[pygame.K DOWN]:
156
img_rect.y + SPEED
157
if keys[pygame.K_SPACE]:
158
Jump()
159
if keys [pygame.K_f]:
160
kick()
161
162
163
limit_movement(ing_rect)
164
limit_movement(target_rect)
165
156
update jump()
167
update_target_physics()
168
1169
If background:
screen.blit(background, (8, 0))
171
170
else:
172
screen.fill(BG_COLOR)
173
174
if img:
1175
screen.blit(img, ing rect.topleft)
176
else:
177
pygame.draw.rect(screen, (255, 0, 0), img rect)
178
179
14 target_img:
180
screen.blit(target_ing, target_rect.topleft)
181
else:
152
pygame.draw.rect(screen, (6, 255, 0), target_rect)
183
184
pygame.display.flip()
185
186 pygame.quit()
187
