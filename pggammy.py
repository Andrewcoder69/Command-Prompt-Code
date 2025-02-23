import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Complex Game Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_size = 50
player_color = (0, 128, 255)
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_color = (255, 0, 0)
enemy_pos = [100, 100]
enemy_speed = 3

# Update the game loop to include enemy movement
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Enemy movement (simple AI)
    if enemy_pos[0] < player_pos[0]:
        enemy_pos[0] += enemy_speed
    elif enemy_pos[0] > player_pos[0]:
        enemy_pos[0] -= enemy_speed
    if enemy_pos[1] < player_pos[1]:
        enemy_pos[1] += enemy_speed
    elif enemy_pos[1] > player_pos[1]:
        enemy_pos[1] -= enemy_speed

    # Screen update
    screen.fill(BLACK)
    pygame.draw.rect(screen, player_color, (*player_pos, player_size, player_size))
    pygame.draw.rect(screen, enemy_color, (*enemy_pos, enemy_size, enemy_size))
    pygame.display.flip()

    # Frame rate
    clock.tick(30)
    
# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Screen update
    screen.fill(BLACK)
    pygame.draw.rect(screen, player_color, (*player_pos, player_size, player_size))
    pygame.display.flip()

    # Frame rate
    clock.tick(30)

pygame.quit()
