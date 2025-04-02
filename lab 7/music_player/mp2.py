import pygame
import os

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music Player")

music_directory = "pp2_labs/lab 7/music_player/musics"
os.chdir(music_directory)

music_files = [file for file in os.listdir() if file.endswith(".mp3")]
current_track = 0 # индекс текущего трека (начинается с первого в списке)
paused = False 
pygame.mixer.music.load(music_files[current_track])
#Установка шрифта
font = pygame.font.Font(None, 24)
icon = pygame.image.load("../icon.jpg")
ikaif = pygame.transform.scale(icon, (200, 200))

running = True
while running:
    screen.fill((255, 228, 225))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                pygame.mixer.music.pause() if paused else pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
    
    screen.blit(font.render("Space: Play/Pause / <- Prev | -> Next", True, (0, 0, 0)), (10, 10))
    screen.blit(ikaif, (150, 100))
    pygame.display.flip()

pygame.quit()
