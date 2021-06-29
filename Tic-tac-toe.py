field = [['-'] * 3 for _ in range(3)]
qq = '^*^  ' * 10
smail = '^_^'
print('Добро пожаловать в игру крести-нолина на python. \nСпасибо Skill-Factory за курс и помощь' '\n', qq)
print('')


def qus():
    var = True
    while var:

        kiki = input('Напишите "play" для начала игры '
                     'или "rules" для получения правил \nВвод:')
        if kiki == "play":
            var = False
            pass
        elif kiki == "rules":
            print(
                'Rules: 1-е ходят крестики "х" ход осуществляется с помощью цифр,'
                ' писать нужно через пробел и 1-я цифра означает стороку, а 2-я столбик ')
            print(input('<<<Нажмите ENTER>>>'))
            var = False
        else:
            print("Введите только 'play' или 'rules\n иначе игра не начнётся '")


def show(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))


def user_input(f, user):
    while True:
        place = input(f"Ходит {user}. Введите координаты:").split()  # Разбивает ввод на  на list [1,2]
        if len(place) != 2:
            print(10 * '*', 'Введите две координаты, через пробел', '*' * 10)
            continue

        if not (place[0].isdigit() and place[1].isdigit()):  # isdigit проверяет содержит ли только числа (bool)значение
            print(5 * '*', 'Вводите только числа', '*' * 5)
            continue
        x, y = map(int, place)
        if not (0 <= x < 3 and 0 <= y < 3):  # if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print(3 * '*', 'Вы выйшли из деапозона', '*' * 3)
            continue
        if f[x][y] != '-':
            print('*', 'Клетка занята', '*')
            continue
        break
    return x, y


def win_v2(f, user):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        simvol = []
        for c in cord:
            simvol.append(f[c[0]][c[1]])
        if simvol == [user, user, user]:
            return True
    return False


def start(f):
    qus()
    count = 0
    while True:
        show(f)
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        if count < 9:
            x, y = user_input(f, user)
            f[x][y] = user

        elif count == 9:
            print(f'{smail} Ничья {smail}')
            break
        if win_v2(field, user):
            print(f"Выйграл {user},\n nice")
            show(field)
            break
        count += 1


start(field)
