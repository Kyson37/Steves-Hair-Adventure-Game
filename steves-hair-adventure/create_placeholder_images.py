"""
Simple script to create basic colored square images for testing Steve's Hair Adventure.
Run this script to generate placeholder images if you don't have sprite graphics yet.
"""

import pygame
import os

# Initialize pygame
pygame.init()

# Colors for each sprite
COLORS = {
    'steve.png': (0, 100, 255),        # Blue for Steve
    'alcohol_bottle.png': (200, 0, 0),  # Dark red for alcohol
    'rogain_bottle.png': (0, 200, 0),   # Green for rogain
    'goth_mommy.png': (150, 0, 150)     # Purple for goth mommy
}

# Sizes for each sprite
SIZES = {
    'steve.png': (30, 30),
    'alcohol_bottle.png': (20, 20),
    'rogain_bottle.png': (20, 20),
    'goth_mommy.png': (25, 25)
}

def create_placeholder_images():
    """Create simple colored square images for testing."""
    
    # Get the assets/images directory path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(os.path.dirname(current_dir), "assets", "images")
    
    print(f"Creating placeholder images in: {assets_dir}")
    
    # Create each placeholder image
    for filename, color in COLORS.items():
        size = SIZES[filename]
        
        # Create a surface
        surface = pygame.Surface(size)
        surface.fill(color)
        
        # Add a simple border for visual distinction
        pygame.draw.rect(surface, (255, 255, 255), surface.get_rect(), 1)
        
        # Save the image
        filepath = os.path.join(assets_dir, filename)
        pygame.image.save(surface, filepath)
        print(f"Created: {filename} ({size[0]}x{size[1]})")
    
    print("\nPlaceholder images created successfully!")
    print("You can now replace these with your own sprite artwork.")

if __name__ == "__main__":
    create_placeholder_images()
    pygame.quit()
