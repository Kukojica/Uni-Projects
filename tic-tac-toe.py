#def intro():
#     player_1 = input('Имя первого игрока')
#     player_2 = input('Имя второго игрока')
#     return player_1, player_2
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
        for i in range(3):
            print(f'{b[0+i*3]} | {b[1+i*3]} | {b[2+i*3]}')
    # elif len(b) == 25:
    #     for i in range(5):
    #         print(f'{b[0+i*5]} | {b[1+i*5]} | {b[2+i*5]} | {b[3+i*5]} | {b[4+i*5]}')

def gameplay():
    game_board(b)
    win = False
    while not win:
        for i in bg:
            if i % 2 != 0:
                print('Ход игрока 1')
                print(f'Ход номер: {i}')
                valid = False
                while not valid:
                    p = int(input('Введите номер клетки, чтобы сделать ход: '))
                    if 0 < p < 10:
                        pass
                    else:
                        print('Клетки с таким номером не существует! Попробуйте еще раз.')
                    if b[p - 1] in ['X', 'O']:
                        print('Клетка занята. Попробуйте еще раз')
                    else:
                        b[p-1] = 'X'
                        valid = True
                game_board(b)
                if i >= 5:
                    check(b)
                    win = True
            elif i % 2 == 0:
                print('Ход игрока 2')
                print(f'Ход номер: {i}')
                p = int(input('Введите номер клетки, чтобы сделать ход: '))
                valid = False
                while not valid:
                    if 0 < p < 10:
                        pass
                    else:
                        print('Клетки с таким номером не существует! Попробуйте еще раз.')
                    if b[p - 1] in ['X', 'O']:
                        print('Клетка занята. Попробуйте еще раз')
                    else:
                        b[p - 1] = 'O'
                        valid = True
                game_board(b)
                if i >= 5:
                    check(b)
                    win = True




def check(b):
    win_con = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for w in win_con:
        if b[w[0]] == b[w[1]] == b[w[2]]:
            print('победа')

gameplay()

