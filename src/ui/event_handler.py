"""Event handling for the Tetris game."""
import pygame
import sys
from src.core.game import Game
from src.core.game_state import GameStatus


class EventHandler:
    def __init__(self, game: Game):
        self.game = game
    
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
            self.game.reset()
        elif self.game.status == GameStatus.PLAYING:
            if event.key == pygame.K_LEFT:
                self.game.move_left()
            elif event.key == pygame.K_RIGHT:
                self.game.move_right()
            elif event.key == pygame.K_DOWN:
                self.game.move_down()
                self.game.update_score(0, 1)
            elif event.key == pygame.K_UP:
                self.game.rotate()
    
    def _handle_game_update(self):
        if self.game.status == GameStatus.PLAYING:
            self.game.move_down()
