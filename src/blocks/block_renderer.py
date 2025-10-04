from abc import ABC, abstractmethod
import pygame

from src.ui.colors import Colors

class Renderer(ABC):
    @abstractmethod
    def draw_grid(self, screen, grid):
        pass

    @abstractmethod
    def draw_block(self, screen, block, offset_x, offset_y):
        pass

class BlockRenderer(Renderer):
    def __init__(self, cell_size=30):
        self.cell_size = cell_size
        self.colors = Colors.get_cell_colors()
    
    def draw_grid(self, screen, grid):
        grid.draw(screen)

    def draw_block(self, screen, block, offset_x, offset_y):
        tiles = block.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pygame.draw.rect(screen, self.colors[block.block_id], tile_rect)
