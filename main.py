# This is Tic Tac Toe game

import random

board = ['-']*9     # main board where the positions are saved. start with full spaces

player1_marker = ''   # assigned value of X or O
player2_marker = ''
next_player = ''    # player 1 or player 2
marker = ''
game_on = True      # for main while loop to continue the game
position = 0

def assign_marker():
    marker = input('Player 1: Choose your marker (X or O): ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def display_board(in_board):
    # simply print a board if positions are fed as a list
    print(' ' + in_board[0] + ' | ' + in_board[1] + ' | ' + in_board[2] + ' ')
    # print('-----------')
    print(' ' + in_board[3] + ' | ' + in_board[4] + ' | ' + in_board[5] + ' ')
    # print('-----------')
    print(' ' + in_board[6] + ' | ' + in_board[7] + ' | ' + in_board[8] + ' ')

def display_reference_board():
    # print a board with positions numbered, for a reference
    print('These are the board positions for your reference:')
    print(' 1 | 2 | 3 ')
    print(' 4 | 5 | 6 ')
    print(' 7 | 8 | 9 ')

def place_marker(in_board, marker, position):
    in_board[position] = marker

def win_check(in_board, mark):
    # check each row and column, and both diagonals against the marker passed as parameter
    return (in_board[0] == mark and in_board[1] == mark and in_board[2] == mark) or \
    (in_board[3] == mark and in_board[4] == mark and in_board[5] == mark) or \
    (in_board[6] == mark and in_board[7] == mark and in_board[8] == mark) or \
    (in_board[0] == mark and in_board[4] == mark and in_board[8] == mark) or \
    (in_board[2] == mark and in_board[4] == mark and in_board[6] == mark) or \
    (in_board[0] == mark and in_board[3] == mark and in_board[6] == mark) or \
    (in_board[1] == mark and in_board[4] == mark and in_board[7] == mark) or \
    (in_board[2] == mark and in_board[5] == mark and in_board[8] == mark)

def is_board_full(in_board):
    is_full = True
    for i in range(0,len(in_board)):
        if in_board[i] == '-':
            is_full = False
            break
    return is_full

player1_marker, player2_marker = assign_marker()
next_player = choose_first()
print(next_player + " goes first!")
display_reference_board()

# main while loop which holds the game
while game_on:
    # if next turn is player 1, take input from player 1
    if next_player == 'Player 1':
        # take position as input
        # display_reference_board()
        position = int(input('Player 1 - Enter your marker position (1 to 9): '))
        # place the marker in the position
        place_marker(board, player1_marker, position-1)
        display_board(board)
        # check if player 1 has won
        if win_check(board, player1_marker):
            print('Player 1 has won!')
            game_on = False
            continue
        # check if board is full - a tie
        if is_board_full(board):
            print('It is a tie!')
            game_on = False
            continue
        # pass control to the other player
        next_player = 'Player 2'

    # if next turn is player 2, take input from player 2
    if next_player == 'Player 2':
        # take position as input
        # display_reference_board()
        position = int(input('Player 2 - Enter your marker position (1 to 9): '))
        # place the marker in the position
        place_marker(board, player2_marker, position-1)
        display_board(board)
        # check if player 2 has won
        if win_check(board,player2_marker):
            print('Player 2 has won!')
            game_on = False
            continue
        # check if board is full - a tie
        if is_board_full(board):
            print('It is a tie!')
            game_on = False
            continue
        # pass control to the next player
        next_player = 'Player 1'