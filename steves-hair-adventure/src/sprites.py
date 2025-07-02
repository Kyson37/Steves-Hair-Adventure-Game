import pygame
import os

# Colors (fallback colors if images don't load)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)

def load_image(filename, size=None, fallback_color=None):
    """
    Load an image from the assets/images folder.
    If the image doesn't exist, create a colored rectangle as fallback.
    
    Args:
        filename: Name of the image file (e.g., "steve.png")
        size: Tuple (width, height) for the image size
        fallback_color: Color tuple for fallback rectangle
    
    Returns:
        pygame.Surface object
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

class AlcoholBottle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)  # Increased size
        self.vel_x = -4  # Move left across screen
        
        # Try to load image, fallback to red square
        self.image = load_image("alcohol_bottle.png", (32, 32), RED)
        if self.image is None:
            # Create fallback surface if load_image returns None
            self.image = pygame.Surface((32, 32))
            self.image.fill(RED)
        
    def update(self):
        self.rect.x += self.vel_x
        
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            # Final fallback to drawing a rectangle
            pygame.draw.rect(screen, RED, self.rect)

class RogainBottle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)  # Increased size by 50%
        self.vel_x = -3  # Move left across screen (slightly slower)
        
        # Try to load image, fallback to green square
        self.image = load_image("rogain_bottle.png", (30, 30), GREEN)
        if self.image is None:
            # Create fallback surface if load_image returns None
            self.image = pygame.Surface((30, 30))
            self.image.fill(GREEN)
        
    def update(self):
        self.rect.x += self.vel_x
        
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            # Final fallback to drawing a rectangle
            pygame.draw.rect(screen, GREEN, self.rect)

class GothMommy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.vel_x = -3.5  # Move left across screen
        
        # Try to load image, fallback to purple square
        self.image = load_image("goth_mommy.png", (25, 25), PURPLE)
        if self.image is None:
            # Create fallback surface if load_image returns None
            self.image = pygame.Surface((25, 25))
            self.image.fill(PURPLE)
        
    def update(self):
        self.rect.x += self.vel_x
        
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            # Final fallback to drawing a rectangle
            pygame.draw.rect(screen, PURPLE, self.rect)