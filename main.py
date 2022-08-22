from random import randint
import sys
import pygame
from pygame.math  import Vector2
cell_size = 40
cell_number = 20
class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (126, 111, 100), snake_rect)

    def move_snake(self):
        snake_head = self.body[0]
            
        body_copy = self.body[:-1]
        print(snake_head.x)
        if snake_head.x < 0:
            snake_head = Vector2(cell_number, snake_head.y)
        elif snake_head.x > cell_number:
            snake_head = Vector2(-1, snake_head.y)
        if snake_head.y < 0:
            snake_head = Vector2(snake_head.x, cell_number)
        elif snake_head.y > cell_number:
            snake_head = Vector2(snake_head.x, -1)
        body_copy.insert(0, snake_head + self.direction)
        self.body = body_copy

    def change_direction(self):
        pass
class Fruit:
    def __init__(self) -> None:
        self.x = randint(0, cell_number - 1)
        self.y = randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114),fruit_rect)

pygame.init()


screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

fruit = Fruit()
snake = Snake()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            snake.move_snake()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)
            

    screen.fill((175, 215, 70))
    fruit.draw_fruit()    
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)