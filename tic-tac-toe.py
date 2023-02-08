import time


def intro():
    player_1 = input('Имя первого игрока: ')
    player_2 = input('Имя второго игрока: ')
    return player_1, player_2
#Выбрать размер поля
#
# n = int(input('Выберите размеры поля: \n'
#               '1 - 3*3\n'
#               '2 - 5*5\n'
#               ''))
# if n == 1:
#     n = 9
# elif n == 2:
#     n = 25
# b = list(range(1, n+1))
b = [1,2,3,4,5,6,7,8,9]
bg = [1,2,3,4,5,6,7,8,9]

def game_board(b):
    #if len(b) == 9:
        print('Игровое поле:')
        for i in range(3):
            print(f'{b[0+i*3]} | {b[1+i*3]} | {b[2+i*3]}')
    # elif len(b) == 25:
    #     for i in range(5):
    #         print(f'{b[0+i*5]} | {b[1+i*5]} | {b[2+i*5]} | {b[3+i*5]} | {b[4+i*5]}')

def user(p,a,b,s):
    print(f'Ход игрока {p}')
    print(f'Ход номер: {a}')
    game_board(b)
    valid = False
    while not valid:
        try:
            p = int(input('Введите номер клетки от 1 до 9, чтобы сделать ход: '))
            if 0 < p < 10:
                pass

            if b[p - 1] in ['X', 'O']:
                print('Клетка занята. Попробуйте еще раз')
            else:
                b[p - 1] = s
                valid = True
        except:
            print('Вам необходимо ввести номер клетки от 1 до 9. Попробуйте еще раз.')
    game_board(b)

def bot():
    

def gameplay():
    p1, p2 = intro()
    game_over = False
    while not game_over:
        for i in bg:
            if i % 2 != 0:
                user(p1, i, b, s='X')
            elif i % 2 == 0:
                user(p2, i, b, s='O')
            if i >= 5:
                if check(b):
                    if i % 2 != 0:
                        print(f'Выиграл игрок {p1}. Поздравляем!')
                        time.sleep(4)
                        game_over = True
                        break
                    elif i % 2 == 0:
                        print(f'Выиграл игрок {p2}. Поздравляем!')
                        time.sleep(4)
                        game_over = True
                        break
            if i == 9:
                print('Ничья')
                time.sleep(4)
                game_over = True
                break
    print('Хотите сыграть еще?')
    time.sleep(3)


def check(b):
    win_con = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in win_con:
        if b[w[0]] == b[w[1]] == b[w[2]]:
            return True
    return False

def decor(func):
    def wrapper():
        print('Обнаружен рабочий процесс.')
        result = func()
        print('Рабочих процессов не обнаружено.')
        return result
    return wrapper

@decor
def ttt():
    import time
    print('Добро пожаловать в крестики-нолики!')
    time.sleep(4)
    print('Хотите начать игру?')
    time.sleep(2)
    while True:
        a = input('Нажмите "Да", чтобы начать \n'
                  'Нажмите "Нет", чтобы выйти \n'
                  '')
        y_opt = ['Да', 'да', 'lf', 'ДА', 'LF', 'yes', 'y']
        n_opt = ['Нет', 'нет', 'НЕТ', 'ytn', 'YTN', 'no', 'n']
        if a in y_opt:
            game_board(b)
            gameplay()
            check(b)
        elif a in n_opt:
            print('"Завершение работы приложения..."')
            time.sleep(4)
            print('Процесс успешно завершен.')
            break
        else:
            print('Ответ не распознан, попробуйте еще раз.')


ttt()
