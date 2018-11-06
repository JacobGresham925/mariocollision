import pygame
from pygame.sprite import Sprite

class Background(Sprite):

    def __init__(self, screen):
        """Initialize the mario, and set its starting position."""
        super(Background, self).__init__()
        self.screen = screen

        # Load the mario image, and get its rect.
        self.image = pygame.image.load('images/world.png')
        self.image = pygame.transform.scale(self.image, (6784, 920))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new mario at the bottom center of the screen.
        self.rect.topleft = self.screen_rect.topleft

        # Store a decimal value for the mario's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def reset_background(self):
        """Center the mario on the screen."""
        self.rect.topleft = self.screen_rect.topleft

    def update(self):
        """Update the mario's position, based on movement flags."""
        # Update the mario's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 2
        if self.moving_left and self.rect.left > 0:
            self.center -= 2

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the mario at its current location."""
        self.screen.blit(self.image, self.rect)
