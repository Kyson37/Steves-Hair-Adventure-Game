# How to Import Images for Sprites in Steve's Hair Adventure

## Current Implementation

The game now supports loading sprite images with automatic fallbacks to colored squares. Here's how it works:

### 1. Image Loading Function

Each sprite file (`sprites.py` and `player.py`) includes a `load_image()` function:

```python
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
            return None
```

### 2. Sprite Classes with Image Support

Each sprite class now loads its image in the `__init__` method:

```python
class Player:
    def __init__(self, x, y):
        # ... other initialization code ...
        
        # Try to load Steve's image, fallback to blue square
        self.image = load_image("steve.png", (30, 30), BLUE)
        if self.image is None:
            self.image = pygame.Surface((30, 30))
            self.image.fill(BLUE)
```

### 3. Drawing with Images

The `draw()` method uses `screen.blit()` instead of `pygame.draw.rect()`:

```python
def draw(self, screen):
    if self.image:
        screen.blit(self.image, self.rect)
    else:
        # Final fallback to drawing a rectangle
        pygame.draw.rect(screen, BLUE, self.rect)
```

## Required Image Files

Place these files in `assets/images/`:

- `steve.png` - Steve character (30x30 pixels) - Blue fallback
- `alcohol_bottle.png` - Alcohol bottles (20x20 pixels) - Red fallback  
- `rogain_bottle.png` - Rogain bottles (20x20 pixels) - Green fallback
- `goth_mommy.png` - Goth mommies (25x25 pixels) - Purple fallback

## Image Formats Supported

- PNG (recommended - supports transparency)
- JPG/JPEG
- GIF
- BMP

## Creating Your Own Sprites

### Option 1: Use the Placeholder Generator
Run the included script to create basic colored squares:
```bash
python create_placeholder_images.py
```

### Option 2: Create Custom Sprites
1. Use any image editor (Photoshop, GIMP, Paint.NET, etc.)
2. Create images at the required sizes
3. Save as PNG for best quality and transparency support
4. Place in `assets/images/` folder

### Option 3: Pixel Art Tools
- Aseprite (paid)
- Piskel (free online)
- GIMP (free)
- Paint.NET (free)

## Advanced Features

### Transparency
PNG files with transparency are fully supported. The transparent areas will show the background.

### Animation (Future Enhancement)
The current system loads static images, but can be extended to support sprite sheets and animation frames.

### Scaling
Images are automatically scaled to the required size. For best quality, create images at the target size or larger.

## Troubleshooting

### Image Not Loading
1. Check the filename matches exactly (case-sensitive)
2. Verify the image is in `assets/images/` folder
3. Check the image format is supported
4. Look for error messages in console

### Game Shows Colored Squares
This is normal if image files don't exist - the game falls back to colored rectangles and continues working.

### Performance Issues
- Keep image file sizes reasonable (under 1MB each)
- Use appropriate image dimensions
- Consider using indexed color PNG files for smaller sizes

## Example: Adding a New Sprite

1. Create the image file (e.g., `powerup.png`)
2. Place it in `assets/images/`
3. In your sprite class:

```python
class PowerUp:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.image = load_image("powerup.png", (15, 15), (255, 255, 0))  # Yellow fallback
        if self.image is None:
            self.image = pygame.Surface((15, 15))
            self.image.fill((255, 255, 0))
    
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, (255, 255, 0), self.rect)
```

The game will automatically use your custom sprite if the image file exists, or display a colored square if it doesn't!
