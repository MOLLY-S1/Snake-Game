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

# Snake will be 20 by 20 pixels
snake_x = 490  # Centre point horizontally
snake_y = 315  # Centre point vertically

# Loop to keep screen open until user presses x
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    # Create the snake body (rectangle)
    pygame.draw.rect(screen, teal, [snake_x, snake_y, 20, 20])
    pygame.display.update()
pygame.quit()
quit()
