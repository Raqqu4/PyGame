import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    rad = 20
    color = pygame.Color(pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), rad))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 255))
        for i in range(100000):
            screen.fill(pygame.Color())
        :
        pygame.display.flip()

    pygame.quit()
