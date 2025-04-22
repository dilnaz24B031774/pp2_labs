import pygame
import random
import sys
pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race Game")
clock = pygame.time.Clock()

#фоновая изобрежения
background = pygame.image.load("pp2_labs/lab 8-lab 9/race_tasks/street.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Загрузка и масштабирование изображения игрока 
player_img = pygame.image.load("pp2_labs/lab 8-lab 9/race_tasks/Player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (70, 80))

# Загрузка и масштабирование изображения монеты
coin_img = pygame.image.load("pp2_labs/lab 8-lab 9/race_tasks/coin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (45, 45))

# Загрузка и масштабирование изображения врага 
enemy_img = pygame.image.load("pp2_labs/lab 8-lab 9/race_tasks/Enemy_Green.png").convert_alpha() 
enemy_img = pygame.transform.scale(enemy_img, (70, 100))

# Загрузить фоновую музыку
music_file = "pp2_labs/lab 8-lab 9/race_tasks/game-music-teste-204327.mp3"
pygame.mixer.music.load(music_file)  # Background music
crash_sound = pygame.mixer.Sound("pp2_labs/lab 8-lab 9/race_tasks/crash.wav")

# Начинать проигрывать фоновую музыку по циклу (-1 означает бесконечный цикл)
pygame.mixer.music.play(-1)

player_rect = player_img.get_rect() #создаёт hitbox игрока.
player_rect.center = (WIDTH // 2, HEIGHT - 100) # ставит машину в центр внизу экрана.

# Создание массивов для хранения монет и врагов
coins = []
enemies = []

# Установите таймер событий  для появления монет и врагов
COIN_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_SPAWN, 1000)   # Монета каждые 1000 мс (1 сек)

ENEMY_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(ENEMY_SPAWN, 3000)  # Враг каждые 3 сек

score = 0
font = pygame.font.Font(None, 36) 

# Main game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Монетка появится случайно по горизонтали в пределах ширины окна.
        if event.type == COIN_SPAWN:
            x = random.randint(0, WIDTH - coin_img.get_width()) # чтобы монетка не вышла за правый край экрана.
            coin_rect = coin_img.get_rect(topleft=(x, 0))#устанавливает, что монетка появится в точке (x, 0)
            coins.append(coin_rect) #Добавляем монетку в список coins

    
        if event.type == ENEMY_SPAWN:
            x = random.randint(0, WIDTH - enemy_img.get_width())
            enemy_rect = enemy_img.get_rect(topleft=(x, 0))
            enemies.append(enemy_rect)

    #управлять действями игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5  # Move player left
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5  # Move player right

   # Удерживать игрока в границах экрана
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WIDTH:
        player_rect.right = WIDTH

    # Обновление положения монет и врагов
    for coin in coins:
        coin.y += 3  # Регулировка скорости по желанию

    # Удалять монеты, которые упали в нижнюю часть экрана.
    coins = [coin for coin in coins if coin.top < HEIGHT]

    # Переместить врагов вниз по экрану
    for enemy in enemies:
        enemy.y += 4  # Враг может двигаться немного быстрее

    # Remove enemies that have fallen off the bottom of the screen
    enemies = [enemy for enemy in enemies if enemy.top < HEIGHT]

    #Проверяет, не столкнулся ли игрок с монетами, удаляет монету и увеличивает счет.
    for coin in coins[:]:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            score += 1

    #завершение игры при попадании игрока во врага
    for enemy in enemies:
        if player_rect.colliderect(enemy): #контроль столкновение
            crash_sound.play()
            running = False

    if score >= 150:
        running = False

    screen.blit(background, (0, 0))
    # Draw the player sprite
    screen.blit(player_img, player_rect)

  # Нарисовать каждую монету
    for coin in coins:
        screen.blit(coin_img, coin)

    # Draw each enemy
    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    # отображение текста score в правом верхнем углу
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    text_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(score_text, text_rect)

    # Обновление дисплея и поддержание частоты кадров  FPS
    pygame.display.flip()
    clock.tick(60)
pygame.mixer.music.stop()

#display "Game Over!"
screen.fill((0, 0, 0))
game_over_text = font.render("Game Over!", True, (255, 0, 0))
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

pygame.time.wait(2000) # Подождать некоторое время, прежде чем закрыть игру 
pygame.quit()
sys.exit()
