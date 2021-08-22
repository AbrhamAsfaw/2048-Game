
# 2048 By Abrham Asfaw ATE_5110_09


# Main file where the game starts to run 

import pygame
from pygame.locals import *
import logic as l
import board as b
import sys
import layout as lyt

cols = 4
rows = 4
black = 0, 0, 0


pygame.init()
pygame.display.set_caption("2048 By Abrham Asfaw")

SIZE = width, height = cols * lyt.TILE_SIZE + (cols + 1) * lyt.PADDING,\
                       rows * lyt.TILE_SIZE + (rows + 1) * lyt.PADDING
screen = pygame.display.set_mode(SIZE)

twenty_forty_eight = l.TwentyFortyEight(rows, cols, lyt.OFFSETS)
board = b.Board(rows, cols, twenty_forty_eight.get_game_state(), lyt.PADDING, lyt.TILE_SIZE,
                lyt.BACKGROUND_COLOR, lyt.BACKGROUND_COLOR_EMPTY_TILE, lyt.BACKGROUND_TILE_COLORS,
                lyt.TILE_COLORS, lyt.FONT)

screen.fill(black)
# Main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                twenty_forty_eight.move(lyt.LEFT)
                board.update_board(twenty_forty_eight.get_game_state())
            elif event.key == pygame.K_RIGHT:
                twenty_forty_eight.move(lyt.RIGHT)
                board.update_board(twenty_forty_eight.get_game_state())
            elif event.key == pygame.K_UP:
                twenty_forty_eight.move(lyt.UP)
                board.update_board(twenty_forty_eight.get_game_state())
            elif event.key == pygame.K_DOWN:
                twenty_forty_eight.move(lyt.DOWN)
                board.update_board(twenty_forty_eight.get_game_state())

    board.draw_board()
    board.draw_tiles()
    screen.blit(board.get_board(), (0, 0))
    pygame.display.update()
    pygame.display.flip()
