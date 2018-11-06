import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    """A class to represent a single enemy"""

    def __init__(self, screen):
        """Initialize the enemy, and set its starting position."""
        super(Block, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # Load the enemy image, and set its rect attribute.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new enemy near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the enemy's exact position.
        self.x = float(self.rect.x)
        self.rect.centerx = self.screen_rect.left + 100
        self.rect.bottom = self.screen_rect.bottom - 100

    def blitme(self):
        """Draw the enemy at its current location."""
        self.screen.blit(self.image, self.rect)
