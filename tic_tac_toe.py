import os

le_board = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

grid = {'1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '}

turn = 'X'
x_score = 0
o_score = 0


def score(side):
    global x_score
    global o_score
    if side == 'x':
        x_score += 1
    elif side == 'o':
        o_score += 1
    else:
        pass

def check():
    if grid['2'] == 'X' and grid['5'] == 'X' and grid['8'] == 'X':
        board(grid)
        print('X wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('x')
            restart()
        else: quit()
    elif grid['1'] == 'X' and grid['4'] == 'X' and grid['7'] == 'X':
        board(grid)
        print('X wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('x')
            restart()
        else: quit()
    elif grid['3'] == 'X' and grid['6'] == 'X' and grid['9'] == 'X':
        board(grid)
        print('X wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('x')
            restart()
        else: quit()
    elif grid['1'] == 'X' and grid['2'] == 'X' and grid['3'] == 'X':
        board(grid)
        print('X wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('x')
            restart()
        else: quit()
    elif grid['4'] == 'X' and grid['5'] == 'X' and grid['6'] == 'X':
        board(grid)
        print('X wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('x')
            restart()
        else: quit()
    elif grid['7'] == 'X' and grid['8'] == 'X' and grid['9'] == 'X':
        board(grid)
        print('X wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('x')
            restart()
        else: quit()
    elif grid['1'] == 'X' and grid['5'] == 'X' and grid['9'] == 'X':
        board(grid)
        print('X wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('x')
            restart()
        else: quit()
    elif grid['3'] == 'X' and grid['5'] == 'X' and grid['7'] == 'X':
        board(grid)
        print('X wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('x')
            restart()
        else: quit()
    elif grid['2'] == 'O' and grid['5'] == 'O' and grid['8'] == 'O':
        board(grid)
        print('O wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('o')
            restart()
        else: quit()
    elif grid['1'] == 'O' and grid['4'] == 'O' and grid['7'] == 'O':
        board(grid)
        print('O wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('o')
            restart()
        else: quit()
    elif grid['3'] == 'O' and grid['6'] == 'O' and grid['9'] == 'O':
        board(grid)
        print('O wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('o')
            restart()
        else: quit()
    elif grid['1'] == 'O' and grid['2'] == 'O' and grid['3'] == 'O':
        board(grid)
        print('O wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('o')
            restart()
        else: quit()
    elif grid['4'] == 'O' and grid['5'] == 'O' and grid['6'] == 'O':
        board(grid)
        print('O wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('o')
            restart()
        else: quit()
    elif grid['7'] == 'O' and grid['8'] == 'O' and grid['9'] == 'O':
        board(grid)
        print('O wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('o')
            restart()
        else: quit()
    elif grid['1'] == 'O' and grid['5'] == 'O' and grid['9'] == 'O':
        board(grid)
        print('O wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('o')
            restart()
        else: quit()
    elif grid['3'] == 'O' and grid['5'] == 'O' and grid['7'] == 'O':
        board(grid)
        print('O wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('o')
            restart()
        else: quit()
    elif grid['1'] != ' ' and grid['2'] != ' ' and grid['3'] != ' ' and grid['4'] != ' ' and grid['5'] != ' ' and grid['6'] != ' ' and grid['7'] != ' ' and grid['8'] != ' ' and grid['9'] != ' ':
        board(grid)
        print('Nobody wins')
        again = input('Play again? ')
        if again.lower() == 'yes':
            score('eh')
            restart()
        else:
            quit()


def board(tile):
    global x_score
    global o_score
    print(' ' + tile['1'] + ' | ' + tile['2'] + ' | ' + tile['3'] + ' ' + '     123')
    print('---+---+---' + '     456')
    print(' ' + tile['4'] + ' | ' + tile['5'] + ' | ' + tile['6'] + ' ' + '     789')
    print('---+---+---' + '                X: {}    O: {}'.format(x_score, o_score))
    print(' ' + tile['7'] + ' | ' + tile['8'] + ' | ' + tile['9'] + ' ')


def moves(sign):
    global turn
    move = input('Turn for ' + sign + ': ')
    if move.lower() == 'restart':
        restart()
    elif move.lower() == 'quit':
        exit()
    elif move not in grid.keys():
        print('choose a valid tile')
        error()
    elif grid[move] != ' ':
        print('choose a vacant tile')
        error()
    elif grid[move] == ' ':
        return move


def restart():
    global grid
    grid = dict(le_board)
    global turn
    turn = 'X'
    os.system('cls')

def error():
    global turn
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
    game()


def game():
    global turn
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
    grid[moves(turn)] = turn
    os.system('cls')
    check()
    board(grid)
    game()


board(grid)
game()
