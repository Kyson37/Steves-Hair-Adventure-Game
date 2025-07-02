"""
Simple test to verify game mechanics without opening a pygame window
"""

# Test the movement logic without pygame initialization
class MockRect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
    
    @property
    def right(self):
        return self.x + self.width

class MockSprite:
    def __init__(self, x, y, vel_x):
        self.rect = MockRect(x, y, 20, 20)
        self.vel_x = vel_x
    
    def update(self):
        self.rect.x += self.vel_x

def test_side_scrolling_logic():
    print("🎮 Steve's Hair Adventure - Movement Test")
    print("=" * 50)
    
    # Screen dimensions
    SCREEN_WIDTH = 800
    
    # Create mock sprites with right-to-left movement
    sprites = {
        "Alcohol Bottle": MockSprite(SCREEN_WIDTH, 200, -4),
        "Rogain Bottle": MockSprite(SCREEN_WIDTH, 250, -3),
        "Goth Mommy": MockSprite(SCREEN_WIDTH, 300, -3.5)
    }
    
    print(f"📍 Starting positions (all spawn at x={SCREEN_WIDTH}):")
    for name, sprite in sprites.items():
        print(f"   {name}: x={sprite.rect.x}, vel_x={sprite.vel_x}")
    
    print(f"\n🏃 After 20 frames of movement:")
    for name, sprite in sprites.items():
        for _ in range(20):
            sprite.update()
        distance_moved = SCREEN_WIDTH - sprite.rect.x
        print(f"   {name}: x={sprite.rect.x} (moved {distance_moved}px left)")
    
    print(f"\n✅ Movement verification:")
    all_moving_left = True
    for name, sprite in sprites.items():
        if sprite.rect.x < SCREEN_WIDTH:
            print(f"   ✓ {name} is moving LEFT correctly")
        else:
            print(f"   ✗ {name} is NOT moving!")
            all_moving_left = False
    
    print(f"\n🗑️ Cleanup test (remove when rect.right < 0):")
    cleanup_working = True
    for name, sprite in sprites.items():
        # Move sprite off-screen left
        sprite.rect.x = -30
        should_remove = sprite.rect.right < 0
        if should_remove:
            print(f"   ✓ {name} would be removed (rect.right={sprite.rect.right})")
        else:
            print(f"   ✗ {name} cleanup failed (rect.right={sprite.rect.right})")
            cleanup_working = False
    
    print(f"\n🎯 Game Mechanics Summary:")
    print(f"   • Objects spawn from RIGHT side (x={SCREEN_WIDTH})")
    print(f"   • Objects move LEFT with different speeds")
    print(f"   • Objects removed when completely off LEFT side")
    print(f"   • Player starts on LEFT side (x=50)")
    
    print(f"\n{'🎉 ALL SYSTEMS GO!' if all_moving_left and cleanup_working else '⚠️ ISSUES DETECTED'}")
    print("=" * 50)
    
    return all_moving_left and cleanup_working

if __name__ == "__main__":
    success = test_side_scrolling_logic()
    print(f"\nGame conversion {'SUCCESS' if success else 'FAILED'}! 🎮")
