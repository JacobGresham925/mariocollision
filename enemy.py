import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """A class to represent a single enemy"""

    def __init__(self, screen):
        """Initialize the enemy, and set its starting position."""
        super(Enemy, self).__init__()
        self.screen = screen

        # Load the enemy image, and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new enemy near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the enemy's exact position.
        self.x = float(self.rect.x)
        
    def move(self):
        """Return True if enemy is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move the enemy right or left."""
        self.x -= 2
        self.rect.x = self.x

    def blitme(self):
        """Draw the enemy at its current location."""
        self.screen.blit(self.image, self.rect)
