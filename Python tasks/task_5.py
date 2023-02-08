def find_ch(st):
    f = st.lower().find(letter)
    return f

letter = 'g'
print(find_ch('FlaminGo'))


# import re
# def email_check():
#     st = input('Enter email: ')
#     if re.fullmatch('[\S]+@[\S]+.[\S]+',st):
#         print('yes')
#     else:
#         print('no')
#
# email_check()

import random
l = []

def fill_list(lst, r, a, b):
    for i in range(r):
        lst.append(random.randint(a, b))
    return lst

print(fill_list(l, 10, 1, 20))