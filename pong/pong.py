import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Load images
background_img = pygame.image.load("background.jpg")
ball_img = pygame.image.load("ball.png")
bar_img = pygame.image.load("bar.png")

# Set the background image
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5

# Ball dimensions
BALL_SIZE = 20
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Paddle A
paddle_a_x = 50
paddle_a_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Paddle B
paddle_b_x = WIDTH - 50 - PADDLE_WIDTH
paddle_b_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Ball
ball_x = WIDTH // 2 - BALL_SIZE // 2
ball_y = HEIGHT // 2 - BALL_SIZE // 2
ball_dx = random.choice([-1, 1]) * BALL_SPEED_X
ball_dy = random.choice([-1, 1]) * BALL_SPEED_Y

# Score
score_a = 0
score_b = 0

# Update the game state
def update():
    global paddle_a_y, paddle_b_y, ball_x, ball_y, ball_dx, ball_dy, score_a, score_b

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a_y > 0:
        paddle_a_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a_y < HEIGHT - PADDLE_HEIGHT:
        paddle_a_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b_y > 0:
        paddle_b_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b_y < HEIGHT - PADDLE_HEIGHT:
        paddle_b_y += PADDLE_SPEED

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check collision with paddles
    if (
        ball_x <= paddle_a_x + PADDLE_WIDTH
        and paddle_a_y <= ball_y + BALL_SIZE <= paddle_a_y + PADDLE_HEIGHT
    ):
        ball_dx = BALL_SPEED_X
    elif (
        ball_x + BALL_SIZE >= paddle_b_x
        and paddle_b_y <= ball_y + BALL_SIZE <= paddle_b_y + PADDLE_HEIGHT
    ):
        ball_dx = -BALL_SPEED_X

    # Check collision with walls
    if ball_y <= 0 or ball_y + BALL_SIZE >= HEIGHT:
        ball_dy *= -1

    # Check if ball is out of bounds
    if ball_x <= 0:
        score_b += 1
        reset_ball()
    elif ball_x + BALL_SIZE >= WIDTH:
        score_a += 1
        reset_ball()

# Reset the ball position
def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = WIDTH // 2 - BALL_SIZE // 2
    ball_y = HEIGHT // 2 - BALL_SIZE // 2
    ball_dx = random.choice([-1, 1]) * BALL_SPEED_X
    ball_dy = random.choice([-1, 1]) * BALL_SPEED_Y

# Draw the game elements
def draw():
    WIN.blit(background, (0, 0))  # Draw the background image
    WIN.blit(ball_img, (ball_x, ball_y))
    WIN.blit(bar_img, (paddle_a_x, paddle_a_y))
    WIN.blit(bar_img, (paddle_b_x, paddle_b_y))

    # Render the scores
    font = pygame.font.Font(None, 36)
    text_a = font.render(str(score_a), True, (255, 255, 255))
    text_b = font.render(str(score_b), True, (255, 255, 255))
    WIN.blit(text_a, (WIDTH // 2 - 50, 10))
    WIN.blit(text_b, (WIDTH // 2 + 30, 10))

    pygame.display.update()

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # Set the frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()
    draw()

# Quit the game
pygame.quit()
