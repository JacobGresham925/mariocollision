import pygame
from pygame.sprite import Sprite

class Mario(Sprite):

    def __init__(self, screen, small_regular_mario_images):
        """Initialize the mario, and set its starting position."""
        super(Mario, self).__init__()
        self.screen = screen
        self.mario_images = small_regular_mario_images

        # Load the mario image, and get its rect.
        self.image = pygame.transform.scale(self.mario_images[0], (36, 34))
        self.rect2 = pygame.Rect(0, 0, 36, 36)
        self.rect3 = pygame.Rect(0, 0, 6, 34)

        self.rect = self.image.get_rect()
        self.rect2.center = self.rect.center
        self.screen_rect = screen.get_rect()

        # Start each new mario at the bottom left of the screen.
        self.rect.centerx = self.screen_rect.left + 20
        self.rect.bottom = self.screen_rect.bottom - 48
        self.rect2.center = self.rect.center
        self.rect3.center = self.rect.center
        self.onblock = False

        
        # Store a decimal value for the mario's center.
        self.center = float(self.rect.centerx)
        
        # Movement flags.
        self.moving_right = False
        self.moving_left = False

        self.on_the_ground = True
        # can be changed to bool to save space and time
        self.last_direction = "right"

        self.gravity = 0.2
        self.y_veloctiy = 0
        self.x_velocity = 3
        self.frame = 0
        
    def center_mario(self):
        """Center the mario on the screen."""
        self.centerx = self.screen_rect.centerx
        self.centery = self.rect.centery
        
    def update(self):
        """Update the mario's position, based on movement flags and if he's jumping."""
        self.y_veloctiy += self.gravity

        if self.rect.bottom > self.screen_rect.bottom - 48:
            self.rect.centery = self.screen_rect.bottom - 65
            self.y_veloctiy = 0
            self.on_the_ground = True

        # Update mario's center value, not the rect.
        if not self.on_the_ground:
            if self.moving_left:
                self.x_velocity = -2
            else:
                self.x_velocity = 2
            self.rect.centery += self.y_veloctiy
        elif self.on_the_ground:
            if self.moving_left:
                self.x_velocity = -3
            else:
                self.x_velocity = 3
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.x_velocity
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx += self.x_velocity
        self.rect2.center = self.rect.center
        self.rect2.centery += 4
        self.rect3.center = self.rect.center
        self.rect3.centery -= 4
            
        # Update rect object from self.center.
        # self.rect.centerx = self.centerx
        # self.rect.centery = self.centery

    def blitme(self):
        """Draw the mario at its current location."""
        if not self.on_the_ground:
            if self.last_direction == "right":
                self.image = self.mario_images[5]
            elif self.last_direction == "left":
                self.image = pygame.transform.flip(self.mario_images[5], True, False)
            self.image = pygame.transform.scale(self.image, (36, 34))

        elif self.on_the_ground:
            if self.moving_right:
                self.frame += 1
                if self.frame == 15:
                    self.frame = 0
                self.image = self.mario_images[int(self.frame / 5) + 1]
            elif self.moving_left:
                self.frame += 1
                if self.frame == 15:
                    self.frame = 0
                self.image = pygame.transform.flip(self.mario_images[int(self.frame / 5) + 1], True, False)
            elif self.last_direction == "right":
                self.image = self.mario_images[0]
            elif self.last_direction == "left":
                self.image = pygame.transform.flip(self.mario_images[0], True, False)
            self.image = pygame.transform.scale(self.image, (36, 34))
        self.screen.blit(self.image, self.rect)
