import pygame


class Camera:
    def __init__(self):
        self.target = None
        self.center = pygame.Vector2(pygame.display.get_surface().get_rect().center)
        self.position = pygame.Vector2(self.center)
        self.offset = None

    def follow_key_press(self):
        amount = 10
        keys = pygame.key.get_pressed()
        if any(keys[key] for key in [pygame.K_w, pygame.K_UP]):
            self.position += (0, -amount)
        if any(keys[key] for key in [pygame.K_s, pygame.K_DOWN]):
            self.position += (0, amount)
        if any(keys[key] for key in [pygame.K_a, pygame.K_LEFT]):
            self.position += (-amount, 0)
        if any(keys[key] for key in [pygame.K_d, pygame.K_RIGHT]):
            self.position += (amount, 0)

        self.offset = self.center - self.position