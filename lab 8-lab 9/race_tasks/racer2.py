import pygame
import random
import sys

pygame.init()

# Set up display dimensions and create the window
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race Game")
clock = pygame.time.Clock()

# Load and scale the background image
background = pygame.image.load("pp2_labs/lab 8/race_tasks/street.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load and scale the player image 
player_img = pygame.image.load("pp2_labs/lab 8/race_tasks/Player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (70, 80))

# Load and scale the coin image
coin_img = pygame.image.load("pp2_labs/lab 8/race_tasks/coin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (45, 45))

# Load and scale the enemy image 
enemy_img = pygame.image.load("pp2_labs/lab 8/race_tasks/Enemy_Green.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (70, 100))


# Load background music and game over sound using the same file.
# (In a full project you might use different files, but here we use the one provided.)
music_file = "pp2_labs/lab 8/race_tasks/game-music-teste-204327.mp3"
pygame.mixer.music.load(music_file)  # Background music
crash_sound = pygame.mixer.Sound("pp2_labs/lab 8/race_tasks/crash.wav")

# Start playing the background music on loop (-1 means loop indefinitely)
pygame.mixer.music.play(-1)

# --------------------------
# Set up game objects
# --------------------------

# Set up the player rectangle and position it near the bottom center of the screen
player_rect = player_img.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - 100)

# Lists to store coin and enemy rectangles
coins = []
enemies = []

# Set up timer events for spawning coins and enemies
COIN_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_SPAWN, 1000)  # Spawn a coin every 1 second

ENEMY_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(ENEMY_SPAWN, 3000)  # Spawn an enemy every 3 seconds

# Initialize the score and set up a font for displaying text
score = 0
font = pygame.font.Font(None, 36) 
# --------------------------
# Main game loop
running = True
while running:
    # Process events (keyboard, timers, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Timer event: spawn a new coin at a random horizontal position at the top
        if event.type == COIN_SPAWN:
            x = random.randint(0, WIDTH - coin_img.get_width())
            coin_rect = coin_img.get_rect(topleft=(x, 0))
            coins.append(coin_rect)

        # Timer event: spawn a new enemy at a random horizontal position at the top
        if event.type == ENEMY_SPAWN:
            x = random.randint(0, WIDTH - enemy_img.get_width())
            enemy_rect = enemy_img.get_rect(topleft=(x, 0))
            enemies.append(enemy_rect)

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5  # Move player left
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5  # Move player right

    # Keep the player within screen boundaries
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WIDTH:
        player_rect.right = WIDTH

    # --------------------------
    # Update coin and enemy positions
    # --------------------------
    # Move coins down the screen (simulate falling coins)
    for coin in coins:
        coin.y += 3  # Adjust speed as desired

    # Remove coins that have fallen off the bottom of the screen
    coins = [coin for coin in coins if coin.top < HEIGHT]

    # Move enemies down the screen
    for enemy in enemies:
        enemy.y += 4  # Enemies can move a bit faster

    # Remove enemies that have fallen off the bottom of the screen
    enemies = [enemy for enemy in enemies if enemy.top < HEIGHT]

    # --------------------------
    # Check for collisions
    # Collision with coins: collect coin and increase score
    for coin in coins[:]:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            score += 1

    # Collision with enemies: immediate game over if player hits an enemy
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            crash_sound.play()
            running = False

    # Optionally, you can also set a win condition (e.g., score reaches 10)
    if score >= 150:
        running = False

    screen.blit(background, (0, 0))
    # Draw the player sprite
    screen.blit(player_img, player_rect)

    # Draw each coin
    for coin in coins:
        screen.blit(coin_img, coin)

    # Draw each enemy
    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    # Render and display the score text in the top right corner
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    text_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(score_text, text_rect)

    # Update the display and maintain a frame rate of 60 FPS
    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()

#display "Game Over!" message
screen.fill((0, 0, 0))
game_over_text = font.render("Game Over!", True, (255, 0, 0))
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

# Wait a short time before closing the game so the player can see the message
pygame.time.wait(2000)

pygame.quit()
sys.exit()
