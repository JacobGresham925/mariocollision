import pygame
from pygame.sprite import Group

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from mario import Mario
from background import Background
import game_functions as gf
from block import Block

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()
    screen = pygame.display.set_mode((1000, 450))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()
    
    # Make the Play button.
    play_button = Button(screen, "Play")
    
    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats()
    sb = Scoreboard(screen, stats)
    
    # Set the background color.
    bg_color = (230, 230, 230)

    # load all sprite images
    large_regular_mario_images, small_regular_mario_images, \
    large_fire_mario_images, small_fire_mario_images, \
    large_star_mario_images, small_star_mario_images, \
    goomba_images, turtle_images, \
    mushroom_images, flower_images, question_block_images, star_images, static_coin_images, dynamic_coin_images, \
    overworld_brick_images, overworld_floor_image, \
    underworld_brick_image, underworld_floor_image, \
    vertical_pipe_images, horizontal_pipe_images = gf.get_sprites()

    # Make a mario, a group of bullets, and a group of enemies.
    background = Background(screen)
    mario = Mario(screen, small_regular_mario_images)
    bullets = Group()
    enemies = Group()

    # Create the fleet of enemies.
    # gf.create_enemies(screen, mario, enemies)

    pygame.mixer.music.load("sounds/overworld_theme.mp3")
    pygame.mixer.music.play(-1)
    block = Block(screen)
    # Start the main loop for the game.
    while True:
        gf.check_events(screen, stats, sb, play_button, mario,
            enemies, bullets)
        gf.check_collision(screen, mario, block)
        
        if stats.game_active:
            mario.update()
            # gf.update_enemies(screen, stats, sb, mario, enemies)
        
        gf.update_screen(screen_rect, stats, sb, background, mario, enemies, play_button, block)

        clock.tick(60)

run_game()
