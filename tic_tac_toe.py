def check_win_conditions(game_field, n):
    for i in range(3):
        if game_field[i][0] == game_field[i][1] == game_field[i][2] and game_field[i][0] != '-':
            print('Сторона: (', game_field[i][0], ') победила')
            return

        elif game_field[0][i] == game_field[1][i] == game_field[2][i] and game_field[0][i] != '-':
            print('Сторона: (', game_field[0][i], ') победила')
            return

    if game_field[0][0] == game_field[1][1] == game_field[2][2] and game_field[0][0] != '-':
        print('Сторона: (', game_field[1][1], ') победила')
        return

    elif game_field[0][2] == game_field[1][1] == game_field[2][0] and game_field[0][2] != '-':
        print('Сторона: (', game_field[1][1], ') победила')
        return
    if n == 10:
        print('Ничья')
        return


def print_field(game_field):
    t = 1
    print('    1 2 3 ', end='\n')
    print('   ______')
    for i in range(3):
        for j in range(4):
            if j == 0:
                print(t, '|', end=' ')
                t += 1
            else:
                print(game_field[i][j - 1], end=' ')
        print()


def step(game_field, n):
    x, y = int(input('Введиет номер строки: ')), int(input('Введиет номер столбца: '))
    if game_field[x - 1][y - 1] == '-':
        print('Ход: ', n,
              '\n-------------------------------------------')
        if n % 2 != 0:
            game_field[x - 1][y - 1] = 'x'
            n += 1
        else:
            game_field[x - 1][y - 1] = 'o'
            n += 1

        print_field(game_field)

    else:
        print('Поле занято')

    check_win_conditions(game_field, n)

    step(game_field, n, )


def tic_tac_toe():
    game_field = [['-', '-', '-'],
                  ['-', '-', '-'],
                  ['-', '-', '-']]
    n = 1
    print_field(game_field)
    step(game_field=game_field, n=n)
