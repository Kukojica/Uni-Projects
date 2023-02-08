string = 'abcd 134'
print(string[1:4])
print(string[0::3])
print(string[-2:-5:-1])
print(string[-1:-6:-2])
print(string[3::4])
inp = int(input('Введите число: '))
hour = inp // 3600
minute = (inp % 3600) // 60
sec = (inp % 3600) % 60
print(f'{hour} ч., {minute} мин., {sec} сек.')
