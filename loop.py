# count = 0
# while (s := input()) != 'Приехали!':
#     if 'зайка' in s:
#         count += 1
# print(count)
###########
# k, n = int(input()), int(input())
# for i in range(k, n + 1):
#     print(i, end=' ')
###########
# k, n = int(input()), int(input())
# print(k, end=' ')
# for i in range(k+1, n):
#     print(i, end=' ')
# print(n, end=' ')
###############
# summa = 0
# while (cash := int(input())) != 0:
#     if cash >= 500:
#         sale = cash * 0.1
#         cash -= sale
#     summa += cash
# print(summa)
##############
# summa = 0
# while (cash := float(input())) != 0:
#     if cash >= 500:
#         sale = cash * 0.1
#         cash -= sale
#     summa += cash
# print(summa)
###############
# a, b = 108, 72
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# print(a + b)
##################
# a, b = 12, 42
# m = a * b
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# print(m // (a + b))
########
# f = 1
# for i in range(3):
#     f = f * (i + 1)
# print(f)
###############
# n = input()
# k = int(input())
# x = 0
# y = 0
# while n != 'СТОП':
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
####################
# number = int(input())
# summa = 0
# for i in range(len(str(number))):
#     n = (number % 10 ** (i + 1)) // 10 ** i
#     summa += n
# print(summa)
###############
# number = int(input())
# maxi = 0
# for i in range(len(str(number))):
#     n = (number % 10 ** (i + 1)) // 10 ** i
#     if maxi < n:
#         maxi = n
# print(maxi)
#######################
# n = 1
# for i in range(2, n):
#     if n % i == 0:
#         print("NO")
#         break
# else:
#     print("YES")
#################
# n = int(input())
# count = 0
# for i in range(n):
#     s = input()
#     if 'зайка' in s:
#         count += 1
# print(count)
##################
# n = int(input())
# for i in range(len(str(n))):
#     n1 = (n % 10 ** (i + 1)) // 10 ** i
#
#     if n1 == n2:
#         print('YES')
#     else:
#         print('NO')
########################
# num = 123407
# res, power = 0, 1
#
# while num:
#     last_digit = num % 10
#     if last_digit % 2 == 1:
#         res += last_digit * power
#         power *= 10
#
#     num = num // 10
#
# print(res)
############
# n, m, k1, k2 = 32, 285, 300, 240
# v2 = n * (k1 - m)/(k1 - k2)
# v1 = n - v2
# print(v1, v2)
############
# num = 1234
# for i in range(len(str(num))):
#     last_digit = num % 10
#     num = num // 1000
#     if first_digit == last_digit:
#         print("YES")
#     num //= 10
# else:
#     print("NO")
############
# n, m, k1, k2 = 32, 285, 300, 240
# v2 = n * (k1 - m)//(k1 - k2)
# v1 = n - v2
# print(v1, v2)
###############
# n = 98
# k = 2
# while n != 1:
#     if n % k == 0:
#         n = int(n / k)
#         print(k, end=' * ')
#     else:
#         k += 1
# ########################
# guess = int(input())
# num = int(input())
# while num != guess:
#     if num > guess:
#         print('Меньше')
#     elif num < guess:
#         print('Больше')
#     num = int(input())
# print('Угадал!')
