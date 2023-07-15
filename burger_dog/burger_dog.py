import pygame
import random

pygame.init()

WIDTH = 750
HEIGHT = 600
WHITE = (255, 255, 255)
VELOCITY = 8
BURGER_SPEED_INCREASE = 0
FPS = 60
lives = [3]
burgers_eaten = 0
score = 0
current_burger_points = 0
boost = 0

pygame.font.init()
font = pygame.font.Font("burger_dog_assets/WashYourHand.ttf",28)
window_surface = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def draw_text(text, postionX, postionY):
    text = font.render(text, True, (255, 200, 0), 25)
    text_rect = text.get_rect()
    text_rect.center = (postionX, postionY)
    return text, text_rect

def draw_image(image, postionX, postionY):
    image = pygame.image.load(image)
    image_rect = image.get_rect()
    image_rect.center = (postionX, postionY)
    return image, image_rect

def pause_game(lives = []):

        pause = True
        pygame.display.update()
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    lives[0] = 3
                    pause = False

def burger_points(postionY):
    points = 4000 - postionY * 6
    return points

def boost_points(burrger_points):
    boost = burrger_points//100
    return boost

game_title_text, game_title_text_rect = draw_text("Burger Dog",WIDTH//2, 25)

burger_image_path = "burger_dog_assets/burger.png"
burger_image, burger_rect = draw_image(burger_image_path, random.randint(20, WIDTH - 20), -20)

dog_right_path = "burger_dog_assets/dog_right.png"
dog_left_path = "burger_dog_assets/dog_left.png"

dog_right_image , dog_right_rect = draw_image(dog_right_path, 350, 400)
dog_left_image , dog_left_rect = draw_image(dog_left_path, 350, 400)

dog_left_image = pygame.image.load("burger_dog_assets/dog_left.png")
dog_left_rect = dog_left_image.get_rect()
dog_left_rect.center = (350,400)
dog_image = dog_right_image
dog_rect = dog_right_rect

run = True

while run:
    current_burger_points = burger_points(burger_rect.y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dog_rect.x > 0:
        dog_image = dog_left_image
        dog_rect.x -= VELOCITY

    if keys[pygame.K_RIGHT] and dog_rect.x < WIDTH - dog_rect.width:
        dog_image = dog_right_image
        dog_right_rect.x += VELOCITY

    if keys[pygame.K_UP] and dog_rect.y > 100:
        dog_rect.y -= VELOCITY

    if keys[pygame.K_DOWN] and dog_rect.y < 600 - dog_rect.height:
        dog_rect.y += VELOCITY

    if keys[pygame.K_SPACE]:
        boost -= 1
        speed_increase = 15
        VELOCITY = speed_increase
        if boost < 0:
            boost = 0
    else:
        VELOCITY = 7
    if dog_rect.colliderect(burger_rect):
        score += current_burger_points
        burger_rect.y = -20
        burger_rect.x = random.randint(20,WIDTH-20)
        burgers_eaten += 1
        BURGER_SPEED_INCREASE += 0.25
        boost += boost_points(current_burger_points)
        if boost > 100:
            boost = 100



    if burger_rect.y > HEIGHT:
        burger_rect.y = -20
        burger_rect.x = random.randint(20,WIDTH-20)
        dog_rect.center = (350,400)
        BURGER_SPEED_INCREASE = 0
        lives[0] -= 1

    window_surface.fill((0, 0, 0))

    burgers_eaten_text, burgers_eaten_rect = draw_text(f"Burgers Eaten: {burgers_eaten}", WIDTH//2, 72)
    lives_text, lives_text_rect = draw_text(f"Lives: {lives[0]}", 680, 25)
    score_text, score_rect = draw_text(f"Score: {score}", 90, 72)
    final_score_text, final_score_rect = draw_text(f"Final score: {score}", WIDTH//2, HEIGHT//2)
    press_key_text, press_key_rect = draw_text("Press any key to play again", WIDTH//2, HEIGHT//2+40)
    burger_points_text, burger_points_rect = draw_text(f"Burger Points: {current_burger_points}", 125, 25)
    boost_text , boost_rect = draw_text(f"Boost: {boost}", 680, 72)
    line = pygame.draw.line(window_surface, WHITE, (0,100), (WIDTH,100),2)
    window_surface.blit(dog_image, dog_rect)
    window_surface.blit(burger_image, burger_rect)
    window_surface.blit(burgers_eaten_text, burgers_eaten_rect)
    window_surface.blit(lives_text, lives_text_rect)
    window_surface.blit(game_title_text, game_title_text_rect)
    window_surface.blit(score_text, score_rect)
    window_surface.blit(burger_points_text, burger_points_rect)
    window_surface.blit(boost_text, boost_rect)

    burger_rect.y += 5 + BURGER_SPEED_INCREASE
    clock.tick(FPS)
    pygame.display.update()

    if lives[0] == 0:
        window_surface.blit(final_score_text, final_score_rect)
        window_surface.blit(press_key_text, press_key_rect)
        pause_game(lives)
        burgers_eaten = 0
        score = 0
        boost = 0




pygame.quit()