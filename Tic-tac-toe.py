def greet():
    print('Добро пожаловать в игру крести-нолики!')


greet()

field = [['-'] * 3 for _ in range(3)]


def launch():
    var = True
    while var:
        condition = input('Напишите "play" для начала игры '
                          'или "rules" для получения правил. \nВвод:')
        if condition == "play":
            var = False
            pass
        elif condition == "rules":
            print(
                'Rules: 1-е ходят крестики "X" ход осуществляется с помощью цифр,\n'
                '       писать нужно через пробел: 1-я цифра означает стороку, а 2-я столбик.')
            print(input('<<<Нажмите ENTER>>>'))
            var = False
        else:
            print("Введите только 'play' или 'rules\n иначе игра не начнётся '")


def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        place = input("Введите координаты:").split()
        if len(place) != 2:
            print(10 * '*', 'Введите две координаты, через пробел', 10 * '*')
            continue

        x, y = place

        if not (x.isdigit() and y.isdigit()):
            print(5 * '*', 'Вводите только числа', 5 * '*')
            continue
        x, y = int(x), int(y)
        if not (0 <= x < 3 and 0 <= y < 3):
            print(3 * '*', 'Вы выйшли из деапозона', '*' * 3)
            continue
        if field[x][y] != '-':
            print('*', 'Клетка занята', '*')
            continue
        break
    return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbol = []
        for c in cord:
            symbol.append(field[c[0]][c[1]])
        if symbol == ["X", "X", "X"]:
            print('Выиграл крестик "X"!!!')
            return True
        if symbol == ["0", "0", "0"]:
            print('Выиграл нолик "0"!!!')
            return True
    return False


def start():
    launch()
    count = 0
    while True:
        count += 1
        show()
        if count % 2 == 1:
            print(' Ходит крестик "X"!')
        else:
            print(' Ходит нолик "0"!')

        x, y = ask()

        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"

        if check_win():
            break

        if count == 9:
            print('Ничья!')
            break


start()
