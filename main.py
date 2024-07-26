import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Iván contra los Zombies')
clock = pygame.time.Clock()

# Cargar imágenes
ivan = pygame.image.load('assets/ivan.png')
zombie = pygame.image.load('assets/zombie.png')
background = pygame.image.load('assets/background.png')

# Posiciones iniciales
ivan_rect = ivan.get_rect(topleft=(50, 400))
zombie_rect = zombie.get_rect(topleft=(700, 400))

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render('Presiona Enter para Jugar', True, (255, 255, 255))
        screen.blit(text, (100, 250))
        pygame.display.flip()

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ivan_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            ivan_rect.x += 5
        if keys[pygame.K_SPACE]:
            ivan_rect.y -= 10
        else:
            ivan_rect.y += 5

        screen.blit(background, (0, 0))
        screen.blit(ivan, ivan_rect)
        screen.blit(zombie, zombie_rect)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main_menu()
