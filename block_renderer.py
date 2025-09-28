import pygame

from colors import Colors


class BlockRenderer:
    def __init__(self, cell_size=30):
        self.cell_size = cell_size
        self.colors = Colors.get_cell_colors()

    def draw(self, screen, block, offset_x, offset_y):
        tiles = block.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pygame.draw.rect(screen, self.colors[block.block_id], tile_rect)
