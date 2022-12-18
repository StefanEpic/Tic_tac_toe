import random


def greetings():
    player_name = int(random.randint(100, 1000))
    print(f'\t\t┈┈┈☆☆☆☆☆☆☆┈┈┈')
    print(f'\t\t┈┈╭┻┻┻┻┻┻┻┻┻╮┈┈')
    print(f'\t\t┈┈┃╱╲╱╲╱╲╱╲╱┃┈┈')
    print(f'\t\t┈╭┻━━━━━━━━━┻╮┈')
    print(f'\t\t┈┃╱╲╱╲╱╲╱╲╱╲╱┃┈')
    print(f'\t\t┈┗━━━━━━━━━━━┛┈ ')
    print(f'\tРада видеть тебя, Испытуемая №{player_name}!')
    print(f'\tВ этом маленьком тесте GLaDOS проверит, насколько ты смышленная...')
    print()
    print('\tПоиграем?')
    input('\tPress enter to continue...')


def show_battle_place():
    print()
    print("       0   1   2   ")
    print("     -------------")
    for i, row in enumerate(field):
        row_str = f"  {i}  | {' | '.join(row)} |"
        print(row_str)
        print("     -------------")
    print()


def input_coordinates():
    while True:
        cords = input("\t>>>>>>: ").split()

        if len(cords) != 2:
            print("\tGLaDOS: Эй! Надо 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("\tGLaDOS: Координаты буквами?? Введите числа!! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("\tGLaDOS: От 0 до 2! Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print("\tGLaDOS: Нет, нет, нет! Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    glados_win = ["Это было не плохо...\nА. Нет. Плохо", "Хм..., а ты точно поняла смысл игры??",
                  "Ты проиграла... Снова."]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            for i in range(3):
                field[cord[i][0]][cord[i][1]] = ''
            show_battle_place()
            print("\tGLaDOS: Молодец! Ты прошла испытание и заслужила тортик! 🎂")
            return True
        if symbols == ["0", "0", "0"]:
            for i in range(3):
                field[cord[i][0]][cord[i][1]] = ''
            show_battle_place()
            print(f"\tGLaDOS: {glados_win[random.randint(0, 2)]}")
            return True
        if " " not in field[0] and " " not in field[1] and " " not in field[2]:
            show_battle_place()
            print("\tOoops! У кое-кого больше нет ходов... \n\tМожет в следующий раз...")
            return True
    return False


def gla_move():
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if field[x][y] == " ":
            field[x][y] = "0"
            break


greetings()
game = '+'
while game == '+':
    player_move = ["Твой ход...", "Ну же, ходи...", "Ходи же.."]
    field = [[" "] * 3 for i in range(3)]
    while True:
        gla_move()
        if check_win():
            break
        show_battle_place()
        print(f"\tGLaDOS: {player_move[random.randint(0, 2)]}")
        x, y = input_coordinates()
        field[x][y] = "X"
        if check_win():
            break
    game = input('\tGLaDOS: Еще разок? (+/-):')
