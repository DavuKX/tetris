import sys
import pygame
from block_factory import RandomBagBlockFactory, TrueRandomBlockFactory
from block_renderer import BlockRenderer
from game import Game
from score_observer import ScoreDatabaseObserver
from ui_config import UIConfig
from ui_renderer import UIRenderer
from event_handler import EventHandler


def initialize_pygame():
    pygame.init()
    screen = pygame.display.set_mode((UIConfig.SCREEN_WIDTH, UIConfig.SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    return screen, clock


def create_game():
    block_factory = RandomBagBlockFactory()
    # block_factory = TrueRandomBlockFactory()
    renderer = BlockRenderer()
    game = Game(block_factory, renderer)
    
    score_observer = ScoreDatabaseObserver()
    game.attach_observer(score_observer)
    
    return game, score_observer


def setup_game_timer():
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, UIConfig.GAME_UPDATE_INTERVAL)
    return GAME_UPDATE


def main():
    screen, clock = initialize_pygame()
    game, score_observer = create_game()
    setup_game_timer()
    
    ui_renderer = UIRenderer(screen)
    event_handler = EventHandler(game)
    
    running = True
    while running:
        running = event_handler.handle_events()
        
        ui_renderer.render(game, score_observer)
        
        pygame.display.update()
        clock.tick(UIConfig.FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
