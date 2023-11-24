import pygame
import random


if __name__ == '__main__':
    w, n = map(int, input().split())

    pygame.init()

    size = width, height = w, w
    screen = pygame.display.set_mode(size)
    xc, yc = width // 2, height // 2
    screen.fill('white')
    # drawing...
    for r in range(n):
        for c in range(n):
            if (r + c) % 2 == 0:
                screen.fill('black', pygame.Rect(c * (w // n), r * (w // n), w // n, w // n))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
