import pygame
import random

pygame.init()
WIDTH = 900
HEIGHT = 400
FPS = 60
COIN_SPEED_INCREASE = 0.5
VELOCITY  = 5.75
points = 0
lives = 5
coin_speed = 5

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

sound_coin = pygame.mixer.Sound("feed_the_dragon_assets/coin_sound.wav")
sound_coin_miss = pygame.mixer.Sound("feed_the_dragon_assets/miss_sound.wav")
sound_coin_miss.set_volume(0.5)

pygame.mixer.music.load("feed_the_dragon_assets/ftd_background_music.wav")
game_music = pygame.mixer.music.play(-1)

font = pygame.font.init()
game_font = pygame.font.Font('feed_the_dragon_assets/AttackGraffiti.ttf', 24)
game_over_font = pygame.font.Font('feed_the_dragon_assets/AttackGraffiti.ttf', 40)

game_title_text = game_font.render("FEED THE DRAGON", True, (0,255,0),(0,125,255))
game_title_react = game_title_text.get_rect()
game_title_react.center = (400,35)

game_over_text = game_over_font.render("GAME OVER ", True, (0,255,0))
game_over_react = game_over_text.get_rect()
game_over_react.center = (400,170)

press_key_text = game_over_font.render("PRESS ANY KEY TO CONTINUE", True, (0,255,0))
press_key_rect = press_key_text.get_rect()
press_key_rect.center = (400,230)

dragon_image = pygame.image.load("feed_the_dragon_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.bottomleft = (50, 260)

coin_image = pygame.image.load("feed_the_dragon_assets/coin.png")
coin_rect = coin_image.get_rect()
coin_random_positon_y = random.randint(80 + coin_rect.height,400 + coin_rect.height)
coin_rect.bottomleft = (900, coin_random_positon_y)


run = True
clock = pygame.time.Clock()

while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and dragon_rect.y > 80:
        dragon_rect.y -= VELOCITY

    if keys[pygame.K_DOWN] and dragon_rect.y < 400 - dragon_rect.height:
        dragon_rect.y += VELOCITY

    if lives == 0:
        window_surface.blit(game_over_text, game_over_react)
        window_surface.blit(press_key_text, press_key_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    lives = 5
                    points = 0
                    coin_speed = 0
                    pause = False




    if coin_rect.x < 0:
        lives -= 1
        coin_rect.y = random.randint(80+coin_rect.height,390-coin_rect.height)
        coin_rect.x = 900
        sound_coin_miss.play()

    if dragon_rect.colliderect(coin_rect):
        points += 1
        coin_rect.y = random.randint(80+coin_rect.height,390-coin_rect.height)
        coin_rect.x = 900
        coin_speed += COIN_SPEED_INCREASE
        sound_coin.play()



    lives_text = game_font.render(f"Lives: {lives}", True, (0, 255, 0))
    lives_text_react = lives_text.get_rect()
    lives_text_react.center = (750, 35)

    points_text = game_font.render(f"Points: {points}", True, (0, 255, 0))
    points_text_react = points_text.get_rect()
    points_text_react.center = (70, 35)

    window_surface.fill((0,0,0))
    pygame.draw.line(window_surface, (255, 255, 255), (0, 80), (WIDTH, 80),3)
    window_surface.blit(points_text, points_text_react)
    window_surface.blit(lives_text, lives_text_react)
    window_surface.blit(game_title_text, game_title_react)
    window_surface.blit(dragon_image, dragon_rect)
    window_surface.blit(coin_image, coin_rect)

    coin_rect.x -= coin_speed



    pygame.display.update()

    clock.tick(FPS)

pygame.quit()