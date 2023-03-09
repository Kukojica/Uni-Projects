import math
#Math
# №1
def sq_root(a, b, c):
    if a == 0:
        a = 1
    elif b == 0:
        b = 1
    elif c == 0:
        c =1
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        x1 = round((-b + math.sqrt(d)) / (2 * a), 1)
        x2 = round((-b - math.sqrt(d)) / (2 * a), 1)
    print(f'Корни квадратного уравнения: x1 = {x1}, x2 = {x2}')
sq_root(3, -7, 4)

# №2
def r_area(r):
    area = math.pi * (r**2)
    print(f'Площадь круга равна - {round(area, 1)}')
r_area(6)

#Counter
from collections import Counter
array = [1, 5, 4, 14, 5, 7, 89, 13, 4, 6, 26, 14, 56, 3, 1]
count = []
for key, value in Counter(array).items():
    if value == 2:
        count.append(key)
print(f'Элемент, который встречается 2 раза - {count}')

n = int(input())
c = 0
while c < n:
    a = [int(i) for i in input().split()]
    c = len(a)
counter = Counter(a)
result = a[0]
max_count = counter[result]
for number, count in counter.items():
    if count > max_count or (count == max_count and number > result):
        result = number
        max_count = count
print(f'Наибольшее число, которое чаще других встречается в массиве - {result}')

#itertools
import itertools
k = 0
a = list(itertools.product('атом', repeat=5))
for i in a:
    if i.count('м') == 1:
        k += 1
print(f'Количество кодовых слов - {k}')

n = list(itertools.permutations('небо'))
print(f'Количество вариантов слов - {len(n)}')
#Cycle
def infinite(lst, iterations):
    result = ''
    iter_lst = itertools.cycle(lst)
    if lst:
        for symbol in range(iterations):
            result += str(next(iter_lst))
    return result
print(infinite([2, 5, 8], 7))
print(infinite([], 1000))
print(infinite([7], 4))

#JSON
import json
path = 'C:/Users/redlo/Desktop/lab/books.json'
with open(path, 'r') as f:
    data = json.load(f)
book_list = []
for book in data:
    if book['pageCount'] > 500:
        book_list.append(book['title'])
print('Названия книг с количеством страниц более 500 - {}'.format('\n'.join(book_list)))

#CSV
import csv
path = 'C:/Users/redlo/Desktop/lab/freshman_kgs.csv'
with (open(path, newline='') as input,
      open('output.csv', 'w', newline='') as output):
    reader = csv.DictReader(input)
    writer = csv.DictWriter(output, fieldnames=['Sex',
                                                ' "Weight (Sep)"',
                                                ' "Weight (Apr)"',
                                                ' "BMI (Sep)"',
                                                ' "BMI (Apr)"',
                                                'WeightDif'])
    writer.writeheader()
    for row in reader:
        dif = int(row[' "Weight (Sep)"']) - int(row[' "Weight (Apr)"'])
        writer.writerow({'Sex' : row['Sex'],
                         ' "Weight (Sep)"': row[' "Weight (Sep)"'],
                         ' "Weight (Apr)"' : row[' "Weight (Apr)"'],
                         ' "BMI (Sep)"' : row[' "BMI (Sep)"'],
                         ' "BMI (Apr)"' : row[' "BMI (Apr)"'],
                         'WeightDif': dif})
with open('output.csv') as f:
    reader = csv.DictReader(f)
    s = []
    for i in reader:
        if int(i['WeightDif']) > 0 and i['Sex'] == 'M' and float(i[' "BMI (Apr)"']) > 20:
            s.append(i)
    print(f'Строки соответсвующие условиям - {s}')

path = 'C:/Users/redlo/Desktop/lab/homes.csv'
with open(path, 'r') as homes, \
    open('out.csv', 'w', newline='') as out:
    reader = csv.DictReader(homes)

    writer = csv.DictWriter(out, fieldnames=['Sell',
                                                ' "List"',
                                                ' "Living"',
                                                ' "Rooms"',
                                                ' "Beds"',
                                                ' "Baths"',
                                                ' "Age"',
                                                ' "Acres"',
                                                ' "Taxes"',
                                                'Search'])
    writer.writeheader()
    for row in reader:
        if row['Sell'] != ' ' and int(row['Sell']) > 180 and int(row[' "Taxes"']) < 3500:
            row['Search'] = 'True'
        else:
            row['Search'] = 'False'
        writer.writerow(row)
with open(path, 'r') as homes1:
    reader = csv.DictReader(homes1)
    c = 0
    l = []
    for i in reader:
        if i[' "Rooms"'] == '  8':
            c += 1
            l.append(int(i['Sell']))
    print(f'Общее число домов с 8 комнатами - {c}')
    print(f'Общая стоимость домов с 8 комнатами в тысячах долларов - {sum(l)}')
    print(f'Средняя стоимость дома с 8 комнатами в тысячах долларов - {round(sum(l) / c, 2)}')

with open('out.csv') as f:
    reader = csv.DictReader(f)
    for i in reader:
        if i['Search'] == 'True':
            print(f'Дом, подподающий под условие - {i}')