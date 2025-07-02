import pygame
from game import Game

def main():
    pygame.init()
    # Window size (no zoom)
    DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600
    GAME_WIDTH, GAME_HEIGHT = DISPLAY_WIDTH, DISPLAY_HEIGHT

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Steve's Hair Adventure")
    game = Game(screen)

    running = True
    clock = pygame.time.Clock()
    while running:
        # --- Game logic ---
        game.handle_events()
        if game.alcoholism < 100 and game.hair_growth < 100:
            # --- Camera logic: follow player only on x-axis, clamp so player is always visible ---
            player_rect = game.player.rect
            cam_x = max(0, player_rect.centerx - GAME_WIDTH // 2)
            cam_y = 0  # Fixed vertical camera
            game.spawn_objects(cam_x)
            # Pass platforms to player update
            game.player.update(platforms=game.platforms)
            game.update_objects()
            game.check_collisions()
        else:
            cam_x = max(0, game.player.rect.centerx - GAME_WIDTH // 2)
            cam_y = 0
        game.draw(camera_offset=(cam_x, cam_y))
        pygame.display.flip()
        clock.tick(60)
        if not game.running:
            running = False
    pygame.quit()

if __name__ == "__main__":
    main()