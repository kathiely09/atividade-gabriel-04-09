
1 import pygame
2 import os
3
4 # Inicializando o Pygame
5 pygame.init()
6
7# Definindo o tamanho da janela padrão
8 WIDTH, HEIGHT 720, 420
9 screen pygame.display.set_mode((WIDTH, HEIGHT), pygame. RESIZABLE) # Janela redimensionável
10 pygame.display.set_caption("Mover Imagem com Setas")
11
12 # Definindo a cor de fundo (usada se não houver imagem de fundo)
13 BG COLOR (193, 0, 40) # cor de fundo (um tom escuro)
14
15 # Carregar a imagem do personagem principal (jogador)
16 image_file = "player.png"
17 if os.path.exists(image_file):
18 img pygame.image.load(image_file).convert_alpha()
19 img_rect img.get_rect(midbottom=(WIDTH // 2, HEIGHT)) # inicia no chão
20 else:
21 print("Imagem do personagem não encontrada!")
22 img = None
23 img_rect pygame. Rect(WIDTH // 2, HEIGHT 50, 50, 50) # fallback no chão
24
25 # Carregar a imagem do personagem alvo (para ser chutado)
26 target file = "patrick.png"
27 if os.path.exists(target_file):
28 target_img = pygame.image.load(target_file).convert_alpha()
29 target_rect=target_img.get_rect(midbottom=(WIDTH // 2+200, HEIGHT)) # também no chão
30 else:
31 print("Imagem do personagem alvo não encontrada!")
32 target_img = None
33 target_rect = pygame.Rect(WIDTH I / 2 + 200 HEIGHT 50, 50, 50) #fallback no chão
34
35 # Carregar a imagem de fundo
36 background_file = "background.png"
37 if os.path.exists(background_file):
38 background_orig = pygame.image.load(background_file).convert()
39 background pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
40 else:
background_orig = None 41
42 background None
43 print("Imagem de fundo não encontrada!")
44
45 # Velocidade de movimento do jogador
46 SPEED = 3
47 JUMP STRENGTH = 18
48 GRAVITY = 0.3
49 JUMPING = False
50 VELOCITY Y = 0
51
52 # Variáveis para o alvo chutado
53 target_velocity_x = 0
54 target_velocity_y = 0
55 target jumping False
56 target_gravity= GRAVITY
57
58 # Controle redimensionamento
59 last_width, last_height = WIDTH, HEIGHT
60
61 # Limitar movimento para não sair da tela
62 def limit_movement(rect):
63 if rect.left < 0:
64 rect.left = 0
65 if rect.right > WIDTH:
66
rect.right = WIDTH
67 if rect.top < 0:
68 rect.top = 0
69 if rect.bottom > HEIGHT:
70 rect.bottom = HEIGHT
71
72 # Função para pular do jogador
73 def jump():
global VELOCITY_Y, JUMPING 74
75 if not JUMPING:
76 VELOCITY_Y = -JUMP STRENGTH
77 JUMPING = True
78
79 # Atualiza o pulo do jogador
80 def update_jump():
81 global VELOCITY_Y, JUMPING, img_rect, GRAVITY
82 if JUMPING:
83
VELOCITY_Y += GRAVITY
84
img_rect.y += VELOCITY_Y
85
if img_rect.bottom >= HEIGHT:
86
img_rect.bottom = HEIGHT
87
JUMPING False
88
VELOCITY_Y = 0
89
90 # Atualiza o pulo queda do alvo chutado
91 def update_target_physics():
global target_velocity_x, target_velocity_y, target_jumping, target_rect, target_gravity
93
if target jumping:
94
target_velocity_y += target_gravity
95
target_rect.x += target_velocity_x
96
target_rect.y += target_velocity_y
92
97
98
if target_rect.bottom >= HEIGHT:
99
100
target_rect.bottom = HEIGHT
101
target jumping = False
102
target_velocity_x = 0
1.03
184
target_velocity_y = 0
else:
185
target_velocity_x *= 0.95
186
107 # Função para "chutar" o alvo
108 def kick():
109 global target_velocity_x, target_velocity_y, target_jumping, target_rect, img_rect
110
111 dist_x target_rect.centerx img_rect.centerx
112 dist_y = target_rect.centery img_rect.centery
113 distancia = (dist_x** 2+ dist_y ** 2) ** 0.5
114
115 if distancia < 150:
116
117
target_velocity_x x = 2theta if dist_x > 0 else -20
118
target_velocity_y l = - 2theta
119
target_jumping = True
120 # Loop principal do jogo
121 running = True
122 while running:
123 for event in pygame.event.get():
124
if event.type == pygame.QUIT:
125
running = False
126
127
#Detectar redimensionamento
128
129
current_width, current_height = screen.get_size()
if current_width != last_width or current_height != last_height:
130
WIDTH, HEIGHT = current_width, current_height
131
132
#manter personagens no chão
133
img_rect.bottom = HEIGHT
134
target_rect.bottom = HEIGHT
135
136
if background_orig:
137
background pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
138
last_width, last_height = current_width, current_height
139
140
#Teclas pressionadas
141
keys = pygame.key.get_pressed()
142
143
if keys [pygame.K_LEFT]:
144
img_rect.x -= SPEED
145
if keys [pygame.K_RIGHT]:
146
img_rect.x += SPEED
147
if keys [pygame.K_UP]:
148
img_rect.y = SPEED
149
if keys [pygame.K_DOWN]:
150
img_rect.y += SPEED
151
152
if keys [pygame.K_SPACE]:
153
jump()
154
if keys [pygame.K_f]:
155
kick()
156
limit_movement(img_rect)
157
limit_movement(target_rect)
159
158
update_jump()
161
160
update_target_physics()
162
if background:
163
screen.blit(background, (0, 0))
165
164
else:
166
167
screen.fill(BG_COLOR)
168
if img:
169
screen.blit(img, img_rect.topleft)
-
170
else:
171
pygame.draw.rect(screen, (255, 0, 0), img_rect)
172
173
if target_img:
174
175
screen.blit(target_img, target_rect.topleft)
else:
176
pygame.draw.rect(screen, (8, 255, 0), target_rect)
177
178
pygame.display.flip()
179
180 pygame.quit()
181
