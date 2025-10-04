import pygame
from typing import Dict
from src.ui.game_commands import (
    GameCommand,
    MoveLeftCommand,
    MoveRightCommand,
    MoveDownCommand,
    RotateCommand,
    ResetGameCommand,
    HardDropCommand,
)


class InputMapper:
    def __init__(self):
        self._key_bindings: Dict[int, GameCommand] = self._create_default_bindings()
    
    def _create_default_bindings(self) -> Dict[int, GameCommand]:
        return {
            pygame.K_LEFT: MoveLeftCommand(),
            pygame.K_RIGHT: MoveRightCommand(),
            pygame.K_DOWN: MoveDownCommand(),
            pygame.K_UP: RotateCommand(),
            pygame.K_w: ResetGameCommand(),
            pygame.K_SPACE: HardDropCommand(),
        }
    
    def get_command(self, key: int) -> GameCommand | None:
        return self._key_bindings.get(key)
    
    def bind_key(self, key: int, command: GameCommand):
        self._key_bindings[key] = command
    
    def unbind_key(self, key: int):
        if key in self._key_bindings:
            del self._key_bindings[key]
    
    def get_all_bindings(self) -> Dict[int, GameCommand]:
        return self._key_bindings.copy()
