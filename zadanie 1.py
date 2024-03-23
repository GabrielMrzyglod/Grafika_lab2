import pygame
import math

# Inicjalizacja modułu pygame
pygame.init()

# Ustawienia okna
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Przekształcenie wielokąta")

# Kolory
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Funkcja rysująca dziewięciokąt w środku ekranu
def draw_nonagon():
    center = (window_width // 2, window_height // 2)
    radius = 150
    num_sides = 9
    angle_increment = (2 * math.pi) / num_sides

    points = []
    for i in range(num_sides):
        x = center[0] + int(radius * math.cos(i * angle_increment))
        y = center[1] + int(radius * math.sin(i * angle_increment))
        points.append((x, y))

    return points

# Funkcja przekształcająca wielokąt w zależności od wybranej opcji
def transform_nonagon(points, option):
    if option == 2:
        # Obrót o 45 stopni
        points = rotate_polygon(points, 45)
    elif option == 3:
        # Obrót o 180 stopni
        points = rotate_polygon(points, 180)
    elif option == 4:
        # Pochylenie w lewo
        points = skew_polygon(points, 1.5)
    elif option == 5:
        # Przy górnej krawędzi
        points = align_top(points)
    elif option == 6:
        # Pochylenie w lewo i obrót o 180 stopni
        points = skew_polygon(points, 1.5)
        points = rotate_polygon(points, 225)
    elif option == 7:
        # Obrót o 180 stopni i odbicie lustrzane
        points = rotate_polygon(points, 180)
        points = mirror_polygon(points, "vertical")
    elif option == 8:
        # Obrót o 45 stopni i przy dolnej krawędzi
        points = rotate_polygon(points, 45)
        points = align_bottom(points)
    elif option == 9:
        # Obrót o 180 stopni, pochylenie w lewo i przy prawej krawędzi
        points = rotate_polygon(points, 180)
        points = skew_polygon(points, 1.5)
        points = align_right(points)

    return points

# Funkcja obracająca wielokąt
def rotate_polygon(points, angle):
    center = (window_width // 2, window_height // 2)
    angle_radians = math.radians(angle)
    rotated_points = []
    for point in points:
        x = center[0] + math.cos(angle_radians) * (point[0] - center[0]) - math.sin(angle_radians) * (point[1] - center[1])
        y = center[1] + math.sin(angle_radians) * (point[0] - center[0]) + math.cos(angle_radians) * (point[1] - center[1])
        rotated_points.append((x, y))
    return rotated_points

# Funkcja pochylająca wielokąt
def skew_polygon(points, factor):
    center = (window_width // 2, window_height // 2)
    skewed_points = []
    for point in points:
        x = point[0] + factor * (point[1] - center[1])
        y = point[1]
        skewed_points.append((x, y))
    return skewed_points

# Funkcja odbijająca wielokąt
def mirror_polygon(points, axis):
    if axis == "vertical":
        center_x = sum(point[0] for point in points) / len(points)
        mirrored_points = [(2 * center_x - point[0], point[1]) for point in points]
    elif axis == "horizontal":
        center_y = sum(point[1] for point in points) / len(points)
        mirrored_points = [(point[0], 2 * center_y - point[1]) for point in points]
    return mirrored_points

# Funkcja przesuwająca wielokąt do górnej krawędzi
def align_top(points):
    min_y = min(point[1] for point in points)
    shifted_points = [(point[0], point[1] - min_y) for point in points]
    return shifted_points

# Funkcja przesuwająca wielokąt do dolnej krawędzi
def align_bottom(points):
    max_y = max(point[1] for point in points)
    shifted_points = [(point[0], point[1] - max_y + window_height) for point in points]
    return shifted_points

# Funkcja przesuwająca wielokąt do prawej krawędzi
def align_right(points):
    max_x = max(point[0] for point in points)
    shifted_points = [(point[0] - max_x + window_width, point[1]) for point in points]
    return shifted_points

# Główna pętla programu
running = True
option = 1
points = draw_nonagon()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                option = 1
            elif event.key == pygame.K_2:
                option = 2
            elif event.key == pygame.K_3:
                option = 3
            elif event.key == pygame.K_4:
                option = 4
            elif event.key == pygame.K_5:
                option = 5
            elif event.key == pygame.K_6:
                option = 6
            elif event.key == pygame.K_7:
                option = 7
            elif event.key == pygame.K_8:
                option = 8
            elif event.key == pygame.K_9:
                option = 9

    window.fill(YELLOW)
    transformed_points = transform_nonagon(points, option)
    pygame.draw.polygon(window, BLACK, transformed_points)
    pygame.display.update()

# Zakończenie działania programu
pygame.quit()
