import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prostokąt i trójkąt")

# Kolory
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Rysowanie prostokąta
rect_width = 150  # Zwiększamy szerokość prostokąta
rect_height = 200
rectangle = pygame.Surface((rect_width, rect_height))
rectangle.fill(GREEN)
rect_pos = (WIDTH // 2 - rect_width // 2, HEIGHT // 2 - rect_height // 2)
screen.blit(rectangle, rect_pos)

# Rysowanie trójkąta
triangle_height = 100
triangle_points = [(rect_pos[0], rect_pos[1] + rect_height),
                   (rect_pos[0] + rect_width, rect_pos[1] + rect_height),
                   (rect_pos[0] + rect_width // 2, rect_pos[1] + rect_height - triangle_height)]
pygame.draw.polygon(screen, WHITE, triangle_points)

# Odświeżenie ekranu
pygame.display.flip()

# Pętla główna gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
