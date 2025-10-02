from src.blocks.block_factory import BlockFactory
from src.blocks.block_renderer import Renderer
from src.core.game_state import GameState, PlayingState, GameOverState, GameStatus
from src.core.grid import Grid
from src.core.scoring_manager import GameScoreManager
from typing import List


class Game:
    def __init__(self, block_factory: BlockFactory, renderer: Renderer, state: GameState = PlayingState()):
        self.grid = Grid()
        self.block_factory = block_factory
        self.current_block = self.block_factory.create_random_block()
        self.next_block = self.block_factory.create_random_block()
        
        self.status = GameStatus.PLAYING
        self.block_renderer = renderer
        self.score_manager = GameScoreManager()

        self._state = state
        self._observers = []  # List of observers

    def draw(self, screen):
        self.block_renderer.draw_grid(screen, self.grid)
        self.block_renderer.draw_block(screen, self.current_block, 11, 11)
        self.block_renderer.draw_block(screen, self.next_block, 270, 270)

    def move_left(self):
        self._state.move_left(self)

    def move_right(self):
        self._state.move_right(self)

    def move_down(self):
        self._state.move_down(self)

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()

        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.block_id

        self.current_block = self.next_block
        self.next_block = self.block_factory.create_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.score_manager.update_score(rows_cleared, 0)

        if not self.block_fits():
            self.status = GameStatus.GAME_OVER
            self._state = GameOverState()
            self._notify_game_over()  # Notify observers

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def rotate(self):
        self._state.rotate(self)

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def reset(self):
        self.grid.reset()
        self.block_factory.reset_bag()
        self.current_block = self.block_factory.create_random_block()
        self.next_block = self.block_factory.create_random_block()
        self.score_manager.reset_score()
        self.status = GameStatus.PLAYING
        self._state = PlayingState()

    def update_score(self, lines_clear, move_down_points):
        self.score_manager.update_score(lines_clear, move_down_points)
    
    def is_valid_position(self):
        return self.block_inside() and self.block_fits()

    def _attempt_move(self, row_offset, col_offset):
        self.current_block.move(row_offset, col_offset)

        if not self.is_valid_position():
            self.current_block.move(-row_offset, -col_offset)

    @property
    def score(self):
        return self.score_manager.score
    
    def attach_observer(self, observer):
        self._observers.append(observer)
    
    def detach_observer(self, observer):
        self._observers.remove(observer)
    
    def _notify_game_over(self):
        for observer in self._observers:
            observer.on_game_over(self.score)
