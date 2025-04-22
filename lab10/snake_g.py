
import pygame
import random
import sys
import time
import psycopg2

# Подключение к базе данных
def connect_db():
    return psycopg2.connect(
        host="localhost",
        dbname="snake_bd",
        user="postgres",
        password="5432" 
    )

def get_user_id(username):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if user:
                return user[0]
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                new_id = cur.fetchone()[0]
                conn.commit()
                return new_id

def load_progress(user_id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT score, level
                FROM snake_scores
                WHERE users_id = %s
                ORDER BY saved_at DESC
                LIMIT 1
            """, (user_id,))
            row = cur.fetchone()
            return row if row else (0, 0)

def save_progress(user_id, score, level):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO snake_scores (users_id, score, level)
                VALUES (%s, %s, %s)
            """, (user_id, score, level))
            conn.commit()
    print(f"Progress saved: users_id={user_id}, score={score}, level={level}")

USERNAME = input("Enter your username: ")
USER_ID = get_user_id(USERNAME)
score, level = load_progress(USER_ID)

print(f"Welcome, {USERNAME}! Level: {level}, Score: {score}")

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 25
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MINT = (204, 255, 229)
RED = (200, 0, 0)
BROWN = (102, 51, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 64)
ORANGE = (204, 85, 0)
GREEN = (0, 100, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

def get_level(score):
    if score < 5:
        return 0
    elif score < 10:
        return 1
    else:
        return 2

def get_speed(level):
    return [8, 12, 15][level]

def get_walls_for_level(level):
    walls = set()
    for x in range(GRID_WIDTH):
        walls.add((x, 0))
        walls.add((x, GRID_HEIGHT - 1))
    for y in range(GRID_HEIGHT):
        walls.add((0, y))
        walls.add((GRID_WIDTH - 1, y))
    if level >= 1:
        for i in range(5, 15):
            walls.add((i, i))
    if level >= 2:
        for i in range(10, 20):
            walls.add((i, GRID_HEIGHT - i))
    return walls

snake = [(5, 5)]
direction = (1, 0)
game_over = False
food = (0, 0)
food_timer = time.time()
FOOD_LIFETIME = 5
food_value = 1

def spawn_food():
    global food, food_value, food_timer
    while True:
        candidate = (
            random.randint(1, GRID_WIDTH - 2),
            random.randint(1, GRID_HEIGHT - 2)
        )
        if candidate not in walls and candidate not in snake:
            food = candidate
            break
    food_value = random.choice([1, 2, 3])
    food_timer = time.time()

level = get_level(score)
speed = get_speed(level)
walls = get_walls_for_level(level)
spawn_food()

def draw_all():
    win.fill(MINT)
    for wx, wy in walls:
        pygame.draw.rect(win, BROWN, (wx*CELL_SIZE, wy*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(win, ORANGE, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    txt = font.render(str(food_value), True, BLACK)
    win.blit(txt, (food[0]*CELL_SIZE + 5, food[1]*CELL_SIZE))
    for sx, sy in snake:
        pygame.draw.rect(win, GREEN, (sx*CELL_SIZE, sy*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    s1 = font.render(f"User: {USERNAME}", True, BLACK)
    s2 = font.render(f"Score: {score}", True, BLACK)
    s3 = font.render(f"Level: {level}", True, BLACK)
    win.blit(s1, (10, 10))
    win.blit(s2, (10, 40))
    win.blit(s3, (10, 70))
    pygame.display.update()

def update_snake():
    global game_over, score, level, speed, walls
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    if new_head in snake or new_head in walls or not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
        game_over = True
        return
    snake.insert(0, new_head)
    if new_head == food:
        score += food_value
        spawn_food()
        new_level = get_level(score)
        if new_level != level:
            level = new_level
            speed = get_speed(level)
            walls = get_walls_for_level(level)
    else:
        snake.pop()
    if time.time() - food_timer > FOOD_LIFETIME:
        spawn_food()

def pause_game():
    save_progress(USER_ID, score, level)
    paused_text = font.render("Paused: Press C to continue, Q to quit", True,BLUE )
    paused = True
    while paused:
        win.fill(BLACK)
        win.blit(paused_text, (WIDTH//2 - paused_text.get_width()//2, HEIGHT//2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    save_progress(USER_ID, score, level)
                    pygame.quit()
                    sys.exit()

while True:
    clock.tick(speed)
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key == pygame.K_p:
                    pause_game()
        update_snake()
        draw_all()
    else:
        win.fill(BLACK)
        go_text = font.render("Game Over! Press R to Restart", True, RED)
        sc_text = font.render(f"Overall score: {score}", True, WHITE)
        win.blit(go_text, (WIDTH//2 - go_text.get_width()//2, HEIGHT//2 - 30))
        win.blit(sc_text, (WIDTH//2 - sc_text.get_width()//2, HEIGHT//2 + 10))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    snake = [(5,5)]
                    direction = (1,0)
                    score, level = 0, 0
                    speed = get_speed(level)
                    walls = get_walls_for_level(level)
                    spawn_food()
                    game_over = False
