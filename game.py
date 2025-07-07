import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
TILE_SIZE = WIDTH // COLS
FPS = 60
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 165, 0), (255, 105, 180)]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy Crush Mini")
clock = pygame.time.Clock()

board = [[random.randint(0, len(COLORS) - 1) for _ in range(COLS)] for _ in range(ROWS)]


def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, COLORS[board[row][col]],
                             (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, (0, 0, 0),
                             (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)


def swap_tiles(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]


def check_matches():
    matched = []
   
    for row in range(ROWS):
        for col in range(COLS - 2):
            if board[row][col] == board[row][col + 1] == board[row][col + 2]:
                matched.extend([(row, col), (row, col + 1), (row, col + 2)])

    for col in range(COLS):
        for row in range(ROWS - 2):
            if board[row][col] == board[row + 1][col] == board[row + 2][col]:
                matched.extend([(row, col), (row + 1, col), (row + 2, col)])

    return list(set(matched))


def remove_matches(matches):
    for r, c in matches:
        board[r][c] = -1

    for c in range(COLS):
        col_values = [board[r][c] for r in range(ROWS) if board[r][c] != -1]
        col_values = [-1] * (ROWS - len(col_values)) + col_values
        for r in range(ROWS):
            board[r][c] = col_values[r]

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == -1:
                board[r][c] = random.randint(0, len(COLORS) - 1)


selected = None

running = True
while running:
    clock.tick(FPS)
    screen.fill((255, 255, 255))

    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // TILE_SIZE, x // TILE_SIZE
            if selected:
                r0, c0 = selected
                if abs(r0 - row) + abs(c0 - col) == 1:
                    swap_tiles((r0, c0), (row, col))
                    matches = check_matches()
                    if matches:
                        remove_matches(matches)
                    else:
                        swap_tiles((r0, c0), (row, col))  # swap back if no match
                    selected = None
                else:
                    selected = (row, col)
            else:
                selected = (row, col)

    pygame.display.flip()

pygame.quit()
sys.exit()
