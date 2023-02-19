import random

_BOARD_SIZE = 8
_board = [[0] * _BOARD_SIZE for _ in range(_BOARD_SIZE)]
_NUM_BOARDS = 4


def _clear_board():
    for i in range(len(_board)):
        for j in range(len(_board[i])):
            _board[i][j] = 0


def check_queens(queens):
    _clear_board()
    for queen in queens:
        _board[queen[0]][queen[1]] = 1
    for row in _board:
        if sum(row) > 1:
            return False
    for col in (x for x in zip(*_board)):
        if sum(col) > 1:
            return False

    for i in range(-(_BOARD_SIZE - 1), _BOARD_SIZE):
        _sum = 0
        for j in range(_BOARD_SIZE):
            row, col = j, i + j
            if 0 <= row < len(_board) and 0 <= col < len(_board[0]):
                _sum += _board[row][col]
                if _sum > 1:
                    return False
    for i in range(-(_BOARD_SIZE - 1), _BOARD_SIZE):
        _sum = 0
        for j in range(_BOARD_SIZE):
            row, col = j, i + j
            if 0 <= row < len(_board) and 0 <= col < len(_board[0]):
                _sum += _board[row][_BOARD_SIZE - col - 1]
                if _sum > 1:
                    return False
    return True


def print_board():
    print(' ', end='')
    print(*(f" {x}" for x in range(_BOARD_SIZE)))
    for y in range(len(_board)):
        print(y, ' ', end='', sep='')
        for x in range(len(_board[y])):
            if _board[x][y] == 1:
                print('Q  ', end='', sep='')
            else:
                print('+  ', end='', sep='')
        print()
    print()


def get_rand_boards():
    win_count = 0
    count = 0
    rand_array = [x for x in range(_BOARD_SIZE)]
    while win_count < _NUM_BOARDS:
        count += 1
        queen_list = []
        random.shuffle(rand_array)
        for q in range(8):
            queen_list.append((rand_array[q], q))
        if check_queens(queen_list):
            print_board()
            win_count += 1


if __name__ == "__main__":
    get_rand_boards()
