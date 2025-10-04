from abc import ABC, abstractmethod
from src.core.game import Game


class GameCommand(ABC):
    
    @abstractmethod
    def execute(self, game: Game):
        pass
    
    @abstractmethod
    def can_execute(self, game: Game) -> bool:
        pass


class MoveLeftCommand(GameCommand):
    
    def execute(self, game: Game):
        game.move_left()
    
    def can_execute(self, game: Game) -> bool:
        from src.core.game_state import GameStatus
        return game.status == GameStatus.PLAYING


class MoveRightCommand(GameCommand):
    def execute(self, game: Game):
        game.move_right()
    
    def can_execute(self, game: Game) -> bool:
        from src.core.game_state import GameStatus
        return game.status == GameStatus.PLAYING


class MoveDownCommand(GameCommand):
    def execute(self, game: Game):
        game.move_down()
        game.update_score(0, 1)
    
    def can_execute(self, game: Game) -> bool:
        from src.core.game_state import GameStatus
        return game.status == GameStatus.PLAYING


class RotateCommand(GameCommand):
    def execute(self, game: Game):
        game.rotate()
    
    def can_execute(self, game: Game) -> bool:
        from src.core.game_state import GameStatus
        return game.status == GameStatus.PLAYING


class ResetGameCommand(GameCommand):
    def execute(self, game: Game):
        game.reset()
    
    def can_execute(self, game: Game) -> bool:
        from src.core.game_state import GameStatus
        return game.status == GameStatus.GAME_OVER


class HardDropCommand(GameCommand):
    def execute(self, game: Game):
        from src.core.game_state import GameStatus
        
        while game.status == GameStatus.PLAYING:
            game.current_block.move(1, 0)
            
            if not game.is_valid_position():
                game.current_block.move(-1, 0)
                break
            
            game.update_score(0, 1)
    
    def can_execute(self, game: Game) -> bool:
        from src.core.game_state import GameStatus
        return game.status == GameStatus.PLAYING
