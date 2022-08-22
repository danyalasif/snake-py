from random import randint
import sys
import pygame
from pygame.math  import Vector2
cell_size = 40
cell_number = 20
class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.is_add_block = False

    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (126, 111, 100), snake_rect)

    def move_snake(self):
        if self.is_add_block:
            return
        snake_head = self.body[0]
            
        body_copy = self.body[:-1]
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

    def add_block(self):
        self.is_add_block = True
        snake_head = self.body[0]
        body_copy = self.body[:]
        body_copy.insert(0, snake_head + self.direction)
        self.body = body_copy
        self.is_add_block = False

    def check_fail(self):
        # check if snake collides with itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                pass

    def change_direction(self):
        pass
class Fruit:
    def __init__(self) -> None:
        self.randomize()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114),fruit_rect)
    
    def randomize(self):
        self.x = randint(0, cell_number - 1)
        self.y = randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class Score:
    def __init__(self) -> None:
        self.score = 0
        self.score_font = pygame.font.Font(None, 25)

    def draw_score(self):
        score_text = str(self.score)
        score_surface = self.score_font.render(score_text, True, (0, 0, 0))
        score_rect = score_surface.get_rect(center = (cell_size, cell_size))
        screen.blit(score_surface, score_rect)

    def increment(self):
        self.score += 1
class Main:
    def __init__(self) -> None:
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = Score()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.score.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.score.increment() 
            self.snake.add_block()


pygame.init()


screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

main_game = Main()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            snake_dir = main_game.snake.direction
            if event.key == pygame.K_UP and snake_dir.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and snake_dir.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and snake_dir.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and snake_dir.x != -1:
                main_game.snake.direction = Vector2(1, 0)
            

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)