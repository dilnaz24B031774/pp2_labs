import pygame
import random
import time

pygame.init()

screen_width = 600
screen_height = 400
snake_size = 10
food_size = 10
initial_speed = 10

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 150, 0)
red = (255, 0, 0)

font_style = pygame.font.SysFont(None, 30)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

def display_text(text, x, y, color=white, center=False):
    value = font_style.render(text, True, color)
    if center:
        text_rect = value.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(value, text_rect.topleft)
    else:
        screen.blit(value, [x, y])

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_size, snake_size])

def generate_food(snake_list):
    while True:
        food_x = random.randrange(0, screen_width - food_size, 10)
        food_y = random.randrange(0, screen_height - food_size, 10)
        if (food_x, food_y) not in snake_list:
            return food_x, food_y

def game_loop():
    x, y = screen_width // 2, screen_height // 2
    dx, dy = 0, 0
    snake_list = []
    snake_length = 1
    food_x, food_y = generate_food(snake_list)
    score = 0
    level = 1
    speed = initial_speed
    game_running = True

    while game_running:
        screen.fill(black)
        display_text(f"Score: {score}", 10, 10)
        display_text(f"Level: {level}", 10, 30)
        pygame.draw.rect(screen, red, [food_x, food_y, food_size, food_size])
        draw_snake(snake_list)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -snake_size, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = snake_size, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -snake_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, snake_size
        
        x += dx
        y += dy
        if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
            game_running = False
            break
        
        snake_list.append((x, y))
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        if (x, y) in snake_list[:-1]:
            game_running = False
            break
        
        if x == food_x and y == food_y:
            food_x, food_y = generate_food(snake_list)
            snake_length += 1
            score += 1
            if score % 5 == 0:
                level += 1
                speed += 2
        
        clock.tick(speed)
    
    screen.fill(black)
    display_text("Game Over", screen_width // 2, screen_height // 2, red, center=True)
    pygame.display.update()
    time.sleep(2)
    game_loop()

game_loop()