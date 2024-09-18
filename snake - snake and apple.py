import random

import pygame

GRID_SIZE = 40
CELL_SIZE = 16
DIRECTIONS: dict[str, tuple[int]] = {
    "w": (0, -1),
    "a": (-1, 0),
    "s": (0, 1),
    "d": (1, 0)
}


def renderAll(window: pygame.Surface, snake, apple: tuple[int]) -> None:
    # Make a new surface and fill it with grey
    gridSurf = pygame.Surface((GRID_SIZE * CELL_SIZE + 1, GRID_SIZE * CELL_SIZE + 1))
    gridSurf.fill('grey')
    # Draw 41 lines both vertically and horizontally to the new surface
    for i in range(41):
        pygame.draw.line(gridSurf, (0, 0, 0), (0, i * CELL_SIZE), (gridSurf.get_width(), i * CELL_SIZE))
        pygame.draw.line(gridSurf, (0, 0, 0), (i * CELL_SIZE, 0), (i * CELL_SIZE, gridSurf.get_height()))

    # Draw the apple
    radius = CELL_SIZE // 2
    pygame.draw.circle(gridSurf, (222, 22, 22), (apple[0] * CELL_SIZE + radius, apple[1] * CELL_SIZE + radius), radius)

    # Draw the snake
    for pos in snake:
        pygame.draw.circle(gridSurf, (22, 22, 222), (pos[0] * CELL_SIZE + radius, pos[1] * CELL_SIZE + radius), radius)
    # Make a tongue for our snake
    end = snake[0][0] * CELL_SIZE + radius + DIRECTIONS[snake[0][2]][0] * radius, snake[0][1] * CELL_SIZE + radius + DIRECTIONS[snake[0][2]][1] * radius
    pygame.draw.line(gridSurf, (222, 22, 22), (snake[0][0] * CELL_SIZE + radius, snake[0][1] * CELL_SIZE + radius), end, 4)

    # Make a border around the grid
    border = pygame.Rect((0, 0), (gridSurf.get_width() + GRID_SIZE, gridSurf.get_height() + GRID_SIZE))

    # Make sure everything is centered based on the original window
    rect = window.get_rect()
    gridRect = gridSurf.get_rect(center=rect.center)
    border.center = rect.center

    # Draw the border and grid onto the window
    pygame.draw.rect(window, (88, 111, 88), border)
    window.blit(gridSurf, gridRect)


def move(snake: list[list[int, str]], apple: list[int], turning: list[int, str]) -> bool:
    # Apply any changes to the direction of each snake part
    for turn in turning.copy():
        snake[turn[0]][2] = turn[1]
        if turn[0] == len(snake) - 1:
            turning.remove(turn)
        else:
            turn[0] += 1

    # Move the snake parts
    for i in range(len(snake)):
        direction = snake[i][2]
        snake[i][0] += DIRECTIONS[direction][0]
        snake[i][1] += DIRECTIONS[direction][1]

    # Check for an apple
    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        snake.append([snake[-1][0] - DIRECTIONS[snake[-1][2]][0], snake[-1][1] - DIRECTIONS[snake[-1][2]][1], snake[-1][2]])
        return True
    return False


def isDead(snake) -> bool:
    snakeHead = snake[0]
    # First Check board collision
    if snakeHead[0] < 0 or snakeHead[0] > GRID_SIZE:
        return True
    if snakeHead[1] < 0 or snakeHead[1] > GRID_SIZE:
        return True

    for body in snake[1:]:
        if snakeHead[0] == body[0] and snakeHead[1] == body[1]:
            return True
    return False


size: tuple[int] = 900, 720
window: pygame.SurfaceType = pygame.display.set_mode(size)
clock: pygame.time.Clock = pygame.time.Clock()

playerScore: int = 0
snake: list[list[int, str]] = [[GRID_SIZE // 4, GRID_SIZE // 2, "d"], [GRID_SIZE // 4 - 1, GRID_SIZE // 2, "d"]]
piecesTurning: list[int, str] = []
apple: tuple = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

running: bool = True
while running:
    pygame.display.set_caption("Snake | Score: " + str(playerScore))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode in "wasd":
                piecesTurning.append([0, event.unicode])
    if move(snake, apple, piecesTurning):
        apple = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        playerScore += 1
    if isDead(snake):
        print(playerScore)
        running = False

    window.fill((88, 222, 88))
    renderAll(window, snake, apple)

    clock.tick(4)
    pygame.display.flip()

pygame.quit()
