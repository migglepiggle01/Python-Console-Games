import os
import time
import random
import sys
import msvcrt  # For non-blocking keyboard input in Windows

# Game constants
WIDTH = 40
HEIGHT = 20
PADDLE_HEIGHT = 4
BALL = "O"
PADDLE = "|"

# Initial positions
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 1  # Ball direction in X (1 means right, -1 means left)
ball_dy = 1  # Ball direction in Y (1 means down, -1 means up)
player_y = HEIGHT // 2 - PADDLE_HEIGHT // 2  # Player paddle initial position
ai_y = HEIGHT // 2 - PADDLE_HEIGHT // 2  # AI paddle initial position

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to draw the game state
def draw_game():
    global ball_x, ball_y, player_y, ai_y

    clear_screen()
    # Draw top border
    print("+" + "-" * (WIDTH - 2) + "+")
    
    # Draw game area
    for y in range(HEIGHT):
        if y == ball_y:
            print("".join([' ' * ball_x + BALL + ' ' * (WIDTH - ball_x - 1)]))
        else:
            if y >= player_y and y < player_y + PADDLE_HEIGHT:
                # Draw player paddle
                print(f"{PADDLE}{' ' * (WIDTH - 2)}")
            elif y >= ai_y and y < ai_y + PADDLE_HEIGHT:
                # Draw AI paddle
                print(f"{' ' * (WIDTH - 2)}{PADDLE}")
            else:
                print(" " * WIDTH)
    
    # Draw bottom border
    print("+" + "-" * (WIDTH - 2) + "+")

# Function to read key presses (non-blocking)
def get_input():
    if msvcrt.kbhit():
        return msvcrt.getch().decode("utf-8")
    return None

# Main game loop
while True:
    # Draw the current game state
    draw_game()

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= HEIGHT - 1:
        ball_dy = -ball_dy

    # Ball collision with player paddle
    if ball_x == 1 and player_y <= ball_y < player_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball collision with AI paddle
    if ball_x == WIDTH - 2 and ai_y <= ball_y < ai_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball goes out of bounds (left or right)
    if ball_x <= 0 or ball_x >= WIDTH - 1:
        print("Game Over!")
        break

    # Move AI paddle
    if ai_y + PADDLE_HEIGHT // 2 < ball_y:
        ai_y += 1
    elif ai_y + PADDLE_HEIGHT // 2 > ball_y:
        ai_y -= 1

    # Get player input to move the paddle
    input_char = get_input()
    if input_char == 'w' and player_y > 0:
        player_y -= 1  # Move paddle up
    elif input_char == 's' and player_y + PADDLE_HEIGHT < HEIGHT:
        player_y += 1  # Move paddle down

    # Control the game speed
    time.sleep(0.05)
