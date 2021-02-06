import numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece  # pieza del jugador


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r *
                                            SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2),
                                               int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), int(SQUARESIZE/2 - 5))

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2),
                                                    height-int(r*SQUARESIZE+SQUARESIZE/2)), int(SQUARESIZE/2 - 5))
            elif board[r][c] == 2:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2),
                                                 height-int(r*SQUARESIZE+SQUARESIZE/2)), int(SQUARESIZE/2 - 5))

    pygame.display.update()


def winning_move(board, piece):
    # Check horizontal
    # no hace falta todas las columnas,
    # a partir de las tres últimas no se puede ganar
    # (no puede haber 4 seguidas)
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check diagonal positiva
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check diagonal negativa
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE  # para tirar la ficha

size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, YELLOW, (posx, int(
                    SQUARESIZE/2)), int(SQUARESIZE/2 - 5))
            else:
                pygame.draw.circle(screen, RED, (posx, int(
                    SQUARESIZE/2)), int(SQUARESIZE/2 - 5))
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # print(event.pos)
            # Preguntar input jugador 1
            if turn == 0:
                posx = event.pos[0]  # entre 0 a 700
                col = int(math.floor(posx/SQUARESIZE))

                #col = int(input("Jugador 1 haz tu selección (0-6): "))
                #print("Jugador 1: "+str(col))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        print("Jugador 1 gana!!!")
                        label = myfont.render("Jugador 1 gana!!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

            # Preguntar input jugador 2
            if turn == 1:
                posx = event.pos[0]  # entre 0 a 700
                col = int(math.floor(posx/SQUARESIZE))

                #col = int(input("Jugador 1 haz tu selección (0-6): "))
                #print("Jugador 1: "+str(col))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        print("Jugador 2 gana!!!")
                        label = myfont.render("Jugador 2 gana!!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

            turn = int((turn + 1)) % 2
            print_board(board)
            draw_board(board)

            if game_over:
                pygame.time.wait(3000)
