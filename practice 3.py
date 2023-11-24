import pygame
import random


if __name__ == '__main__':
    n, k = map(int, input().split())

    pygame.init()

    size = width, height = 2 * n * k, 2 * n * k
    screen = pygame.display.set_mode(size)
    xc, yc = width // 2, height // 2
    colors = ('blue', 'red', 'green')
    # drawing...
    for i in range(k, 0, -1):
        pygame.draw.circle(screen, colors[i % 3], (xc, yc), n * i)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
