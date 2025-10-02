import pygame
import sys
from src.core.game import Game
from src.core.game_state import GameStatus
from src.ui.input_mapper import InputMapper
from src.ui.game_commands import ResetGameCommand


class EventHandler:
    def __init__(self, game: Game, input_mapper: InputMapper = None):
        self.game = game
        self.input_mapper = input_mapper or InputMapper()
        self.reset_command = ResetGameCommand()
    
    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            
            if event.type == pygame.USEREVENT:
                self._handle_game_update()
        
        return True
    
    def _handle_keydown(self, event):
        if self.game.status == GameStatus.GAME_OVER:
            if self.reset_command.can_execute(self.game):
                self.reset_command.execute(self.game)
            return
        
        command = self.input_mapper.get_command(event.key)
        
        if command and command.can_execute(self.game):
            command.execute(self.game)
    
    def _handle_game_update(self):
        if self.game.status == GameStatus.PLAYING:
            self.game.move_down()
