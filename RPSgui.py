# Import the pygame module
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_r,
    K_p,
    K_s
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#moves
oppMove = 'R'
moveOptions = ["R", "P", "S"]
playerMove = 'R'

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_r]:
            self.surf = pygame.image.load("Rock.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            playerMove = 'R'
        if pressed_keys[K_p]:
            self.surf = pygame.image.load("Paper.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            playerMove = 'P'
        if pressed_keys[K_s]:
            self.surf = pygame.image.load("Scissors.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            playerMove = 'S'

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            oppMove = random.choice(moveOptions)
            if(oppMove == 'R'):
                self.surf = pygame.image.load("Rock.png").convert()
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            elif(oppMove == 'P'):
                self.surf = pygame.image.load("Paper.png").convert()
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            else:
                self.surf = pygame.image.load("Scissors.png").convert()
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Instantiate enemy. Right now, this is just a rectangle.
Enemy = Enemy()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    Enemy.update(pressed_keys)

    # Draw the player on the screen
    screen.blit(player.surf, (350, 400))

    # Draw the enemy on the screen
    screen.blit(Enemy.surf, (350, 50))

    # Update the display
    pygame.display.flip()