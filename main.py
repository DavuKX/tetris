import sys
import pygame
from block_factory import RandomBagBlockFactory, TrueRandomBlockFactory
from block_renderer import BlockRenderer
from game import Game
from game_state import GameStatus
from colors import Colors
from score_observer import ScoreDatabaseObserver

dark_blue = (44, 44, 127)
pygame.init()
title_font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 25)

score_surface = title_font.render("Score", True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 60)

next_surface = title_font.render("Next", True, Colors.white)
next_rect = pygame.Rect(320, 215, 170, 180)

high_scores_surface = title_font.render("Scores", True, Colors.white)
high_scores_rect = pygame.Rect(320, 445, 170, 150)

game_over_surface = title_font.render("GAME OVER", True, Colors.white)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

block_factory = TrueRandomBlockFactory()
renderer = BlockRenderer()

game = Game(block_factory, renderer)

score_observer = ScoreDatabaseObserver()
game.attach_observer(score_observer)

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.status == GameStatus.GAME_OVER:
                game.reset()
            elif game.status == GameStatus.PLAYING:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()
        if event.type == GAME_UPDATE and game.status == GameStatus.PLAYING:
            game.move_down()

    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    
    high_scores = score_observer.get_high_scores(3)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    screen.blit(high_scores_surface, (355, 410, 50, 50))

    if game.status == GameStatus.GAME_OVER:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface,
                score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    
    pygame.draw.rect(screen, Colors.light_blue, high_scores_rect, 0, 10)
    
    y_offset = 460
    for i, (score, date) in enumerate(high_scores, 1):
        score_text = small_font.render(f"{i}. {score}", True, Colors.white)
        screen.blit(score_text, (335, y_offset))
        y_offset += 30
    
    for i in range(len(high_scores), 3):
        score_text = small_font.render(f"{i+1}. ---", True, Colors.white)
        screen.blit(score_text, (335, y_offset))
        y_offset += 30
    
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
