# print('Как Вас зовут?')
# name = input()
# print(f'Здравствуйте, {name}!')
# print('Как дела?')
# answer = input()
# if answer == 'хорошо':
#     print('Я за вас рада!')
# else:
#     print('Всё наладится!')
###################
# a, b, c = int(input()), int(input()), int(input())
# if a > b and a > c:
#     print('Петя')
# elif b > a and b > c:
#     print('Вася')
# elif c > a and c > b:
#     print('Толя')
###################
# a, b, c = int(input()), int(input()), int(input())
# max = max(a, b, c)
# min = min(a, b, c)
# if a != max and a != min:
#     print(f'1.{max}\n2.{a}\n3.{min}')
# if b != max and b != min:
#     print(f'1.{max}\n2.{b}\n3.{min}')
# if c != max and c != min:
#     print(f'1.{max}\n2.{c}\n3.{min}')
####################
# a, b, c = int(input()), int(input()), int(input())
# if a > b > c:
#     print('1.Петя\n2.Вася\n3.Толя')
# elif b > c > a:
#     print('1.Вася\n2.Толя\n3.Петя')
# elif c > a > b:
#     print('1.Толя\n2.Петя\n3.Вася')
######################
# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')
####################
# f, s, t = input(), input(), input()
# if f < s and f < t:
#     print(f)
# elif s < f and s < t:
#     print(s)
# else:
#     print(t)
#######################3
# n = int(input())
# n1 = n // 100
# n2 = n // 10 % 10
# n3 = n % 10
# a = n2 + n3
# b = n1 + n2
# if a > b:
#     print(a, b, sep='')
# else:
#     print(b, a, sep='')
###############
# n = 123
# # n1 = n // 100
# # n2 = n // 10 % 10
# # n3 = n % 10
# # maximum = max(n1, n2, n3)
# # minimum = min(n1, n2, n3)
# # summa = maximum + minimum
# # if n1 != maximum and n1 != minimum:
# #     sr = n1
# # elif n2 != maximum and n2 != minimum:
# #     sr = n2
# # else:
# #     sr = n3
# # if summa == sr * 2:
# #     print('YES')
# # else:
# #     print('NO')
#########################
# a, b, c = int(input()), int(input()), int(input())
# # if a + b > c and a + c > b and c + b > a:
# #     print('YES')
# # else:
# #     print('NO')
###########################
# e, g, h = int(input()), int(input()), int(input())
# e1 = e // 10
# e2 = e % 10
# g1 = g // 10
# g2 = g % 10
# h1 = h // 10
# h2 = h % 10
# if e1 == g1 == h1:
#     print(e1)
# elif e2 == g2 == h2:
#     print(e2)
#############################
# n = int(input())
# li = []
# for i in range(n):
#     num = int(input())
#     li.append(num)
# print(li)
##########################
# n = int(input())
# n1 = n // 100
# n2 = n // 10 % 10
# n3 = n % 10
# a1 = str(n1) + str(n2)
# a2 = str(n2) + str(n3)
# a3 = str(n3) + str(n1)
# minimum = min(int(a1), int(a2), int(a3))
# maximum = max(int(a1), int(a2), int(a3))
# if minimum????????????
#################
# print('Как Вас зовут?')
# name = input()
# print('Здравствуйте, '+ name + '!')
# print('Как дела?')
# answer = input()
# if answer == 'хорошо':
#     print('Я за вас рада!')
# else:
#     print('Всё наладится!')
#####################
# a, b = int(input()), int(input())
# a1 = a // 10
# a2 = a % 10
# b1 = b // 10
# b2 = b % 10
# maximum = max(a1, a2, b1, b2)
# minimum = min(a1, a2, b1, b2)
# print(maximum, minimum, sep='')
#####################
# a, b, c = float(input()), float(input()), float(input())
# d = b ** 2 - 4 * a * c
# if d > 0:
#     x1 = (-b - d ** 0.5) / 2 * a
#     x2 = (-b + d ** 0.5) / 2 * a
#     print(min(x1, x2).zfill(4), max(x1, x2))
# elif d == 0:
#     x1 = -b / 2 * a
#     print(x1)
# elif d < 0:
#     print('No solution')
# else:
#     print('Infinite solutions')
####################
# for i in range(3):
#     s = input()
#     if s == 'Три!':
#         print('Ёлочка, гори!')
#     else:
#         print('Режим ожидания...')
##############
# n = 103
# n1 = n // 10
# n2 = n % 10
# print(n1, n2)
#############
# a, c, b = int(input()), int(input()), int(input())
# minimum = min(a, b, c)
# maximum = max(a, b, c)
# sr = (a + b + c) - minimum - maximum
# if maximum ** 2 == minimum ** 2 + sr ** 2:
#     print('100%')
# elif maximum ** 2 < minimum ** 2 + sr ** 2:
#     print('крайне мала')
# elif maximum ** 2 > minimum ** 2 + sr ** 2:
#     print('велика')
###############
# s1, s2, s3 = input(), input(), input()
# len1 = 0
# len2 = 0
# len3 = 0
# if 'зайка' in s1:
#     len1 = len(s1)
# elif 'зайка' in s2:
#     len2 = len(s2)
# elif 'зайка' in s3:
#     len3 = len(s3)
# print(min(len1, len2, len3))
##########
# n = 103
# a = n // 100
# b = n // 10 % 10
# c = n % 10
# minimum = 0
# maximum = 0
# if a != 0:
#     n1 = a * 10 + b
#     n3 = a * 10 + c
#     minimum = min(n1, n3)
#     maximum = max(n1, n3)
# elif b != 0:
#     n2 = b * 10 + c
#     n6 = b * 10 + a
#     minimum = min(n2, n6)
#     maximum = max(n2, n6)
# elif c != 0:
#     n4 = c * 10 + a
#     n5 = c * 10 + b
#     minimum = min(n4, n5)
#     maximum = max(n4, n5)
# print(minimum, maximum)