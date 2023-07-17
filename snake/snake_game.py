import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (1, 55, 32)
VELOCITY_X = 0
VELOCITY_Y = 0
FPS = 10
snake_pos_x = 400
snake_pos_y = 400
score = 0
snake_list = []
snake_head_cord = 0

window_surface = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.font.init()
sound = pygame.mixer.Sound("pick_up_sound.wav")


def display_mesh():
    x = 25
    y = 25
    for i in range(1,WIDTH//25):
        pygame.draw.line(window_surface, WHITE, (0,y),(WIDTH,y))
        y = y + 25
    for i in range(1,HEIGHT//25):
        pygame.draw.line(window_surface, WHITE, (x,0),(x,HEIGHT))
        x = x + 25

def random_postition_apple():
    postitonX = random.randint(0,31) * 25 + 13
    return postitonX

def create_apple(positionX, postionY, color):
    apple = pygame.draw.circle(window_surface, color,(positionX, postionY),11)
    return apple

def snake(postionX, postionY, color):
    snake = pygame.draw.rect(window_surface, color, (postionX,postionY,25,25))
    return snake

def snake_hit_wall(postionX,postionY):
    if postionX < 0 or postionX > WIDTH - 25:
        return True
    elif postionY < 0 or postionY > HEIGHT -25:
        return True
    else:
        return False

def game_over():
    pause = True
    pygame.display.update()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pause = False
def draw_text(text, postionX, postionY, text_size):
    font = pygame.font.SysFont("arial", text_size)
    text_to_display = font.render(text,True,WHITE, 24)
    text_rect = text_to_display.get_rect()
    text_rect.center = (postionX, postionY)
    return  text_to_display, text_rect


apple_pos_x = random_postition_apple()
apple_pos_y = random_postition_apple()
run = True
while run:

    window_surface.fill((0,0,0))
    score_text , score_rect = draw_text(f"Score: {score}", 70, 50, 30)
    clock.tick(FPS)
    apple = create_apple(apple_pos_x, apple_pos_y, RED)
    window_surface.blit(score_text, score_rect)
    snake_head = snake(snake_pos_x,snake_pos_y,GREEN)
    snake_head_cord = [snake_pos_x, snake_pos_y, 25, 25]
    press_key_text, press_key_text_rect = draw_text("Press any key to play again", WIDTH//2, HEIGHT//2 + 60, 40)
    game_over_text, game_over_text_rect = draw_text("GAME OVER", WIDTH//2, HEIGHT//2, 40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()



    if keys[pygame.K_UP]:
        VELOCITY_Y = -25
        VELOCITY_X = 0
    if keys[pygame.K_DOWN]:
        VELOCITY_Y = 25
        VELOCITY_X = 0
    if keys[pygame.K_LEFT]:
        VELOCITY_Y = 0
        VELOCITY_X = -25
    if keys[pygame.K_RIGHT]:
        VELOCITY_Y = 0
        VELOCITY_X = 25

    for snake_body in range(1, len(snake_list)):
        if snake_list[snake_body] == snake_head_cord:
            window_surface.blit(game_over_text, game_over_text_rect)
            window_surface.blit(press_key_text, press_key_text_rect)
            game_over()
            snake_pos_x = 400
            snake_pos_y = 400
            VELOCITY_Y = 0
            VELOCITY_X = 0
            score = 0
            snake_list.clear()
    if snake_head.colliderect(apple):
        score += 1
        new_snake  = [snake_pos_x, snake_pos_y, 25, 25]
        snake_list.append(new_snake)
        apple_pos_x = random_postition_apple()
        apple_pos_y = random_postition_apple()
        sound.play()




    snake_list.insert(0, snake_head_cord)
    snake_pos_x += VELOCITY_X
    snake_pos_y += VELOCITY_Y
    snake_head.move_ip(snake_pos_x, snake_pos_y)

    for snake_body in snake_list:
        pygame.draw.rect(window_surface, GREEN, snake_body)



    snake_list.pop()

    if snake_hit_wall(snake_pos_x, snake_pos_y):
        window_surface.blit(game_over_text, game_over_text_rect)
        window_surface.blit(press_key_text, press_key_text_rect)
        game_over()
        snake_pos_x = 400
        snake_pos_y = 400
        VELOCITY_Y = 0
        VELOCITY_X = 0
        score = 0
        snake_list.clear()
    # display_mesh()
    pygame.display.update()

pygame.quit()