import pygame
import random


def in_bounds(x: int, y: int, width: int, height: int):
    if x >= width or x < 0:
        return False
    if y >= height or y < 0:
        return False
    return True


def check_neighbors(x: int, y: int, frame: list[list[bool]], grid: list[list[bool]]):
    count: int = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if in_bounds(x + j, y + i, len(grid[0]), len(grid)):
                if i != 0 or j != 0:
                    if frame[y + i][x + j]:
                        count += 1
    if frame[y][x]:
        if count < 2 or count > 3:
            grid[y][x] = False
    else:
        if count == 3:
            grid[y][x] = True


def update(grid: list[list[bool]]):
    frame = grid.copy()
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            check_neighbors(j, i, frame, grid)
        print()


def main():

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    running = True
    n = 10
    width = int(16 * n)
    height = int(9 * n)
    cell_width = 1920 // width
    cell_height = 1080 // height

    grid: list[list[bool]] = []
    for i in range(height):
        grid.append([])
        for _ in range(width):
            r = random.randint(1, 20)
            if r == 1:
                grid[i].append(True)
            else:
                grid[i].append(False)

    while running:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if keys[pygame.K_LCTRL]:
                running = False

        screen.fill((0, 0, 0))

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen,
                        (0, 255, 255),
                        (j * cell_width, i * cell_height, cell_width, cell_height),
                    )

        pygame.display.flip()

        update(grid)

    pygame.quit()


main()
