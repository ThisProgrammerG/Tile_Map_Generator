import pygame

from source.wave import Wave

import noise
help(noise)

def normalize(heightmap):
    min_value = min(map(min, heightmap))
    max_value = max(map(max, heightmap))
    normalized_map = [[(value - min_value) / (max_value - min_value) for value in row] for row in heightmap]
    return normalized_map


def generate_noise(width: int, height: int, scale: float, waves: list[Wave], offset: pygame.Vector2) -> list[list[float]]:
    noise_map = [[0.0 for _ in range(width)] for _ in range(height)]

    for x in range(width):
        for y in range(height):
            sample_position_x = x * scale + offset.x
            sample_position_y = y * scale + offset.y

            normalization = 0.0

            for wave in waves:
                noise_map[y][x] += wave.amplitude * noise.pnoise2(
                    sample_position_x * wave.frequency + wave.seed,
                    sample_position_y * wave.frequency + wave.seed,
                )
                normalization += wave.amplitude
            noise_map[y][x] /= normalization

    return noise_map
