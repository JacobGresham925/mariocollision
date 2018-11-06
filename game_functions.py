import sys
from time import sleep
import spritesheet
import pygame

from bullet import Bullet
from enemy import Enemy
def play_sound(sound):
    small_jump_sound = pygame.mixer.Sound('sounds/jump_small.wav')
    if sound == "small_jump":
        small_jump_sound.play()

def check_keydown_events(event, mario):
    """Respond to keypresses."""

    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
        mario.last_direction = "right"
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True
        mario.last_direction = "left"
    elif event.key == pygame.K_SPACE:
        play_sound("small_jump")
        jump_super(mario)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, mario):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False
    elif event.key == pygame.K_SPACE:
        jump_small(mario)

def check_events(screen, stats, sb, play_button, mario, enemies,
        bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, stats, sb, play_button,
                mario, enemies, bullets, mouse_x, mouse_y)

def check_collision(screen, mario, block):
    if pygame.Rect.colliderect(mario.rect3, block.rect):
        if mario.y_veloctiy < 0:
            mario.rect.top = block.rect.bottom + 4
            block.rect.centery -= .1
    elif pygame.Rect.colliderect(mario.rect, block.rect):
        if mario.x_velocity > 0:
            # mario.rect.centerx -= mario.x_velocity
            mario.rect.right = block.rect.left
            mario.x_velocity = 0

        if mario.x_velocity < 0:
            # mario.rect.centerx += mario.x_velocity
            mario.rect.left = block.rect.right
            mario.x_velocity = 0

    elif pygame.Rect.colliderect(mario.rect2, block.rect):
        if mario.y_veloctiy < 0:

            if not mario.on_the_ground and mario.onblock:
                mario.rect.bottom = block.rect.top - 4
                mario.on_the_ground = True
                mario.y_veloctiy = 0
                mario.onblock = True
            # elif mario.on_the_ground:


            # mario.rect.centery += mario.y_veloctiy
            # block.rect.centery += mario.y_veloctiy

        if mario.y_veloctiy > 0:
            mario.rect.bottom = block.rect.top
            mario.on_the_ground = True
            mario.y_veloctiy = 0

    if not pygame.Rect.colliderect(mario.rect2, block.rect) and mario.rect.bottom < mario.screen_rect.bottom - 48:
        mario.on_the_ground = False
        mario.onblock = False

            
def check_play_button(screen, stats, sb, play_button, mario,
        enemies, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        
        
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        # sb.prep_marios()
        
        # Empty the list of enemies and bullets.
        enemies.empty()

        
        # Create a new fleet and center the mario.
        # create_enemies(screen, mario, enemies)
        mario.center_mario()


def update_screen(screen_rect, stats, sb, background, mario, enemies, play_button, block):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    # screen.fill((255, 255, 255))
    if mario.rect.centerx > screen_rect.centerx:
        mario.rect.centerx -= mario.x_velocity
        background.rect.centerx -= mario.x_velocity

    # draw the background, mario, and enemies.
    background.blitme()
    block.blitme()
    mario.blitme()
    # enemies.draw(screen)
    
    # Draw the score information.
    # sb.show_score()
    
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    
        
# def check_high_score(stats, sb):
#     """Check to see if there's a new high score."""
#     if stats.score > stats.high_score:
#         stats.high_score = stats.score
#         sb.prep_high_score()

    
# def mario_hit(screen, stats, sb, mario, enemies):
#     """Respond to mario being hit by enemy."""
#     if stats.marios_left > 0:
#         # Decrement marios_left.
#         stats.marios_left -= 1
#
#         # Update scoreboard.
#         sb.prep_marios()
#
#     else:
#         stats.game_active = False
#         pygame.mouse.set_visible(True)
#
#     # Empty the list of enemies and bullets.
#     enemies.empty()
#
#     # Create a new fleet, and center the mario.
#     # create_enemies(screen, mario, enemies)
#     mario.center_mario()
#
#     # Pause.
#     sleep(0.5)


def jump_super(mario):
    if mario.on_the_ground:
        mario.on_the_ground = False
        mario.y_veloctiy = -7.0

def jump_small(mario):
    if mario.y_veloctiy < -3.0:
        mario.y_veloctiy = -3.0



def get_sprites():
    mario_ss_file = 'images/Mario_Spritesheet.png'
    fire_mario_ss_file = 'images/Fire Mario.png'
    star_mario_ss_file = 'images/Invincible Mario.png'
    enemies_ss_file = 'images/enemies.png'
    items_ss_file = 'images/Mushroom, Flower, Star, Question Block, Static Coin, Dynamic Coin.png'
    blocks_ss_file = 'images/OWBrick, OWFloor, UWFloor, HitTile.png'
    pipes_ss_file = 'images/Pipe.png'

    mario_ss = spritesheet.spritesheet(mario_ss_file)
    fire_mario_ss = spritesheet.spritesheet(fire_mario_ss_file)
    star_mario_ss = spritesheet.spritesheet(star_mario_ss_file)
    enemies_ss = spritesheet.spritesheet(enemies_ss_file)
    items_ss = spritesheet.spritesheet(items_ss_file)
    blocks_ss = spritesheet.spritesheet(blocks_ss_file)
    pipes_ss = spritesheet.spritesheet(pipes_ss_file)

    # MARIO-------------------------------------------------------------------------------------------------------------
    #   Retrieve Regular Mario
    #       Retrieve large regular Mario sprites
    large_regular_mario_images = []
    num_large_mario_sprites = 21
    width_large_mario_sprites = 18
    height_large_mario_sprites = 34
    for num in range(num_large_mario_sprites):
        x = num * width_large_mario_sprites
        rect = ((x, 0), (width_large_mario_sprites, height_large_mario_sprites))
        large_regular_mario_images.append(mario_ss.image_at(rect, -1))
    #       Retrieve small regular Mario sprites
    small_regular_mario_images = []
    num_small_mario_sprites = 14
    width_small_mario_sprites = 17
    height_small_mario_sprites = 17
    for num in range(num_small_mario_sprites):
        x = num * width_small_mario_sprites
        rect = ((x, 34), (width_small_mario_sprites, height_small_mario_sprites))
        small_regular_mario_images.append(mario_ss.image_at(rect, -1))

    #   Retrieve Fire Mario
    #       Retrieve large Fire Mario sprites
    large_fire_mario_images = []
    for num in range(num_large_mario_sprites):
        x = num * width_large_mario_sprites
        rect = ((x, 0), (width_large_mario_sprites, height_large_mario_sprites))
        large_fire_mario_images.append(fire_mario_ss.image_at(rect, -1))
    #       Retrieve small Fire Mario sprites
    small_fire_mario_images = []
    for num in range(num_small_mario_sprites):
        x = num * width_small_mario_sprites
        rect = ((x, 34), (width_small_mario_sprites, height_small_mario_sprites))
        small_fire_mario_images.append(fire_mario_ss.image_at(rect, -1))

    #   Retrieve Star Mario
    #       Retrieve large Star Mario sprites
    large_star_mario_images = []
    for num in range(num_large_mario_sprites):
        x = num * width_large_mario_sprites
        rect = ((x, 0), (width_large_mario_sprites, height_large_mario_sprites))
        large_star_mario_images.append(star_mario_ss.image_at(rect, -1))
    #       Retrieve small Star Mario sprites
    small_star_mario_images = []
    for num in range(num_small_mario_sprites):
        x = num * width_small_mario_sprites
        rect = ((x, 34), (width_small_mario_sprites, height_small_mario_sprites))
        small_star_mario_images.append(star_mario_ss.image_at(rect, -1))

    # ENEMIES-----------------------------------------------------------------------------------------------------------
    #   Retrieve Goomba sprites
    goomba_images = [
        enemies_ss.image_at((0, 4, 16, 16), -1),
        enemies_ss.image_at((30, 4, 16, 16), -1),
        enemies_ss.image_at((60, 4, 16, 8), -1)
    ]

    #   Retrieve Turtle sprites
    turtle_images = []
    num_turtle_sprites = 10
    width_turtle_sprites = 16
    height_turtle_sprites = 24
    height_shell_sprites = 16
    for num in range(num_turtle_sprites):
        x = (num * width_turtle_sprites) + 90  # 90 from Goomba sprites
        if num < 8:
            rect = ((x, 4), (width_turtle_sprites, height_turtle_sprites))
        else:
            rect = ((x, 4), (width_turtle_sprites, height_shell_sprites))
        turtle_images.append(enemies_ss.image_at(rect, -1))
    # ITEMS-------------------------------------------------------------------------------------------------------------
    #   Retrieve Mushroom sprites
    mushroom_images = [
        items_ss.image_at((0, 0, 16, 16), -1),
        items_ss.image_at((16, 0, 16, 16), -1),
        items_ss.image_at((32, 0, 16, 16), -1)
    ]

    #   Retrieve Flower sprites
    flower_images = [
        items_ss.image_at((0, 32, 16, 16), -1),
        items_ss.image_at((16, 32, 16, 16), -1),
        items_ss.image_at((32, 32, 16, 16), -1),
        items_ss.image_at((48, 32, 16, 16), -1)
    ]

    #   Retrieve Star sprites
    star_images = [
        items_ss.image_at((0, 48, 16, 16), -1),
        items_ss.image_at((16, 48, 16, 16), -1),
        items_ss.image_at((32, 48, 16, 16), -1),
        items_ss.image_at((48, 48, 16, 16), -1)
    ]

    question_block_images = [
        items_ss.image_at((0, 80, 16, 16), -1),
        items_ss.image_at((16, 80, 16, 16), -1),
        items_ss.image_at((32, 80, 16, 16), -1),
        items_ss.image_at((48, 80, 16, 16), -1),
        blocks_ss.image_at((47, 0, 16, 16), -1)  # Image of the question post-hit in different file
    ]

    static_coin_images = [
        items_ss.image_at((0, 96, 16, 16), -1),
        items_ss.image_at((16, 96, 16, 16), -1),
        items_ss.image_at((32, 96, 16, 16), -1),
        items_ss.image_at((48, 96, 16, 16), -1)
    ]

    dynamic_coin_images = [
        items_ss.image_at((0, 112, 16, 16), -1),
        items_ss.image_at((16, 112, 16, 16), -1),
        items_ss.image_at((32, 112, 16, 16), -1),
        items_ss.image_at((48, 112, 16, 16), -1)
    ]

    # BRICK-------------------------------------------------------------------------------------------------------------
    overworld_brick_images = [
        blocks_ss.image_at((16, 0, 16, 16), -1),
        blocks_ss.image_at((32, 0, 16, 16), -1)
    ]
    overworld_floor_image = blocks_ss.image_at((0, 0, 16, 16), -1)

    underworld_brick_image = blocks_ss.image_at((16, 32, 16, 16), -1)
    underworld_floor_image = blocks_ss.image_at((0, 32, 16, 16), -1)

    # PIPES-------------------------------------------------------------------------------------------------------------
    vertical_pipe_images = [
        pipes_ss.image_at((0, 0, 32, 32), -1),
        pipes_ss.image_at((0, 32, 32, 32), -1)
    ]

    horizontal_pipe_images = [
        pipes_ss.image_at((32, 0, 48, 32), -1),
        pipes_ss.image_at((32, 32, 48, 32), -1)
    ]

    return large_regular_mario_images, small_regular_mario_images, \
        large_fire_mario_images, small_fire_mario_images, \
        large_star_mario_images, small_star_mario_images, \
        goomba_images, turtle_images, \
        mushroom_images, flower_images, question_block_images, star_images, static_coin_images, dynamic_coin_images, \
        overworld_brick_images, overworld_floor_image, \
        underworld_brick_image, underworld_floor_image, \
        vertical_pipe_images, horizontal_pipe_images