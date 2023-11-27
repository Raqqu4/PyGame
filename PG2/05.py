import random
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Bouncy balls')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    rad = 10
    balls = []
    clock = pygame.time.Clock()
    screen.fill('black')
    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                v = random.randint(50, 100)
                color = pygame.Color('#{:02x}{:02x}{:02x}'.format(random.randrange(256),
                                                                  random.randrange(256),
                                                                  random.randrange(256)))
                balls.append([[event.pos[0], event.pos[1]], [-1, 1], color, v])

        for ball in balls:
            ball[0][0] += ball[1][0] * (ball[3] / 1000)
            ball[0][1] += ball[1][1] * (ball[3] / 1000)
            if ball[0][0] < rad:
                ball[0][0] = rad + 1
                ball[1][0] *= -1

            if ball[0][1] < rad:
                ball[0][1] = rad
                ball[1][1] *= -1

            if ball[0][0] > width - rad:
                ball[0][0] = width - rad
                ball[1][0] *= -1

            if ball[0][1] > height - rad:
                ball[0][1] = height - rad
                ball[1][1] *= -1
        for ball in balls:
            pygame.draw.circle(screen, ball[2], ball[0], rad)

        pygame.display.flip()
    pygame.quit()
