# Steve's Hair Adventure Game

## Overview
Steve's Hair Adventure is a platform game developed using Pygame where players control Steve, a character on a quest to dodge alcohol bottles and collect Rogain bottles to regrow his hair. The game features various challenges, including encounters with Goth mommies that can affect Steve's alcoholism and hair growth.

## Game Mechanics
- **Player Character**: Steve is represented as a square for now. Players control his movement to avoid obstacles and collect items.
- **Side-Scrolling Action**: Objects move from right to left across the screen, creating a side-scrolling runner experience.
- **Obstacles**: Players must dodge alcohol bottles that move from right to left and increase Steve's alcoholism if hit.
- **Collectibles**: Rogain bottles move from right to left and help Steve regrow his hair when collected.
- **Goth Mommies**: Encountering Goth mommies introduces randomness, with a 50% chance to either increase alcoholism and decrease hair growth or vice versa.

## Project Structure
```
steves-hair-adventure
├── src
│   ├── main.py        # Entry point of the game
│   ├── game.py        # Main game logic and state management
│   ├── player.py      # Player class for Steve
│   ├── sprites.py     # Sprite classes for game objects
│   ├── levels.py      # Level management
│   └── utils.py       # Utility functions
├── assets
│   ├── sounds         # Directory for sound files
│   └── images         # Directory for image files
├── requirements.txt    # Dependencies for the project
└── README.md           # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/steves-hair-adventure.git
   ```
2. Navigate to the project directory:
   ```
   cd steves-hair-adventure
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the game:
   ```
   python src/main.py
   ```

## Gameplay Details
- Use the arrow keys or WASD to move Steve around the screen.
- Use SPACE or UP arrow to jump.
- Steve starts on the left side of the screen.
- Avoid alcohol bottles moving from right to left to prevent increasing alcoholism.
- Collect Rogain bottles moving from right to left to help with hair growth.
- Watch out for Goth mommies moving from right to left and their unpredictable effects on Steve's journey.

## Future Improvements
- Replace placeholder squares with actual character and object sprites.
- Add sound effects and background music.
- Implement additional levels and challenges.

Enjoy playing Steve's Hair Adventure!