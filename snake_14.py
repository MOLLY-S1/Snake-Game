import pygame
import time
import random

pygame.init()

# Create the game display
screen = pygame.display.set_mode((1000, 750))  # changed coords
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
score_font = pygame.font.SysFont("segoeuiblack", 20)
exit_font = pygame.font.SysFont("segoeuiblack", 30)
msg_font = pygame.font.SysFont("calibri", 50)

clock = pygame.time.Clock()  # Sets the speed at which the snake moves


# Function to keep track of players high score - writes the value to a file
def load_high_score():
    try:
        hi_score_file = open("HI-Score.txt", 'r')
    except IOError:
        hi_score_file = open("HI_ score.txt", 'w')
        hi_score_file.write("0")
    hi_score_file = open("HI_ score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value


# Function to update record of the highest score
def update_high_score(score, high_score):
    if int(score) > int(high_score):
        return score
    else:
        return high_score


# Save updated high score if player beats it
def save_high_score(high_score):
    high_score_file = open("HI_ score.txt", 'w')
    high_score_file.write(str(high_score))
    high_score_file.close()


# Display players score and high score
def player_score(score, score_colour, hi_score):
    # Current score
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (800, 20))  # Coordinates for top right

    # High Score
    display_score = score_font.render(f"High Score: {hi_score}", True, score_colour)
    screen.blit(display_score, (10,10)) # coordinats for top left

# Draw the snake
def draw_snake(snake_list):
    print(f"Snake List: {snake_list}")  # for testing purposes
    for i in snake_list:
        pygame.draw.rect(screen, teal, [i[0], i[1], 20, 20])


# To put messages on the screen
def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1000/2 = 500 and 650/2 = 325
    text_box = txt.get_rect(center=(500, 360))  # changed coords
    screen.blit(txt, text_box)


# Function to run the main game loop
def game_loop():
    quit_game = False
    game_over = False

    # Snake will be 20 by 20 pixels
    snake_x = 480  # Centre point horizontally
    snake_y = 340  # Centre point vertically                           # changed coords

    snake_x_change = 0  # holds the value change of the x co ordinant
    snake_y_change = 0  # holds the value change of the y co ordinant
    snake_list = []
    snake_length = 1

    # Setting a random position for the food
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20  # changed coords

    # Load the high score
    high_score = load_high_score()

    while not quit_game:
        # give user the option to quit or play again when they die
        while game_over:
            save_high_score(high_score)
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
                instructions = "Exit: X to quit, space bar to resume, R toeset"
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

        if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:  # changed coords
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)  # Changes background to green

        # Create the snake body (rectangle)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_list)

        # Keeping track of the players score
        score = snake_length - 1  # Score excludes snake head
        player_score(score, red, high_score)

        # Get high score
        high_score = update_high_score(score, high_score)

        # Link the speed to the score, increasing difficulty
        if score > 3:
            speed = score
        else:
            speed = 3

        # Using a sprite (from - Create circle for the food) to represent food
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load('apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)

        pygame.display.update()

        # Collision detetection (test if snake touches food)
        # Print lines are for testing
        print(f"Snake X: {snake_x}")
        print(f"Food x: {food_x}")
        print(f"Snake y: {snake_y}")
        print(f"Food y: {food_y}")
        print("\n\n")

        # Collision detection (test if snake touches food)
        if snake_x == food_x and snake_y == food_y:
            # Set new random position if snake touches it
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 720 - 20) / 20) * 20  # changed coords
            # For testing purposes
            print("Got it!")

            # Increase the length of the snake (by original size)
            snake_length += 1

        clock.tick(speed)  # sets the speed which each iteration of the game
        # runs the in frames per second

    pygame.quit()
    quit()


# Main Routine
game_loop()
