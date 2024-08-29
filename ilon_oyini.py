import pygame
import random

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = 'RIGHT'
        self.food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                     random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
        self.speed = 3 
        self.increase_speed = 0.5 

    def run(self):
        while self.running:
            self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.direction = 'RIGHT'

            head_x, head_y = self.snake[0]
            if self.direction == 'UP':
                head_y -= BLOCK_SIZE
            elif self.direction == 'DOWN':
                head_y += BLOCK_SIZE
            elif self.direction == 'LEFT':
                head_x -= BLOCK_SIZE
            elif self.direction == 'RIGHT':
                head_x += BLOCK_SIZE

            if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or (head_x, head_y) in self.snake:
                self.running = False

            new_head = (head_x, head_y)
            self.snake = [new_head] + self.snake[:-1]

            if self.snake[0] == self.food:
                self.snake.append(self.snake[-1])
                self.food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                             random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
                self.speed += self.increase_speed 

            for segment in self.snake:
                pygame.draw.rect(self.screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.screen, RED, (*self.food, BLOCK_SIZE, BLOCK_SIZE))

            pygame.display.flip()
            self.clock.tick(self.speed)

        pygame.quit()

if __name__ == "__main__":
    SnakeGame().run()
