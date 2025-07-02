def random_goth_mommy_effect():
    import random
    return random.choice(['increase', 'decrease'])

def load_image(file_path):
    import pygame
    return pygame.image.load(file_path)

def load_sound(file_path):
    import pygame
    return pygame.mixer.Sound(file_path)