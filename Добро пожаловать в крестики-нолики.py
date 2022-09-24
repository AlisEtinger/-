#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('Добро пожаловать в крестики-нолики!')

from IPython.display import clear_output
import random


def choose_first():
    if random.randint(0,1) == 0:
        return 'player2'
    else:
        return 'player1'


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Вы хотите быть X или O? ").upper()

    if marker == 'X':
        return 'X'
    else:
        return 'O'


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Выберите следующую позицию: (1-9): '))
    return position


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def replay():
    key = input('Вы хотите играть снова? Введите Да или Нет: ')
    return True if key[0].upper() == 'Y' else False


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (
        (board[1]==mark and board[2]==mark and board[3]==mark) or
        (board[4]==mark and board[5]==mark and board[6]==mark) or
        (board[7]==mark and board[8]==mark and board[9]==mark) or
        (board[1]==mark and board[4]==mark and board[7]==mark) or
        (board[2]==mark and board[5]==mark and board[8]==mark) or
        (board[3]==mark and board[6]==mark and board[9]==mark) or
        (board[1]==mark and board[5]==mark and board[9]==mark) or
        (board[3]==mark and board[5]==mark and board[7]==mark)
    )


def display_board(board):
    clear_output()

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker = player_input()
    player2_marker = player_input()

    turn = choose_first()
    print(turn + ' пойдет первым')

    play_game = input('Are you ready to play? yes or no? ')

    if play_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            # Player1 turn 

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Поздравляем! Вы выиграли игру!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Игра вничью!')
                    break
                else:
                    turn = 'Player2'


        else:
            # player2 turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player2 выиграл!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Игра вничью!')
                    break
                else:
                    turn = 'Player1'

    if not replay():
        break


# In[ ]:




