import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1000, 650))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - By Molly Sankey")

# Tuples containing the colours to be used in the game
Black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 51, 51)
green = (102, 255, 178)
teal = (0, 153, 153)

# Fonts for the game
score_font = pygame.font.SysFont("calibri", 20)
exit_font = pygame.font.SysFont("segoeuiblack", 30)

clock = pygame.time.Clock() # Sets the speed at which the snake moves

quit_game = False

# Snake will be 20 by 20 pixels
snake_x = 490  # Centre point horizontally
snake_y = 315  # Centre point vertically

snake_x_change = 0 # holds the value change of the x co ordinant
snake_y_change = 0 # holds the value change of the y co ordinant

# Loop to keep screen open until user presses x
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame. KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -20
            elif event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = 20

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green) # Changes background to green

    # Create the snake body (rectangle)
    pygame.draw.rect(screen, teal, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(5) # sets the speed which each iteration of the game
    # runs the in frames per second

pygame.quit()
quit()
