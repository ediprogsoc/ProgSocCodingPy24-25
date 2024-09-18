import pygame

size: tuple[int] = 800, 600
window: pygame.SurfaceType = pygame.display.set_mode(size)
clock: pygame.time.Clock = pygame.time.Clock()

pygame.display.set_caption("Game")

running: bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill("red")
    clock.tick(60)
    pygame.display.flip()

pygame.quit()


def makeImage(path: str) -> pygame.Surface:
    img = pygame.image.load(path).convert()
    return img


def makeText(text: str, size: int, fontName: str = "") -> pygame.Surface:
    fontName: str = fontName if fontName != "" else pygame.font.get_default_font()
    font: pygame.font.Font = pygame.font.SysFont(fontName, size)
    text: pygame.Surface = font.render(text, 1, (0, 0, 0))
    return text
