"""
Tutorial from:
"""

import pygame

from assets.paths import IMAGES_DIR
from assets.paths import TILE_SET
from source.biomes.biome import BiomePreset
from source.biomes.biome import get_biome
from source.biomes.biome import load_biomes
from source.camera import Camera
from source.map_generator import generator
from source.sprite import Group
from source.sprite import Sprite
from source.tile_sheet_loader import load_tile_sheet
from source.wave import heat_waves
from source.wave import height_waves
from source.wave import moisture_waves


def start_generating(biomes):
    width: int = 100
    height: int = 100
    scale: float = 1.0
    offset: pygame.Vector2 = pygame.Vector2()

    height_map = generator.generate_noise(width, height, scale, height_waves, offset)
    moisture_map = generator.generate_noise(width, height, scale, moisture_waves, offset)
    heat_map = generator.generate_noise(width, height, scale, heat_waves, offset)

    tiles = []
    for x in range(width):
        for y in range(height):
            biome = get_biome(biomes, height_map[y][x], moisture_map[y][x], heat_map[y][x])
            image = biome.get_tile_sprite()
            tiles.append(Sprite(image, (x * 32, y * 32)))

    return tiles


def main():
    pygame.init()
    width, height = 1500, 800
    display = pygame.display.set_mode((width, height))

    camera = Camera()
    biomes: [BiomePreset] = load_biomes(load_tile_sheet(IMAGES_DIR / TILE_SET))

    tiles = Group()
    tiles.add(start_generating(biomes))

    running = True

    while running:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    tiles.empty()
                    tiles.add(start_generating(biomes))

        camera.follow_key_press()
        display.fill("black")
        tiles.draw(display, camera.offset)
        pygame.display.flip()


if __name__ == '__main__':
    main()
