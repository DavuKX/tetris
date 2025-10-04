import pygame
from src.ui.colors import Colors
from src.ui.ui_config import UIConfig
from src.core.game import Game
from src.core.game_state import GameStatus
from src.observers.score_observer import ScoreDatabaseObserver


class UIRenderer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.title_font = pygame.font.Font(None, UIConfig.TITLE_FONT_SIZE)
        self.small_font = pygame.font.Font(None, UIConfig.SMALL_FONT_SIZE)
        
        self.score_title = self.title_font.render("Score", True, Colors.white)
        self.next_title = self.title_font.render("Next", True, Colors.white)
        self.high_scores_title = self.title_font.render("Scores", True, Colors.white)
        self.game_over_text = self.title_font.render("GAME OVER", True, Colors.white)
        
        self.score_rect = pygame.Rect(
            UIConfig.PANEL_X, UIConfig.SCORE_Y, 
            UIConfig.PANEL_WIDTH, UIConfig.SCORE_HEIGHT
        )
        self.next_rect = pygame.Rect(
            UIConfig.PANEL_X, UIConfig.NEXT_Y,
            UIConfig.PANEL_WIDTH, UIConfig.NEXT_HEIGHT
        )
        self.high_scores_rect = pygame.Rect(
            UIConfig.PANEL_X, UIConfig.HIGH_SCORES_Y,
            UIConfig.PANEL_WIDTH, UIConfig.HIGH_SCORES_HEIGHT
        )
    
    def render(self, game: Game, score_observer: ScoreDatabaseObserver):
        self.screen.fill(Colors.dark_blue)
        
        self._render_score_section(game.score)
        self._render_next_section()
        self._render_high_scores_section(score_observer)
        
        if game.status == GameStatus.GAME_OVER:
            self._render_game_over()
        
        game.draw(self.screen)
    
    def _render_score_section(self, score: int):
        self.screen.blit(self.score_title, (UIConfig.SCORE_TITLE_X, UIConfig.SCORE_TITLE_Y))
        
        pygame.draw.rect(
            self.screen, Colors.light_blue, 
            self.score_rect, 0, UIConfig.BORDER_RADIUS
        )
        
        score_surface = self.title_font.render(str(score), True, Colors.white)
        score_rect = score_surface.get_rect(
            centerx=self.score_rect.centerx,
            centery=self.score_rect.centery
        )
        self.screen.blit(score_surface, score_rect)
    
    def _render_next_section(self):
        self.screen.blit(self.next_title, (UIConfig.NEXT_TITLE_X, UIConfig.NEXT_TITLE_Y))
        
        pygame.draw.rect(
            self.screen, Colors.light_blue,
            self.next_rect, 0, UIConfig.BORDER_RADIUS
        )
    
    def _render_high_scores_section(self, score_observer: ScoreDatabaseObserver):
        self.screen.blit(
            self.high_scores_title,
            (UIConfig.HIGH_SCORES_TITLE_X, UIConfig.HIGH_SCORES_TITLE_Y)
        )
        
        pygame.draw.rect(
            self.screen, Colors.light_blue,
            self.high_scores_rect, 0, UIConfig.BORDER_RADIUS
        )
        
        high_scores = score_observer.get_high_scores(UIConfig.HIGH_SCORES_COUNT)
        y_offset = UIConfig.HIGH_SCORES_START_Y
        
        for i, (score, date) in enumerate(high_scores, 1):
            score_text = self.small_font.render(f"{i}. {score}", True, Colors.white)
            self.screen.blit(score_text, (UIConfig.HIGH_SCORES_TEXT_X, y_offset))
            y_offset += UIConfig.HIGH_SCORES_LINE_HEIGHT
        
        for i in range(len(high_scores), UIConfig.HIGH_SCORES_COUNT):
            score_text = self.small_font.render(f"{i+1}. ---", True, Colors.white)
            self.screen.blit(score_text, (UIConfig.HIGH_SCORES_TEXT_X, y_offset))
            y_offset += UIConfig.HIGH_SCORES_LINE_HEIGHT
    
    def _render_game_over(self):
        self.screen.blit(self.game_over_text, (UIConfig.GAME_OVER_X, UIConfig.GAME_OVER_Y))
