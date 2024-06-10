import json
from pathlib import Path

import pygame


def get_tile_range(sheet: [[pygame.Surface]], start: [int], end: [int]) -> [pygame.Surface]:
    tiles = []
    for y in range(start[1], end[1] + 1):
        row = []
        for x in range(start[0], end[0] + 1):
            row.append(sheet[y][x])
        tiles.extend(row)
    return tiles


def load_tile_sheet(path: Path) -> [[pygame.Surface]]:
    surface = pygame.image.load(path).convert_alpha()
    surface_rect = surface.get_rect()

    json_path = path.with_suffix(".json")
    with open(json_path) as file:
        specifications = json.load(file)

    width = surface_rect.width // specifications["columns"]
    height = surface_rect.height // specifications["rows"]

    sheet = []
    for y in range(0, surface_rect.height, height):
        row = []
        for x in range(0, surface_rect.width, width):
            rect = (x, y), (width, height)
            image = surface.subsurface(rect)
            row.append(image)
        sheet.append(row)

    return sheet
