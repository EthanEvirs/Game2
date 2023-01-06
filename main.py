import pygame
import constants
from character import Character

pygame.init()
# adding constants. before the screen width and height allows us to pull from another file.
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Earthbound")

# create clock for maintaning framerate
clock = pygame.time.Clock()


# define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

player_image = pygame.image.load("assets/player.png").convert_alpha()


# create player:
player = Character(100, 100, player_image)


# main game loop
run = True
while run:

    # control framerate
    clock.tick(constants.FPS)

    screen.fill(constants.BG)

    # calulate player movement
    dx = 0
    dy = 0
    if moving_right == True:
        dx = constants.SPEED
    if moving_left == True:
        dx = -constants.SPEED
    if moving_up == True:
        dy = -constants.SPEED
    if moving_down == True:
        dy = constants.SPEED

    # move player
    player.move(dx, dy)

    # draw player on screen
    player.draw(screen)
    # for any events in the game we use this handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # take keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
        # keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()


pygame.quit()