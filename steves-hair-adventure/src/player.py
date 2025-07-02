import pygame
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLUE = (0, 0, 255)

def load_image(filename, size=None, fallback_color=None):
    """
    Load an image from the assets/images folder.
    If the image doesn't exist, create a colored rectangle as fallback.
    """
    # Get the path to the assets/images folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(os.path.dirname(current_dir), "assets", "images")
    image_path = os.path.join(assets_dir, filename)
    
    try:
        # Try to load the image
        image = pygame.image.load(image_path)
        if size:
            image = pygame.transform.scale(image, size)
        return image
    except (pygame.error, FileNotFoundError):
        # If image loading fails, create a colored rectangle
        if size and fallback_color:
            surface = pygame.Surface(size)
            surface.fill(fallback_color)
            return surface
        else:
            # Return None if we can't create a fallback
            return None

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.speed = 5
        self.jump_strength = -12
        self.gravity = 0.8
        
        # Try to load Steve's image, fallback to blue square
        self.image = load_image("steve.png", (30, 30), BLUE)
        if self.image is None:
            # Create fallback surface if load_image returns None
            self.image = pygame.Surface((30, 30))
            self.image.fill(BLUE)

    def update(self, platforms=None):
        # Handle input
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = self.jump_strength
            self.on_ground = False
            
        # Apply gravity
        self.vel_y += self.gravity
        
        # Update position
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Clamp to left edge only
        if self.rect.left < 0:
            self.rect.left = 0
            
        # Platform collision
        self.on_ground = False
        if platforms:
            for platform in platforms:
                if self.rect.colliderect(platform.rect) and self.vel_y >= 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                    
        # Ground collision (if no platform)
        if self.rect.bottom >= SCREEN_HEIGHT - 50:
            self.rect.bottom = SCREEN_HEIGHT - 50
            self.vel_y = 0
            self.on_ground = True
            
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            # Final fallback to drawing a rectangle
            pygame.draw.rect(screen, BLUE, self.rect)