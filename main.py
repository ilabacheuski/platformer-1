import pygame
from constants import *
from player import Player
from enemy import Enemy  
from bullet import Bullet
from level1 import Level1

pygame.init() # Инициализация pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создаем окно для отрисовки
pygame.display.set_caption(TITLE) # Устанавливает заголовок окна
clock = pygame.time.Clock()

basic_font = pygame.font.SysFont(None, 54)
game_over_text = basic_font.render("Game over", True, RED)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.centerx = screen.get_rect().centerx
game_over_text_rect.centery = screen.get_rect().centery

start_new_text = basic_font.render("Press <Enter> to start new game", True, RED)
start_new_text_rect = start_new_text.get_rect()
start_new_text_rect.midtop = (screen.get_rect().centerx, start_new_text_rect.h + 20)

def init():
    global running
    global game_over
    global all_sprites
    global player_sprite
    global player_shoots
    global enemies
    global player
    global enemy_count
    global start_ticks
    global level1

    running = True
    game_over = False

    all_sprites = pygame.sprite.Group()
    player_sprite = pygame.sprite.Group()
    player_shoots = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)
    player_sprite.add(player)

    first_enemy = Enemy()
    enemies.add(first_enemy)
    all_sprites.add(first_enemy)

    enemy_count = 0
    start_ticks = pygame.time.get_ticks()

    level1 = Level1()

init()

# Игровой цикл
while running:
    clock.tick(FPS)
    # events()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                (x, y) = player.rect.midtop
                shoot = Bullet(x, y)
                player_shoots.add(shoot)
                all_sprites.add(shoot)

    if (game_over):
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(start_new_text, start_new_text_rect)
        pygame.display.flip()
        while (game_over):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_over = False
                    init()
    else:
        # Update
        # spawn_enemy
        ticks = pygame.time.get_ticks()
        seconds = (ticks - start_ticks)
        if (enemy_count < MAX_ENEMIES and seconds >= ENEMY_RESPAWN_TIME):
            start_ticks = ticks
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)
            enemy_count +=1
        
        # kill enemy if they are at the end
        for enemy in enemies:
            if (enemy.rect.y >= HEIGHT):
                enemy.kill()
                enemy_count -=1

        # kill enemy if it is hit
        pygame.sprite.groupcollide(enemies, player_shoots, True, True)

        if (pygame.sprite.groupcollide(enemies, player_sprite, True, False)):
            game_over = True

        level1.update()
        all_sprites.update()

        screen.fill(RED)
        level1.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()
