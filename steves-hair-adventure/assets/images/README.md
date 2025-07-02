# Image Assets for Steve's Hair Adventure

Place your sprite images in this folder. The game will automatically load them if they exist, otherwise it will use colored squares as fallbacks.

## Required Image Files:
- `steve.png` - Steve character sprite (30x30 pixels)
- `alcohol_bottle.png` - Alcohol bottle sprite (20x20 pixels)
- `rogain_bottle.png` - Rogain bottle sprite (20x20 pixels)
- `goth_mommy.png` - Goth mommy sprite (25x25 pixels)

## Supported Formats:
- PNG (recommended for transparency)
- JPG/JPEG
- GIF
- BMP

## Tips:
- Use PNG format for sprites with transparency
- Keep file sizes reasonable for better performance
- The game will automatically scale images to the required size
- If an image fails to load, the game will display a colored square instead

## Creating Simple Test Images:
You can create simple test images using any image editor, or even use online tools to create basic pixel art sprites.

## How the Image Loading Works:
The game uses a `load_image()` function that:
1. Looks for the image file in this directory
2. Loads and scales it to the required size
3. If loading fails, creates a colored fallback surface
4. Uses pygame's `screen.blit()` to draw the image instead of `pygame.draw.rect()`
