import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong O\'yini')

paddle_width, paddle_height = 10, 100
ball_size = 20

paddle_speed = 7
ball_speed_x, ball_speed_y = 5, 5

left_paddle = pygame.Rect(30, (HEIGHT - paddle_height) // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(WIDTH - 30 - paddle_width, (HEIGHT - paddle_height) // 2, paddle_width, paddle_height)
ball = pygame.Rect((WIDTH - ball_size) // 2, (HEIGHT - ball_size) // 2, ball_size, ball_size)

# Hisoblar
left_score = 0
right_score = 0

font = pygame.font.Font(None, 74)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed

    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = -ball_speed_x

    if ball.left <= 0:
        right_score += 1
        ball.x = (WIDTH - ball_size) // 2
        ball.y = (HEIGHT - ball_size) // 2
        ball_speed_x = -ball_speed_x

    if ball.right >= WIDTH:
        left_score += 1
        ball.x = (WIDTH - ball_size) // 2
        ball.y = (HEIGHT - ball_size) // 2
        ball_speed_x = -ball_speed_x

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

    pygame.display.flip()
    clock.tick(60)
