import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Snake settings
snake_size = 20
snake_speed = 10

font = pygame.font.SysFont(None, 35)


def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])


def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(
            screen,
            GREEN,
            [segment[0], segment[1], snake_size, snake_size]
        )


def game():
    game_over = False

    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    # Frog (food)
    frog_x = random.randrange(0, WIDTH - snake_size, snake_size)
    frog_y = random.randrange(0, HEIGHT - snake_size, snake_size)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0

                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0

                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        x += x_change
        y += y_change

        # Wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        screen.fill(BLACK)

        # Draw frog
        pygame.draw.circle(
            screen,
            RED,
            (frog_x + snake_size // 2, frog_y + snake_size // 2),
            snake_size // 2
        )

        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > snake_length:
            del snake[0]

        # Self collision
        for segment in snake[:-1]:
            if segment == snake_head:
                game_over = True

        draw_snake(snake)

        # Frog eaten
        if x == frog_x and y == frog_y:
            frog_x = random.randrange(
                0, WIDTH - snake_size, snake_size
            )
            frog_y = random.randrange(
                0, HEIGHT - snake_size, snake_size
            )
            snake_length += 1

        show_score(snake_length - 1)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()


game()