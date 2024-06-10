import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, position, *groups):
        super().__init__(*groups)
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, surface, offset):
        surface.blit(self.image, self.rect.move(offset))


class Group(pygame.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(*sprites)

    def draw(self, surface, offset):
        for sprite in self.sprites():
            sprite.draw(surface, offset)
