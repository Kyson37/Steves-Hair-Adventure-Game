# Game Movement Changes: Right-to-Left Side-Scrolling

## Summary of Changes Made

Steve's Hair Adventure has been converted from a falling-objects platformer to a side-scrolling runner game where objects move from right to left across the screen.

## Key Changes:

### 1. Sprite Movement (sprites.py)
**Before:** Objects fell downward using `vel_y`
**After:** Objects move left using `vel_x`

- **AlcoholBottle**: `vel_x = -4` (moves left at 4 pixels/frame)
- **RogainBottle**: `vel_x = -3` (moves left at 3 pixels/frame) 
- **GothMommy**: `vel_x = -3.5` (moves left at 3.5 pixels/frame)

All `update()` methods changed from `self.rect.y += self.vel_y` to `self.rect.x += self.vel_x`

### 2. Object Spawning (game.py)
**Before:** Objects spawned at top of screen (`y = -20`) with random X positions
**After:** Objects spawn at right edge (`x = SCREEN_WIDTH`) with random Y positions

- Spawn position: `(SCREEN_WIDTH, random_y)` instead of `(random_x, -20)`
- Y positions: `random.randint(100, SCREEN_HEIGHT - 100)` (above ground, below UI)

### 3. Object Cleanup (game.py)
**Before:** Remove objects when `bottle.rect.y > SCREEN_HEIGHT` (off bottom)
**After:** Remove objects when `bottle.rect.right < 0` (completely off left side)

### 4. Player Positioning (game.py)
**Before:** Player started in center: `Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)`
**After:** Player starts on left: `Player(50, SCREEN_HEIGHT - 100)`

This applies to both initial spawn and game restart.

### 5. UI Instructions Updated
Added instruction: "Objects move right to left!" to help players understand the new mechanics.

### 6. Documentation Updates (README.md)
- Updated game mechanics description
- Added side-scrolling explanation
- Updated gameplay details with new movement pattern

## Game Feel Changes:

### Advantages of Right-to-Left Movement:
1. **Runner Game Feel** - More like classic side-scrolling games
2. **Predictable Timing** - Objects appear from right, giving players time to react
3. **Better Positioning** - Player on left can see incoming objects
4. **Varied Heights** - Objects can appear at different vertical levels
5. **More Strategic** - Players can position vertically to avoid clusters

### Different Object Speeds:
- Alcohol bottles: Fastest (-4 px/frame) - Most dangerous
- Goth mommies: Medium (-3.5 px/frame) - Moderate threat
- Rogain bottles: Slowest (-3 px/frame) - Easier to collect

## Technical Implementation:

### Movement System:
```python
# Old (falling):
def update(self):
    self.rect.y += self.vel_y

# New (side-scrolling):
def update(self):
    self.rect.x += self.vel_x
```

### Spawn System:
```python
# Old (top spawn):
AlcoholBottle(random_x, -20)

# New (right spawn):
AlcoholBottle(SCREEN_WIDTH, random_y)
```

### Cleanup System:
```python
# Old (bottom cleanup):
if bottle.rect.y > SCREEN_HEIGHT:
    self.alcohol_bottles.remove(bottle)

# New (left cleanup):
if bottle.rect.right < 0:
    self.alcohol_bottles.remove(bottle)
```

## How to Test:
1. Run the game: `python src\main.py`
2. Steve should start on the left side
3. Objects should appear from the right and move left
4. Use WASD/Arrow keys to move Steve up/down/left/right
5. Use SPACE to jump
6. Objects should disappear when they reach the left edge

The game now feels more like a classic side-scrolling runner where the player must react to incoming threats and opportunities from the right side of the screen!
