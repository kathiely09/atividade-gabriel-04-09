1 import pygame
2 import os
3
4 # Inicializando o Pygame
5 pygame.init()
7 # Definindo o tamanho da janela padrão
8 WIDTH, HEIGHT = 720, 420
9 screen pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # Janela redimension
10 pygame.display.set_caption("Mover Imagem com Setas")
11
12 # Definindo a cor de fundo (usada se não houver imagem de fundo)
13 BG_COLOR (8, 8, 95) # cor fallback
14
15 # Carregar a imagem do personagem principal (jogador)
16 image_file = "player.png"
17 if os.path.exists(image_file):
18 img = pygame.image.load(image_file).convert_alpha()
19 img_rect img.get_rect(midbottom=(WIDTH // 2, HEIGHT)) # jogador sempre no chão
20 else:
21 print("Imagem do personagem não encontrada!")
22 img = None
23 img_rect = pygame.Rect(WIDTH // 2, HEIGHT 50, 50, 50) # fallback no chão
24
25 # Carregar a imagem do personagem alvo (para ser chutado)
26 target_file = "patrick.png"
27 if os.path.exists(target_file):
28 target_img = pygame.image.load(target_file).convert_alpha()
29 target_rect=target_img.get_rect(midbottom=(WIDTH // 2+200, HEIGHT))
30 else:
31 print("Imagem do personagem alvo não encontradal")
32 target_img = None
33 target_rect = pygame.Rect(WIDTH // 2 + 200, HEIGHT 50, 50, 50)
34
35 # Carregar a imagem de fundo
36 background_file = "background.png"
37 if os.path.exists(background_file):
38 background_orig = pygame.image.load(background_file).convert()
39 background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
48 else:
background_orig = None 41
42 background = None
43 print("Imagem de fundo não encontrada!")
44
45# Variável de posição do Fundo
46 background_x = 0
47
48# Velocidade e fisica
49 SPEED = 3
58 JUMP STRENGTH = 18
51 GRAVITY = 0.3
52 JUMPING = False
53 VELOCITY_Y = 0
54
55 # Variáveis para o alvo chutado
56 target_velocity_x = 0
57 target_velocity_y = 0
58 target jumping = False
59 target_gravity GRAVITY
68
61# Controle redimensionamento
62 last_width, last_height = WIDTH, HEIGHT
63
64 # Função para pular do jogador
65 def jump():
66 global VELOCITY_Y, JUMPING
67 if not JUMPING:
68 VELOCITY Y-JUMP STRENGTH
69 JUMPING = True
70
71# Atualiza o pulo do jogador
72 def update_jump():
73 global VELOCITY_Y, JUMPING, img_rect, GRAVITY
74 if JUMPING:
75 VELOCITY_Y += GRAVITY
76 img_rect.y += VELOCITY_Y
77
78 if img_rect.bottom >= HEIGHT:
img_rect.bottom = HEIGHT
79 JUMPING = False
88 VELOCITY_Y = 0
81
82 # Atualiza o pulo queda do alvo chutado
83 def update_target_physics():
  84
global target_velocity_x, target_velocity_y, target_jumping, target_rect, target_gravity
85
if target_jumping:
86
target_velocity_y += target_gravity
88
87
target_rect.x += target_velocity_x
89
target_rect.y += target_velocity_y
90
if target_rect.bottom >= HEIGHT:
91
92
target_rect.bottom = HEIGHT
93
94
target jumping = False
95
target_velocity_x = 0
96
target_velocity_y = 0
97
else:
target_velocity_x *= 0.95
98
99# Função para "chutar" o alvo
108 def kick():
global target_velocity_x, target_velocity_y, target jumping, target_rect, img_rect
181
102
103
dist_x = target_rect.centerx img_rect.centerx
184
dist_y=target_rect.centery img_rect.centery
185
distancia = (dist_x **2 + dist_y **2) **0.5
109
106
167
if distancia < 150:
188
target_velocity_x 20 if dist x > 0 else -20
118
target_velocity_y = -20
111
target_jumping = True
112# Loop principal do jogo
113 running = True
114 while running:
115
for event in pygame.event.get():
116
if event.type pygame. QUIT:
117
running False
118
119 # Detectar redimensionamento
120
121
current_width, current_height = screen.get_size()
122
if current_width != last_width or current_height = last_height:
123
WIDTH, HEIGHT = current_width, current_height
124
#manter jogadores e alvo no chão
125
img_rect.midbottom (WIDTH // 2, HEIGHT)
126
target_rect.bottom HEIGHT
127
128
if background_orig:
129
background pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
130
last_width, last_height current_width, current_height
131
132
keys pygame.key.get_pressed()
133
134
# Movimento do fundo
135
if keys [pygame.K_RIGHT]:
136
137
background_x -- SPEED
target_rect.x= SPEED # alvo se move junto com o fundo
138
if keys [pygame.K_LEFT]:
139
background_x += SPEED
140
target_rect.x += SPEED # alvo se move junto com o fundo
141
#Pulo e chute
142
if keys [pygame.K_SPACE]:
143
jump()
144
if keys [pygame.K_f]:
145
kick()
146
147
#Atualizar física
148
update_jump()
249
update_target_physics()
150
151
152
# Desenhar fundo com rolagem infinita
153
154
if background:
155
screen.blit(background, (background_x, 0))
156
#Reset do loop
screen.blit(background, (background_x + background.get_width(), 0))
157
if background_x <= background.get_width():
158
background_x = 0
159
169
If background_x >= background.get_width():
161
background_x = 0
else:
162
screen.Fill(BG_COLOR)
163
Desenhar jogador (fixo no centro) -
165
164
if img:
166
screen.blit(img, img_rect.topleft)
167
else:
168
169
pygame.draw.rect(screen, (255, 0, 0), img_rect)
170
# Desenhar alvo
171
if target_img:
172
screen.blit(target_img, target_rect.topleft)
173
else:
pygame.draw.rect(screen, (8, 255, 0), target_rect)
175
174
176
177
pygame.display.flip()
pygame.quit()
