import pygame

GRID_SIZE = 40
CELL_SIZE = 16


def renderAll(window: pygame.Surface, snake, apple: tuple[int]) -> None:
    # Make a new surface and fill it with grey
    gridSurf = pygame.Surface((GRID_SIZE * CELL_SIZE + 1, GRID_SIZE * CELL_SIZE + 1))
    gridSurf.fill('grey')
    # Draw 41 lines both vertically and horizontally to the new surface
    for i in range(41):
        pygame.draw.line(gridSurf, (0, 0, 0), (0, i * CELL_SIZE), (gridSurf.get_width(), i * CELL_SIZE))
        pygame.draw.line(gridSurf, (0, 0, 0), (i * CELL_SIZE, 0), (i * CELL_SIZE, gridSurf.get_height()))

    # Draw the apple
    # TODO

    # Draw the snake
    # TODO

    # Make a border around the grid
    border = pygame.Rect((0, 0), (gridSurf.get_width() + 20, gridSurf.get_height() + 20))

    # Make sure everything is centered based on the original window
    rect = window.get_rect()
    gridRect = gridSurf.get_rect(center=rect.center)
    border.center = rect.center

    # Draw the border and grid onto the window
    pygame.draw.rect(window, (88, 111, 88), border)
    window.blit(gridSurf, gridRect)


size: tuple[int] = 900, 720
window: pygame.SurfaceType = pygame.display.set_mode(size)
clock: pygame.time.Clock = pygame.time.Clock()

playerScore: int = 0
direction: str = "d"

running: bool = True
while running:
    pygame.display.set_caption("Snake | Score: " + str(playerScore))
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # if event.unicode.isalnum():
            #     print(event.unicode)
            if event.unicode in "wasd":
                direction = event.unicode

    window.fill((88, 222, 88))
    renderAll(window, [], (2, 2))

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
