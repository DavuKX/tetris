from block_builder import BlockBuilder
from block_director import BlockDirector
from grid import Grid
from blocks import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.constructors = self.get_constructors()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    def get_random_block(self):
        constructor = random.choice(self.constructors)
        block = constructor()

        self.constructors.remove(constructor)

        if not self.constructors:
            self.constructors = self.get_constructors()

        return block

    def get_constructors(self):
        director = BlockDirector(BlockBuilder())

        constructors = [
            director.create_i_block,
            director.create_j_block,
            director.create_l_block,
            director.create_o_block,
            director.create_s_block,
            director.create_t_block,
            director.create_z_block
        ]

        return constructors

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        self.next_block.draw(screen, 270, 270)

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()

        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.block_id

        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared, 0)

        if not self.block_fits():
            self.game_over = True

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def reset(self):
        self.grid.reset()
        self.constructors = self.get_constructors()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def update_score(self, lines_clear, move_down_points):
        if lines_clear == 1:
            self.score += 100
        elif lines_clear == 2:
            self.score += 200
        elif lines_clear == 3:
            self.score += 300
        self.score += move_down_points
