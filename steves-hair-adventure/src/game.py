import pygame
import random
import sys
from player import Player
from sprites import AlcoholBottle, RogainBottle, GothMommy

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)

class Platform:
    def __init__(self, x, y, width=100, height=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (100, 100, 100)
        
    def draw(self, screen, offset=(0, 0)):
        ox, oy = offset
        pygame.draw.rect(screen, self.color, self.rect.move(-ox, -oy))

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game state
        self.alcoholism = 0  # 0-100, game over at 100
        self.hair_growth = 0  # 0-100, win condition at 100
        self.score = 0
        
        # Game objects
        self.player = Player(50, SCREEN_HEIGHT - 100)  # Start player on left side
        self.alcohol_bottles = []
        self.rogain_bottles = []
        self.goth_mommies = []
        self.platforms = []
        
        # Spawn timers
        self.alcohol_spawn_timer = 0
        self.rogain_spawn_timer = 0
        self.goth_spawn_timer = 0
        self.platform_spawn_x = 0
        
        # Platform generation parameters
        self.platform_min_gap = 120
        self.platform_max_gap = 220
        self.platform_min_y = SCREEN_HEIGHT - 200
        self.platform_max_y = SCREEN_HEIGHT - 70
        
        # Font for UI
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self._init_platforms()
        
    def _init_platforms(self):
        # Start with a ground platform
        self.platforms.append(Platform(0, SCREEN_HEIGHT - 50, 1000, 50))
        self.platform_spawn_x = 1000
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_r and (self.alcoholism >= 100 or self.hair_growth >= 100):
                    self.restart_game()
    
    def restart_game(self):
        self.alcoholism = 0
        self.hair_growth = 0
        self.score = 0
        self.player = Player(50, SCREEN_HEIGHT - 100)  # Restart on left side
        self.alcohol_bottles.clear()
        self.rogain_bottles.clear()
        self.goth_mommies.clear()
        self.platforms.clear()
        self._init_platforms()
        
    def spawn_objects(self, cam_x):
        # Define reachable vertical range for player
        min_y = SCREEN_HEIGHT - 50 - 30  # 30px above ground (player height)
        max_y = SCREEN_HEIGHT - 50 - 5   # 5px above ground
        spawn_x = cam_x + SCREEN_WIDTH + 40  # Always spawn just off right edge of camera
        
        # Limit number of each object on screen to prevent over-spawning
        max_alcohol = 5
        max_rogain = 3
        max_goth = 2
        
        # Spawn alcohol bottles from right side
        self.alcohol_spawn_timer += 1
        if self.alcohol_spawn_timer > 90 and len(self.alcohol_bottles) < max_alcohol:
            y = random.randint(min_y, max_y)
            self.alcohol_bottles.append(AlcoholBottle(spawn_x, y))
            self.alcohol_spawn_timer = 0
            
        # Spawn rogain bottles (less frequent) from right side
        self.rogain_spawn_timer += 1
        if self.rogain_spawn_timer > 180 and len(self.rogain_bottles) < max_rogain:
            y = random.randint(min_y, max_y)
            self.rogain_bottles.append(RogainBottle(spawn_x, y))
            self.rogain_spawn_timer = 0
            
        # Spawn goth mommies (moderately frequent) from right side
        self.goth_spawn_timer += 1
        if self.goth_spawn_timer > 120 and len(self.goth_mommies) < max_goth:
            y = random.randint(min_y, max_y)
            self.goth_mommies.append(GothMommy(spawn_x, y))
            self.goth_spawn_timer = 0
    
    def spawn_platforms(self, player_x):
        # Generate platforms ahead of the player
        while self.platform_spawn_x < player_x + 800:
            width = random.randint(80, 160)
            gap = random.randint(self.platform_min_gap, self.platform_max_gap)
            y = random.randint(self.platform_min_y, self.platform_max_y)
            self.platforms.append(Platform(self.platform_spawn_x + gap, y, width, 20))
            self.platform_spawn_x += gap + width
    
    def update_objects(self):
        # Update player
        self.player.update()
        
        # Update and remove off-screen alcohol bottles (left side)
        for bottle in self.alcohol_bottles[:]:
            bottle.update()
            if bottle.rect.right < 0:  # Remove when completely off left side
                self.alcohol_bottles.remove(bottle)
                
        # Update and remove off-screen rogain bottles (left side)
        for bottle in self.rogain_bottles[:]:
            bottle.update()
            if bottle.rect.right < 0:  # Remove when completely off left side
                self.rogain_bottles.remove(bottle)
                
        # Update and remove off-screen goth mommies (left side)
        for mommy in self.goth_mommies[:]:
            mommy.update()
            if mommy.rect.right < 0:  # Remove when completely off left side
                self.goth_mommies.remove(mommy)
        
        # Remove platforms that are far left of the player
        player_x = self.player.rect.x
        self.platforms = [p for p in self.platforms if p.rect.right > player_x - 800]
    
    def check_collisions(self):
        # Check alcohol bottle collisions
        for bottle in self.alcohol_bottles[:]:
            if self.player.rect.colliderect(bottle.rect):
                self.alcohol_bottles.remove(bottle)
                self.alcoholism += 15
                if self.alcoholism > 100:
                    self.alcoholism = 100
                    
        # Check rogain bottle collisions
        for bottle in self.rogain_bottles[:]:
            if self.player.rect.colliderect(bottle.rect):
                self.rogain_bottles.remove(bottle)
                self.hair_growth += 20
                self.score += 10
                if self.hair_growth > 100:
                    self.hair_growth = 100
                    
        # Check goth mommy collisions
        for mommy in self.goth_mommies[:]:
            if self.player.rect.colliderect(mommy.rect):
                self.goth_mommies.remove(mommy)
                # 50% chance for each effect
                if random.random() < 0.5:
                    # Increase alcoholism, decrease hair growth
                    self.alcoholism += 10
                    self.hair_growth -= 5
                else:
                    # Decrease alcoholism, increase hair growth
                    self.alcoholism -= 5
                    self.hair_growth += 10
                
                # Keep values in bounds
                self.alcoholism = max(0, min(100, self.alcoholism))
                self.hair_growth = max(0, min(100, self.hair_growth))
                self.score += 5
    
    def draw_ui(self):
        # Draw alcoholism bar
        pygame.draw.rect(self.screen, RED, (10, 10, 200, 20))
        pygame.draw.rect(self.screen, WHITE, (10, 10, int(200 * (self.alcoholism / 100)), 20))
        alcohol_text = self.small_font.render(f"Alcoholism: {int(self.alcoholism)}%", True, WHITE)
        self.screen.blit(alcohol_text, (10, 35))
        
        # Draw hair growth bar
        pygame.draw.rect(self.screen, BROWN, (10, 60, 200, 20))
        pygame.draw.rect(self.screen, GREEN, (10, 60, int(200 * (self.hair_growth / 100)), 20))
        hair_text = self.small_font.render(f"Hair Growth: {int(self.hair_growth)}%", True, WHITE)
        self.screen.blit(hair_text, (10, 85))
        
        # Draw score
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 110))
        
        # Draw instructions
        instructions = [
            "Use WASD or Arrow Keys to move",
            "SPACE to jump",
            "Avoid red alcohol bottles!",
            "Collect green rogain bottles!",
            "Purple goth mommies: 50/50 chance!",
            "Objects move right to left!"
        ]
        
        for i, instruction in enumerate(instructions):
            text = self.small_font.render(instruction, True, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH - 250, 10 + i * 25))
    
    def draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        if self.alcoholism >= 100:
            game_over_text = self.font.render("GAME OVER - Too Much Alcohol!", True, RED)
        else:
            game_over_text = self.font.render("YOU WIN - Full Head of Hair!", True, GREEN)
            
        restart_text = self.font.render("Press R to Restart or ESC to Quit", True, WHITE)
        
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(restart_text, restart_rect)
    
    def draw(self, camera_offset=(0, 0)):
        offset_x, offset_y = camera_offset
        self.screen.fill(BLACK)
        
        # Draw ground
        pygame.draw.rect(self.screen, GRAY, (0 - offset_x, SCREEN_HEIGHT - 50 - offset_y, SCREEN_WIDTH, 50))
        
        # Draw platforms
        for platform in self.platforms:
            platform.draw(self.screen, offset=(offset_x, offset_y))
        
        # Draw game objects with offset
        player_rect = self.player.rect.move(-offset_x, -offset_y)
        if hasattr(self.player, 'image') and self.player.image:
            self.screen.blit(self.player.image, player_rect)
        else:
            pygame.draw.rect(self.screen, BLUE, player_rect)
            
        for bottle in self.alcohol_bottles:
            bottle_rect = bottle.rect.move(-offset_x, -offset_y)
            if hasattr(bottle, 'image') and bottle.image:
                self.screen.blit(bottle.image, bottle_rect)
            else:
                pygame.draw.rect(self.screen, RED, bottle_rect)
                
        for bottle in self.rogain_bottles:
            bottle_rect = bottle.rect.move(-offset_x, -offset_y)
            if hasattr(bottle, 'image') and bottle.image:
                self.screen.blit(bottle.image, bottle_rect)
            else:
                pygame.draw.rect(self.screen, GREEN, bottle_rect)
                
        for mommy in self.goth_mommies:
            mommy_rect = mommy.rect.move(-offset_x, -offset_y)
            if hasattr(mommy, 'image') and mommy.image:
                self.screen.blit(mommy.image, mommy_rect)
            else:
                pygame.draw.rect(self.screen, PURPLE, mommy_rect)
        
        # Draw UI
        self.draw_ui()
        
        # Draw game over screen if needed
        if self.alcoholism >= 100 or self.hair_growth >= 100:
            self.draw_game_over()
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            
            # Only update game if not game over
            if self.alcoholism < 100 and self.hair_growth < 100:
                self.spawn_objects()
                self.update_objects()
                self.check_collisions()
                # Infinite world: spawn platforms ahead of player
                self.spawn_platforms(self.player.rect.x)
            
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()