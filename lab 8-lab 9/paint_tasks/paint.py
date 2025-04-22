import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 24)
toolbar_height = 60 #высота панели инструментов.
screen = pygame.display.set_mode((WIDTH, HEIGHT + toolbar_height)) #основное окно приложения (высота увеличена на панель).
pygame.display.set_caption("Paint")

#Создание белого поверхности холста (canvas), отдельного от экрана (screen)
screen.fill(WHITE)
canvas = pygame.Surface((WIDTH, HEIGHT)) #отдельный холст, который позже "приклеивается" к экрану, чтобы можно было легко "перерисовывать" без очистки интерфейса.
canvas.fill(WHITE)

tool_icons = {
    "brush": pygame.image.load("pp2_labs/lab 8-lab 9/paint_tasks/icon/paint-brush.png"),
    "clear": pygame.image.load("pp2_labs/lab 8-lab 9/paint_tasks/icon/clear1.png"),
    "eraser": pygame.image.load("pp2_labs/lab 8-lab 9/paint_tasks/icon/eraser1.png"),
}

tool_buttons = {} #пустой словарь для хранения кнопок инструментов.
x_offset = 10 #начальное положение кнопок на панели инструментов
for tool, icon in tool_icons.items():
    tool_buttons[tool] = pygame.Rect(x_offset, HEIGHT + 10, 40, 40)
    x_offset += 50 #каждая кнопка располагается на 50 пикселей правее предыдущей.

clock = pygame.time.Clock()
running = True
drawing = False
moving = False
selected_shape = None
last_pos = None
mode = "pen" #текущий режим (кисть, круг, прямоугольник и т.д.).
color = BLACK
size = 5 #текущий размер кисти.
start_pos = None
shapes = [] #список всех фигур на холсте 

def draw_toolbar(): #Рисует панель инструментов внизу и размещает на ней иконки инструментов.
    pygame.draw.rect(screen, (142, 69, 133), (0, HEIGHT, WIDTH, toolbar_height))
    for tool, rect in tool_buttons.items():
        screen.blit(pygame.transform.scale(tool_icons[tool], (40, 40)), rect.topleft)

def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius, 0 if mode == "circle" else size)
    shapes.append(("circle", color, center, radius))

def draw_rect(surface, color, start, end):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, 0 if mode == "rect" else size)
    shapes.append(("rect", color, rect))


def redraw_canvas(): #Функция для обновления экрана — вызывается каждый кадр.
    screen.blit(canvas, (0, 0))
    draw_toolbar()
    instruction_text = FONT.render("1 - Черный, 2 - Красный, 3 - Зеленый, 4 - Синий | P - Кисть, R - Прямоугольник, C - Круг, E-Ластик", True, (0, 0, 139))
    screen.blit(instruction_text, (10, HEIGHT - 20))

while running:
    redraw_canvas()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] > HEIGHT:
                for tool, rect in tool_buttons.items():
                    if rect.collidepoint(event.pos):
                        if tool == "brush":
                            mode = "pen"
                        elif tool == "clear":
                            canvas.fill(WHITE)
                            shapes.clear()
                        elif tool == "eraser":
                            mode = "eraser"
                        
            else:
                drawing = True
                last_pos = event.pos
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "rect":
                draw_rect(canvas, color, start_pos, event.pos)
            elif mode == "circle":
                radius = int(((event.pos[0] - start_pos[0])**2 + (event.pos[1] - start_pos[1])**2) ** 0.5)
                draw_circle(canvas, color, start_pos, radius)
        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode == "pen":
                pygame.draw.line(canvas, color, last_pos, event.pos, size)
                last_pos = event.pos
            elif drawing and mode == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, event.pos, size)
                last_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = (255, 0, 0)
            elif event.key == pygame.K_3:
                color = (0, 255, 0)
            elif event.key == pygame.K_4:
                color = (0, 0, 255)

    pygame.display.flip()
    clock.tick(60) # ограничение частоты кадров до 60 FPS.
pygame.quit()