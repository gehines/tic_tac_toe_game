board = list(range(1, 10))
win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')


def take_input(player):
    while True:
        value = input('Игрок ' + player + ' ходит. Введите число на клетке: ')
        if not (value in '123456789'):
            print('Данного числа нет на поле. Введите заново.')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Это клетка уже занята. Введите другое число: ')
            continue
        board[value - 1] = player
        break


def check_win():
    for each in win_combinations:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    move = 0
    while True:
        draw_board()
        if move % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if move > 3:
            winner = check_win()
            if winner:
                draw_board()
                print('Игрок', winner, "выйграл!")
                break
        move += 1
        if move > 8:
            draw_board()
            print('Ничья')
            break

main()