import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((1000, 650))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - By Molly Sankey")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 51, 51)
green = (102, 255, 178)
teal = (0, 153, 153)

# Fonts for the game
score_font = pygame.font.SysFont("calibri", 20)
exit_font = pygame.font.SysFont("segoeuiblack", 30)
msg_font = pygame.font.SysFont("calibri", 50)

clock = pygame.time.Clock()  # Sets the speed at which the snake moves


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1000/2 = 500 and 650/2 = 325
    text_box = txt.get_rect(center=(500, 325))
    screen.blit(txt, text_box)


def game_loop():
    quit_game = False
    game_over = False

    # Snake will be 20 by 20 pixels
    snake_x = 490  # Centre point horizontally
    snake_y = 315  # Centre point vertically

    snake_x_change = 0  # holds the value change of the x co ordinant
    snake_y_change = 0  # holds the value change of the y co ordinant

    # Setting a random position for the food
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 650 - 20) / 20) * 20

    # Loop to keep screen open until user presses x
    while not quit_game:
        # give user the option to quit or play again when they die
        while game_over:
            screen.fill(green)
            message("YOU DIED! Press 'Q' to Quit or 'A' to Play Again", black,
                    green)
            pygame.display.update()

            # Check if user wants to quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()  # Restart the main game loop

        # Handling response if user presses 'X' - giving them the option to
        #  quit, start a new game, or keep playing

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to quit, space bar to resume, " \
                               "R to reset"
                message(instructions, green, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        # If user presses X button, game quits
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True

                        # If user presses R button again, game is reset
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()

                        # If user presses the space bar the game continues
                            if event.key == pygame.K_SPACE:
                                end = True

                        # If the user presses 'Q' game quits
                            if event.key == pygame.K_q:
                                quit_game = True
                                end = True



            # Handling snake movement
            if event.type == pygame.KEYDOWN:
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

        if snake_x >= 1000 or snake_x < 0 or snake_y >= 650 or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)  # Changes background to green

        # Create the snake body (rectangle)
        pygame.draw.rect(screen, teal, [snake_x, snake_y, 20, 20])
        pygame.display.update()

        # Create circle for the food
        pygame.draw.circle(screen, red, [food_x, food_y], 10)
        pygame.display.update()

        # Collision detection (test if snake touches food)
        if snake_x == food_x - 10 and snake_y - 10:
            # Set new random position if snake touches it
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 650 - 20) / 20) * 20

        clock.tick(5)  # sets the speed which each iteration of the game
        # runs the in frames per second

    pygame.quit()
    quit()


# Main Routine
game_loop()
