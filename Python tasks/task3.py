# 3.7
# inp = input()
# inp1 = inp.split(' ')
# l = list(map(int, inp1))
# a,b,c = l
# # a = int(input('a '))
# # b = int(input('b '))
# # c = int(input('c '))
# if a + b > c and a + c > b and b + c > a:
#     print('ye')
# else:
#     print('nah')

# 3.8
# year = int(input('Year: '))
# if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
#     print('Високосный')
# else:
#     print('Обычный')

# 3.10
# a = list(input('Number: '))
# lst = list(map(int, a))
#
# if len(lst) == 2 and lst[0] == lst[1]:
#     print('Счастливый')
# elif len(lst) == 4 and sum(lst[:2]) == sum(lst[2:]):
#     print('Счастливый')
# elif len(lst) == 6 and sum(lst[:3]) == sum(lst[3:]):
#     print('Счастливый')
# else:
#     print('Несчастливый')

# 4.1
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
# a = int(input('Number: '))
# if a == 1:
#     print(m[:20])
# elif a == 2:
#     print(m[20:39])
# elif a == 3:
#     print(m[39:61])
# elif a == 4:
#     print(m[61:71])
# elif a == 5:
#     print(m[71:102])
# elif a == 6:
#     print(m[102:114])
# else:
#     print('Пункт не найден')

# 4.5
string_1 = input('Введите первую строку: ')
string_2 = input('Введите вторую строку: ')
print(len(string_1))
print(len(string_2))
if string_1.lower() < string_2.lower():
    print('-1')
elif string_2.lower() < string_1.lower():
    print('1')
elif string_1.lower() == string_2.lower():
    print('0')
