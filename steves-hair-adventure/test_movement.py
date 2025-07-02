"""
Quick verification script to test the right-to-left movement logic
without opening the full game window.
"""

import sys
import os

# Add src directory to path to import game modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the sprite classes
from sprites import AlcoholBottle, RogainBottle, GothMommy

def test_movement_logic():
    """Test that sprites move correctly from right to left"""
    
    print("Testing Steve's Hair Adventure - Right-to-Left Movement")
    print("=" * 55)
    
    # Create test sprites starting from the right side of a 800px wide screen
    SCREEN_WIDTH = 800
    start_x = SCREEN_WIDTH
    test_y = 300
    
    # Create sprites
    alcohol = AlcoholBottle(start_x, test_y)
    rogain = RogainBottle(start_x, test_y)
    goth = GothMommy(start_x, test_y)
    
    sprites = [
        ("Alcohol Bottle", alcohol),
        ("Rogain Bottle", rogain),
        ("Goth Mommy", goth)
    ]
    
    print(f"Initial positions (starting from right edge at x={start_x}):")
    for name, sprite in sprites:
        print(f"  {name}: x={sprite.rect.x}, vel_x={sprite.vel_x}")
    
    print("\nAfter 10 update frames:")
    for name, sprite in sprites:
        # Simulate 10 frames of movement
        for _ in range(10):
            sprite.update()
        print(f"  {name}: x={sprite.rect.x} (moved {start_x - sprite.rect.x} pixels left)")
    
    print("\nMovement verification:")
    for name, sprite in sprites:
        if sprite.rect.x < start_x:
            print(f"  ✓ {name} is moving LEFT correctly")
        else:
            print(f"  ✗ {name} is NOT moving left!")
    
    # Test cleanup condition
    print(f"\nCleanup test (objects removed when rect.right < 0):")
    for name, sprite in sprites:
        # Move sprite far left
        sprite.rect.x = -50
        if sprite.rect.right < 0:
            print(f"  ✓ {name} would be removed correctly (rect.right = {sprite.rect.right})")
        else:
            print(f"  ✗ {name} cleanup condition failed!")
    
    print("\n" + "=" * 55)
    print("Movement system verification complete!")
    print("The game should now work as a right-to-left side-scroller.")

if __name__ == "__main__":
    test_movement_logic()
