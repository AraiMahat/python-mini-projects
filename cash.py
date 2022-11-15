# price = int(input())
# ves = int(input())
# cash = int(input())
# money = cash - (ves * price)
# print(money)

##############
# s = input()
# print((s + '\n') * 3)
###########
# name = input()
# price = int(input())
# ves = int(input())
# cash = int(input())
#
# print(f"Чек \n\
# {name} - {ves}кг - {price}руб/кг \n\
# Итого: {price * ves}руб \n\
# Внесено: {cash}руб \n\
# Сдача: {cash - price * ves}руб")
###########
# n = int(input())
# print(('Купи слона!\n') * n)
############
# name = input()
# num = int(input())
#
# print(f"Группа №{num // 100}.\n\
# {num % 10}. Ванечка.\n\
# Шкафчик: {num}.\n\
# Кроватка: {num // 10 % 10}.")

########
# num = int(input())
# n1 = num // 1000
# n2 = num // 100 % 10
# n3 = num // 10 % 10
# n4 = num % 10
#
# print(n2, n1, n4, n3, sep='')


#####


# a, b = int(input()), int(input())
# a1 = a // 100
# a2 = a // 10 % 10
# a3 = a % 10
#
# b1 = b // 100
# b2 = b // 10 % 10
# b3 = b % 10
#
# n1 = (a1 + b1) % 10
# n2 = (a2 + b2) % 10
# n3 = (a3 + b3) % 10
#
# print(n1, n2, n3, sep='')

#######

#
# kids, candy = int(input()), int(input())
# print(candy // kids, candy % kids, sep='\n')

#####

# red, green, blue = int(input()), int(input()), int(input())
# print(red + blue + 1)

######
# n, m , t = int(input()), int(input()), int(input())
# t1 = t // 60
# t2 = t % 60
# v3 = (m + t2) % 60
# v2 = (m + t2) // 60
# v1 = (n + t1) % 24
# if v1+v2 < 10 and v3 < 10:
#     print(f'0{v1+v2}:0{v3}')
# elif v1+v2 < 10:
#     print(f'0{v1+v2}:{v3}')
# elif v3 < 10:
#     print(f'{v1+v2}:0{v3}')
# else:
#     print(f'{v1+v2}:{v3}')

##########
# a, b, c = int(input()), int(input()), int(input())
# print((b-a)/c)

#####
# print(int('1101', 2))

#####
# a, b = input(), int(input())
# print(b % int(a, 2))

######
# name, price, ves, cash = input(), int(input()), int(input()), int(input())
# print("=" * 16 + 'Чек' + "=" * 15)
# print(f'Товар: {name}\n\
# Цена: {ves}кг * {price}руб/кг\n\
# Итого: {ves * price}руб\n\
# Внесено: {cash}руб\n\
# Сдача: {cash - ves * price}руб')
# print('=' * 35)

# n, m , t = int(input()), int(input()), int(input())
# t1 = t // 60
# t2 = t % 60
# v3 = (m + t2) % 60
# v2 = (m + t2) // 60
# v1 = (n + t1) % 24
# print(str(v1+v2).zfill(2)+':'+str(v3).zfill(2))


######

n, m, k1, k2 = int(input()), int(input()), int(input()), int(input())
v2 = n * (k1 - m)/(k1 - k2)
v1 = n - v2
print(v1, v2)