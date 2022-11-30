# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(i * j, end=" ")
#     print('')
#################
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(j, '*', i, '=', j * i, end='\n')
##################
# n = int(input())
# a = 0
# b = 1
# for i in range(5):
#     print(end=" \n ")
#     for j in range(b):
#         a = a + 1
#         print(a, end="")
#     b = b + 1
# ###################
# name, price, ves, cash = input(), int(input()), int(input()), int(input())
# print("=" * 16 + 'Чек' + "=" * 15)
# print(f'Товар: {name}\n\
# Цена: {ves}кг * {price}руб/кг\n\
# Итого: {ves * price}руб\n\
# Внесено: {cash}руб\n\
# Сдача: {cash - ves * price}руб')
# print('=' * 35)
#####################
# a, b, c = int(input()), int(input()), int(input())
# p = 'Петя'
# v = 'Вася'
# t = 'Толя'
# if a > b and a > c:
#     if b > c:
#         print(f'{p:8f}')
#         print(f'1. {p}\n2. {v}\n3. {t}')
#     else:
#         print(f'1. {p}\n2. {t}\n3. {v}')
# if b > a and b > c:
#     if c > a:
#         print(f'1. {v}\n2. {t}\n3. {p}')
#     else:
#         print(f'1. {v}\n2. {p}\n3. {t}')
# if c > a and c > b:
#     if a > b:
#         print(f'1. {t}\n2. {p}\n3. {v}')
#     else:
#         print(f'1. {t}\n2. {v}\n3. {p}')
####################
# n = 787
# a = n // 100
# b = n // 10 % 10
# c = n % 10
# if a > c:
#     a, c = c, a
# if a > b:
#     a, b = b, a
# if b > c:
#     b, c = c, b
# if a == 0:
#     n1 = b * 10 + a
# else:
#     n1 = a * 10 + b
# n2 = c * 10 + b
# print(n1, n2)
###################
# while (s := input()) != 'Три!':
#     print('Режим ожидания...')
# else:
#     print('Ёлочка, гори!')
#######################
# k, n = int(input()), int(input())
# for i in range(k, n + 1):
#     print(i, end=' ')

################
# n = 1
# for i in range(2, n // 2 + 1):
#     if n % i == 0:
#         print("NO")
#         break
# else:
#     print("YES")
############
# n1 = 31
# n2 = 11
# a = n1 // 10
# b = n1 % 10
# c = n2 // 10
# d = n2 % 10
# if a > d:
#     a, d = d, a
# if a > c:
#     a, c = c, a
# if a > b:
#     a, b = b, a
# if b > c:
#     b, c = c, b
# if b > d:
#     b, d = d, b
# if c > d:
#     c, d = d, c
# sr = (b + c) % 10
# n = d * 100 + sr * 10 + a
# print(n)
########################
# a, b, c = float(input()), float(input()), float(input())
# d = b ** 2 - 4 * a * c
# if a == 0 or b == 0 or c == 0:
#     print('Infinite solutions')
# else:
#     if d > 0:
#         x1 = (-b - d ** 0.5) / (2 * a)
#         x2 = (-b + d ** 0.5) / (2 * a)
#         print(f'{min(x1, x2):.2f}', f'{max(x1, x2):.2f}')
#     elif d == 0:
#         x1 = -b / 2 * a
#         print(f'{x1:.2f}')
#     elif d < 0:
#         print('No solution')
###################
# k, n = int(input()), int(input())
# if k < n:
#     for i in range(k, n + 1):
#         print(i, end=' ')
# else:
#     for i in range(k, n - 1, -1):
#         print(i, end=' ')
####################
# x = 0
# y = 0
# while (n := input()) != 'СТОП':
#     k = int(input())
#     if n == 'СЕВЕР':
#         x += k
#     elif n == 'ВОСТОК':
#         y += k
#     elif n == 'ЮГ':
#         x -= k
#     elif n == 'ЗАПАД':
#         y -= k
# print(x)
# print(y)
##################
# n = int(input())
# k = 2
# while n != 1:
#     if n % k == 0:
#         n = int(n / k)
#         print(k, end=' * ')
#     else:
#         k += 1
##############
# n = int(input())
# summa = 0
# for i in range(n):
#     num = int(input())
#     summa += num
#     while num > 9:
#
# print(summa)
#############
# num = int(input())
# n = num + num
# n = n * num
# n = n - num
# n = n // num
# print(n)
############
# def add_hello(s: str) -> str:
#     return s[:5] + " hello" + s[4:]
#
#
# print(add_hello('This is the first test'))
#####################
# def second_is_a(s: str) -> str:
#     return s[:1] + 'A' + s[2:]
#
#
# print(second_is_a('tttt'))
################
# def format_str(letters: str, f: str) -> str:
#     letters = letters.lower()
#     for i in range(len(f)):
#         if f[i].isupper():
#             letters = letters.replace(letters[i], letters[i].upper())
#     return letters
#
#
# print(format_str('aBcDe', 'Xxxxx!'))
# print(format_str('helloworld', 'Xxxxx, xxxxx!'))
##############
# def more_spaces(s: str) -> str:
#     s = " ".join(s)
#     for i in s:
#         if i == ' ':
#             count += 1
#     print(count)
#     return s
#
# print(more_spaces('Hello, world!'))
#############
# halls, capacity, viewers = int(input()), int(input()), int(input())
# print(halls * capacity >= viewers)
##############
# def odd_num(a, b):
#     if a / b % 2 != 0:
#         return True
#     else:
#         return False
#
#
# x, y = int(input()), int(input())
# print(odd_num(x, y))
#############
# number = int(input())
# if number > 0:
#     print(-number)
# else:
#     print(-number)
#################
# unit = int(input())
# if unit < 1:
#     print('no army')
# elif 1 <= unit <= 9:
#     print('few')
# elif 10 <= unit <= 49:
#     print('pack')
# elif 50 <= unit <= 499:
#     print('swarm')
# elif 500 <= unit <= 999:
#     print('swarm')
# else:
#     print('legion')
###
# def normalize(name):
#     new_name = ""
#     old = ["é", "ë", "á", "å", "œ", "æ"]
#     new = ["e", "e", "a", "aa", "oe", "ae"]
#
#     for letter in name:
#         if letter in old:
#             new_name += new[old.index(letter)]
#         else:
#             new_name += letter
#
#     return new_name
#
#
# print(normalize('Charlotte Brontë'))
####
# dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
#               'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
#               'sign', 'the', 'to', 'uncertain']
# sentence = input().split()
# errors = []
# for word in sentence:
#     if word not in dictionary:
#         errors.append(word)
# if errors:
#     print('\n'.join(errors))
# else:
#     print("OK")
###############
# put your python code here
# grades = input().split()
# count_a = 0
# total = 0
# for grade in grades:
#     total += 1
#     if grade == 'A':
#         count_a += 1
# print(round(count_a / total, 2))
################
# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation." \
        " You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."


def equation():
    print(msg_0)
    x, op, y = input().split()
    while True:
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_1)
            equation()
        except TypeError:
            print(msg_2)
            equation()
        else:
            if op not in ["+", "-", "*", "/"]:
                print(msg_2)
                break


equation()
