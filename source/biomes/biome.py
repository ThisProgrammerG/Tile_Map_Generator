import random
from dataclasses import dataclass

import pygame

from source.sprite import Sprite
from source.tile_sheet_loader import get_tile_range

biome_data = {
    "Desert": {
        "height": 2,
        "moisture": 0,
        "heat": 0.5,
        "tile_range": [[59, 12], [61, 12]]
    },
    "Forest": {
        "height": 2,
        "moisture": 0.4,
        "heat": 0.4,
        "tile_range": [[37, 12], [40, 12]]
    },
    "Grassland": {
        "height": 2,
        "moisture": 0.5,
        "heat": 0.3,
        "tile_range": [[1, 15], [6, 15]]
    },
    "Jungle": {
        "height": 3,
        "moisture": 0.5,
        "heat": 0.62,
        "tile_range": [[45, 13], [48, 13]]
    },
    "Mountains": {
        "height": 0.5,
        "moisture": 0,
        "heat": 0,
        "tile_range": [[41, 13], [52, 13]]
    },
    "Ocean": {
        "height": 0,
        "moisture": 0,
        "heat": 0,
        "tile_range": [[36, 19], [42, 19]]
    },
    "Tundra": {
        "height": 0.2,
        "moisture": 0,
        "heat": 0,
        "tile_range": [[14, 13], [21, 13]]
    }
}

@dataclass(slots=True)
class BiomePreset:
    name: str
    tiles: [Sprite]
    minimum_height: float
    minimum_moisture: float
    minimum_heat: float

    def get_tile_sprite(self) -> Sprite:
        return random.choice(self.tiles)

    def match_condition(self, height: float, moisture: float, heat: float) -> bool:
        height_condition = height >= self.minimum_height
        moisture_condition = moisture >= self.minimum_moisture
        heat_condition = heat >= self.minimum_heat
        return height_condition and moisture_condition and heat_condition


@dataclass(slots=True)
class BiomeTempData:
    biome: BiomePreset

    def get_difference_value(self, height: float, moisture: float, heat: float) -> float:
        difference = sum(
            (
                height - self.biome.minimum_height,
                moisture - self.biome.minimum_moisture,
                heat - self.biome.minimum_heat
            )
        )
        return difference


def load_biomes(sheet: [[pygame.Surface]]) -> [BiomePreset]:
    biomes = []
    for name, data in biome_data.items():
        tiles = get_tile_range(sheet, data["tile_range"][0], data["tile_range"][1])
        biome = BiomePreset(
            name=name,
            tiles=tiles,
            minimum_height=data["height"],
            minimum_moisture=data["moisture"],
            minimum_heat=data["heat"],
        )
        biomes.append(biome)

    return biomes


def get_best_fit(selected_biomes: [BiomeTempData], height: float, moisture: float, heat: float):
    return min(
        selected_biomes,
        key=lambda biome_temp_data: biome_temp_data.get_difference_value(height, moisture, heat),
        default=None
    )


def get_biome(biomes: [BiomePreset], height: float, moisture: float, heat: float) -> BiomePreset:
    biome_temporary_data: [BiomeTempData] = []

    for biome in biomes:
        if biome.match_condition(height, moisture, heat):
            biome_temporary_data.append(BiomeTempData(biome))

    if best_fit := get_best_fit(biome_temporary_data, height, moisture, heat):
        return best_fit.biome
    return biomes[0]
