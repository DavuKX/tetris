from abc import ABC, abstractmethod
from enum import Enum

class GameStatus(Enum):
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3

class GameState(ABC):
    @abstractmethod
    def move_down(self, game):
        pass

    @abstractmethod
    def move_left(self, game):
        pass

    @abstractmethod
    def move_right(self, game):
        pass

    @abstractmethod
    def rotate(self, game):
        pass
    

class PlayingState(GameState):
    def move_down(self, game):
       game.current_block.move(1, 0)
       
       if not game.is_valid_position():
           game.current_block.move(-1, 0)
           game.lock_block()

    def move_left(self, game):
        game.attempt_move(0, -1)

    def move_right(self, game):
        game.attempt_move(0, 1)

    def rotate(self, game):
        game.current_block.rotate()
        
        if not game.is_valid_position():
            game.current_block.undo_rotation()

class GameOverState(GameState):
    def move_down(self, game):
        # Game is over, no action can be taken
        pass

    def move_left(self, game):
        # Game is over, no action can be taken
        pass

    def move_right(self, game):
        # Game is over, no action can be taken
        pass

    def rotate(self, game):
        # Game is over, no action can be taken
        pass
