import pygame as pg
import random as rd

pg.init()

# funcs
def draw_snake(snake):
    screen.fill(blue)
    for unit in snake:
        pg.draw.rect(screen, orange, [unit[0], unit[1], d, d])
    
def move_snake(delta_x, delta_y, snake):  
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                delta_x = -d
                delta_y = 0
            elif event.key == pg.K_RIGHT:
                delta_x = d
                delta_y = 0
            elif event.key == pg.K_UP:
                delta_x = 0
                delta_y = -d
            elif event.key == pg.K_DOWN:
                delta_x = 0
                delta_y = d
                
    new_x = snake[-1][0] + delta_x
    new_y = snake[-1][1] + delta_y
    
    snake.append([new_x, new_y])
    del snake[0]
    
    return delta_x, delta_y, snake

def eat_food(dx, dy, food_x, food_y, snake):
    head = snake[-1]
    
    new_x = head[0] + dx
    new_y = head[1] + dy
    
    if head[0] == food_x and head[1] == food_y:
        snake.append([new_x, new_y])
        food_x, food_y = random_food(food_x, food_y)
        
    pg.draw.rect(screen, green, [food_x, food_y, d, d])
    
    return food_x, food_y, snake
    
def random_food(food_x, food_y):
    food_x = round(rd.randrange(0, screen_dimen[0] - d) / 20) *20
    food_y = round(rd.randrange(0, screen_dimen[1] - d) / 20) *20
    
    return food_x, food_y

def wall_crash(snake):
    head = snake[-1]
    
    if head[0] not in range(screen_dimen[0] + 1) or head[1] not in range(screen_dimen[1] + 1):
        print('Wall crash')
        raise Exception
    
def snake_crash(snake):
    head = snake[-1]
    tail = snake.copy()
    del tail[-1]
    
    for x,y in tail:
        if head[0] == x and head[1] == y:
            print('Snake crash')
            raise Exception
        
def update_score(snake):
    snake_size = str(len(snake))
    score = font.render(str_score + snake_size, True, yellow)
    screen.blit(score, [0, 0])
        
# end funcs

# colors
blue = (50, 100, 213)
orange = (205, 102, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# const
screen_title = 'Snake'
screen_dimen = (800, 600)
x = 400
y = 300
d = 20
str_score = 'Score: '

snake = [[x, y]]

delta_x = 0
delta_y = 0

food_x, food_y = random_food(0, 0)
    
pg.display.set_caption(screen_title)

screen = pg.display.set_mode(screen_dimen)
screen.fill(blue)

font = pg.font.SysFont('arial', 30)

clock = pg.time.Clock()

while True:
    pg.display.update()
    draw_snake(snake)
    delta_x, delta_y, snake = move_snake(delta_x, delta_y, snake)
    food_x, food_y, snake = eat_food(delta_x, delta_y, food_x, food_y, snake)
    update_score(snake)
    wall_crash(snake)
    snake_crash(snake)
    clock.tick(5)