import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock() 
FPS = 50 #ограничение обновления экрана до 50 кадров в секунду.

background = pygame.transform.scale(pygame.image.load('pp2_labs/lab 7/clock_tasks/clock.png'), (600, 600))
minute_hand = pygame.transform.scale(pygame.image.load('pp2_labs/lab 7/clock_tasks/minute_hand.png'), (800, 700))
second_hand = pygame.transform.scale(pygame.image.load('pp2_labs/lab 7/clock_tasks/second_hand.png'), (40, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    t = datetime.datetime.now()
    angles = [-t.second * 6 - 6, -t.minute * 7 - 11]

    hands = [pygame.transform.rotate(second_hand, angles[0]), pygame.transform.rotate(minute_hand, angles[1])]
    #angles[0] повернутая секундная стрелка,angles[1]-повернутая минутная стрелка.
    screen.fill((255, 255, 255))
    screen.blit(background, (100, 100)) # циферблата.

    #Отрисовка стрелок
    for i, hand in enumerate(hands):
        screen.blit(hand, (399 - hand.get_width() // 2, 400 - hand.get_height() // 2)) #центр вращения стрелок
    #pygame.draw.circle(screen, (0, 0, 0), (400, 400), 22)
    
    pygame.display.flip()
    clock.tick(FPS)






