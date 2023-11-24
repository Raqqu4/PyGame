import pygame
import random


if __name__ == '__main__':
    pygame.init()

    size = width, height = 800, 600

    screen = pygame.display.set_mode(size)

    # drawing...
    for i in range(10000):
        screen.fill(pygame.Color(f'#{:02h}{:02h}{:02h}'.format.random.randint()),
                    (random.random() * width,
                     random.random() * height, 1, 1))

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
