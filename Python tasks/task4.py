#Поиск максимумов
# l = [[2,4,6],
#      [3,6,8],
#      [1,7,2]
#      ]
# l2 = []
# max1 = l[0][0]
#
# for i in range(len(l)):
#     max1 = l[i][0]
#     for j in range(len(l[i])):
#         if l[i][j] > max1:
#             max1 = l[i][j]
#     l2.append(max1)
# for i in range(len(l)):
#     max1 = l[0][i]
#     for j in range(len(l[i])):
#         if l[j][i] > max1:
#             max1 = l[j][i]
#     l2.append(max1)
# #
# for i in range(len(l)):
#     if l[i][i] > l[0][0]:
#         l2.append(l[i][i])
# for i in range(len(l)):
#     if l[i][len(l)-1-i] > l[0][len(l) - 1 - i]:
#         l2.append(l[i][len(l) - 1 - i])
# print(l2)

#1.13
# n = int(input('Вместимость рюкзака: '))
# v = []
#
# while n > sum(v):
#     v.append(int(input('Объем вещи: ')))
# print('Довольно!', sum(v), len(v), sep='\n')

#2.11
# w = 'Atlanta'
# a = 0
# while a < len(w):
#     if w[a] in ['a', 'e']:
#         print('Ага! Нашлась')
#         break
#     print(f'Текущая буква: {w[a]}')
#     a += 1

n = int(input('Number: '))
k = 0
d = 0
for i in range(n+1,n*2):
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            d += 1
            break
    if d == 0:
        k += 1
    d = 0
print(k)



