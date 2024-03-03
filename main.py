import random

# a = 30
# b = "Hello"
# c = 2.8
# print(type(a))
# print(type(c))
# print(type(b))

# a = 5
# print(a, type(a))
# a = "Hello"
# print(a, type(a))

# a = 5
# print(a, id(a))
# b = 4
# print(b, id(b))
# a = b
# print(a, id(a))

# a = 21
# b = 512
# a, b = b, a
# print("a:", a)
# print("b:", b)
#
# print("строка символов")
# print('строка символов')

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!"
# print(s1 + ", " + s2 + "!")
# print(s3 * 5)


# num = 4321  # 43
# print(num)
# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d:", d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# print(num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10
# print(res)

# num1 = "2.5"
# num2 = 3
# res = float(num1) + num2
# print(res)

# print(int(2.5))
# print(round(2.8))

# name = "Виктор"

# name = input("Введите имя: ")
# print("Hello,", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
#
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# print("Введите четыре числа: ")
# num1 = int(input("1: "))
# num2 = int(input("2: "))
# num3 = int(input("3: "))
# num4 = int(input("4: "))
# print("Результат: ", round((num1+num2)/(num3+num4), 2))

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)


# print(bool("python"))

# test = None
# print(test)

# ont = 5
# if ont < 10:
#     ont += 1
#     print(ont)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ есть")
# else:
#     print("Доступа нет")


# a = 25
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")






# day = int(input("Введите день недели (цифрой): "))
# if (day >= 1) and (day <= 5):
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
#
# elif day == 6 or day == 7:
#     print("Выходной день")
# else:
#     print("Такого дня недели не существует")


# mounth = int(input("Введите номер месяца (цифрой): "))
# if mounth >= 1 or mounth <= 2 or mounth == 12:
#     print("Зима")
# if mounth >= 3 or mounth <= 5:
#     print("Весна")

# a = int(input("Введите номер месяца: "))
# if 1 <= a <= 12:
#     if 3 <= a <= 5:
#         print("Весна")
#     elif 6 <= a <= 8:
#         print("Лето")
#     elif 9 <= a <= 11:
#         print("Осень")
#     else:
#         print("Зима")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите кол-во ворон:"))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
#
# else:
#     print("Ошибка ввода данных")

# password = "admin"

# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Такого значения нет")

# day = "суббота"
# time = 17
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# # minim = a if a < b else b
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 20, 0
# print('на ноль делить нельзя' if b== 0 else a/b)

# try:
#     n = int(input("Введите целое число:"))
#     print(n * 2)
# except ValueError:
#     print("Что-то пощло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else:
#     print("Все ок")
# finally:
#     print("Конец программы")

# try:
#     n = int(input("Введите первое число: "))
#     m = int(input("Введите второе число: "))
#     print(n + m)

# try:
#     a = input("Введите 1 число: ")
#     b = input("Введите 2 число: ")
# except (ValueError, ZeroDivisionError, NameError):
#     print(a + b)
# else:
#     num = int(a) + int(b)
#     print(num)

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + str(m))


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#      print("i =", i)
#     i += 1

# n = int(input("Укажите количество символов: "))
# print(n * "*\n")

# i = 0
# while i < n:
#     print("*")
#     i += 1

# n = int(input("Введите начало диапозона: "))
# m = int(input("Введите конец диапозона: "))
# sum1 = 0
# while n <= m:
#     if n % 2:
#        # print(n, end=" ")
#       sum1 += n
#     n += 1
#     print(sum1)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
#
# else:
#     print("Нечетное: ")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
#     print("\nЦикл завершен!")

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i +=1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 15:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1
# print()

# i = 0
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1

# for element in collection:
#     print(element)

# for i in "Hello!":
#     print(i)
#
# for color in "red", "blue", "green":
#     print(color)

# print(range(2, 9, 2))
# range(start, stop, step)

# for i in range(100, 0, -10):
#     print(i, end=" ")
#
# print()
#
# i = 100
# while i > 0:
#     print(i, end=" ")
#     i -= 10

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     # if i % 11 == 0:
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
# else:
#     print("Конец цикла")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")
# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите длину прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end="")
#     print()

# d = [i for i in "Hello"]
# print(d)
#
# num = [i for i in range(10) if i % 2 == 0]
# print(num)

# Список (list)

# nums = [8, 3, 4, 7, "Hello", True]
# print(nums)
# # print(type(nums))
# # print(nums[-2])
# # print(nums[5])
# nums[1] = 256
# nums[2] += 100
# print(nums)
# for i in nums:
#     print(i)
# print(len(nums))

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#     print(a)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# res = 0
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(len(a)):
#     if a[i] < 0:
#         res += a[i]
# print(res)

# s = list(range(10, 100, 10))
# print(s)
#
# for i in range(len(s)):
#     print(s[i], end=" ")
# print()
# for i in s:
#     print(i, end=" ")

# n = list(range(21, 41))
# print(n)

# count = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         s += n[i]

# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print("Количество четных элементов списка: ", count)
# print("Сумма нечетных элементов списка: ", s)

# n = list(range(21, 41, 3))
# print(n)
#
# a = 2
# print(n[a])
# print(n[a - 1])

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(len(a)):
#     # if a[i + 1] > a[i]:
#     if a[i] > a[i - 1]:
#         print(a[i])

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = count = 0
# for i in range(len(a)):
#     s += a[i]
#     if a[i] != 0:
#         count += 1
# print(s / count)

# a = [7, 9, 2, 1, 17]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# print(s[1:3])
# print(s[5:0:-1])
# print(s[::-1])
# print(s[::-1], id(s[::-1]))
# print(s[6:22], id(s[6:22]))

# lst = list(range(1, 8))
# print(lst[:])
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[6:])
# print(lst[3:4])
# print(lst[4:1:-1])

# Методы списков dir(list)
# s = [9, 5, 6, 3, 7, 4]
# print(s)
# s.append(8)
# # s.append(s)
# s.extend([20, 1, 2])
# s.extend("add")
# print(s)
# s.insert(3, 100)
# print(s)

# s = []
# n = int(input("Введите кол-во элементов списка: "))
# for _ in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for i in a:
#     for j in b:
#         # if i in c:
#         #     continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
#
# s = []
# for el in a:
#     if el in b and el not in s:
#         s.append(el)
# print(s)

# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# t = a.remove(9)  # удаляет элемент по значению
# print(a)
# last = a.pop()  # удаляет последний элемент из списка и возвращает удаленный элемент
# print(last)
# second = a.pop(0)  # удаляет элемент по индексу
# print(second)
# print(a)
# a.clear() # очищает список

# num = a.count(9) # кол-во заданных значений в списке
# print(num)
# ind = a.index(9) # возвращает индекс элемента по заданному списку
# print(ind)
# ind2 = a.index(9, 2)
# print(ind2)

# num = 17
# if num in a:
#     print(a.index(num))

# a.reverse()


# a = [1, 2, 3]
# b = a.copy()
# print("a = ", a)
# print("b = ", b)
# a.append(4)
# b.append(120)
# print("a = ", a)
# print("b = ", b)

# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# a.sort() # сортировка элементов списка по возрастанию
# a.sort(reverse=True) # сортировка элементов списка по убыванию
# print(a)

# s = ("Виталий", "Сергей", "Анна", "Антон", "Александр")
# print(s)
#
# s.sort(key=len, reverse=True)
# print(s)

# lst = sorted(s, key=len, reverse=True)
# print(lst)
# print(s)
# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(0, 9)) #  9 - включительно
# print(random.randrange(3, 9, 2)) # 9 - не включительно
# print(round(random.uniform(10.5, 25.5), 2))

# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# # random.shuffle(s)
# print(random.choice(s))
# print(random.choices(s, k=3))

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)


# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# res = 0
# for i in s:
#     res = res + i
# print(res)
# print(len(s))
# print(sum(s))
# print(max(s))
# print(min(s))

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# mux = max(lst)
# print("Max: ", mux)
# lst.remove(mux)
# lst.insert(0, mux)
# print(lst)

# lst = []
# if not lst:
#     print("Список пустой")
# print(bool(lst))

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for i in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print(c)
# c = [min(a), min(b), max(a), max(b)]
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print(c)
# n1 = 10
# a = [random.randint(0, 10) for i in range(n1)]
# a = []
# while len(a) != n1:
#     n = random.randrange(n1) # от 0 до 10
#     if n not in a:
#         a.append(n)
# print(a)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [10, 11, 12, 13]
# ]
# print(m, end="\n\n")
#
# for row in range(len(m)):  # 0 1 2
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
    # print(row)
    # for x in row:
    #     print(x, end="\t\t")
    # print()
# print(len(n))
# print(n[1][2])

# s = ["Hello", "World"]
# print(s[1][0])

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [10, 11, 12, 13]
# ]
# for row in m:
#     # print(row)
#     for x in row:
#         print(x ** 2, end="\t\t")
#     print()

# w, h = 5, 3
# matrix = [[random.randint(1, 20) for x in range(w)] for y in range(h)]
# matrix = [[0 for x in range(w)] for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#         matrix.append(new_row)


# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# import math
#
# num1 = math.sqrt(4)
# num2 = math.pi
# num3 = math.ceil(3.2)
# num4 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# import math as m
#
#
# num3 = m.ceil(3.2)
# num4 = m.floor(3.8)
#
#
# print(num3)
# print(num4)

# from math import *
#
#
# num3 = ceil(3.2)
# num4 = floor(3.8)
#
#
# print(num3)
# print(num4)

# from math import pi
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * radius, 2))

import time
import locale

locale.setlocale(locale.LC_ALL, "ru")

# second = time.time()
# print(second)
# s = 1557045478
#
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
# print(res)

# print(time.strftime("%d/%m/%Y, %H.%M.%S", time.localtime(s)))
# print(time.strftime("Сегодня: %B %d, %Y, %A"))
# start = time.monotonic()
# pause = 5
# print("Программа запущена:...")
# time.sleep(pause)
# print("Пауза была", pause, "секунд")
# finish = time.monotonic()
# res = finish - start
# print(res)

# Функции
# print()

# def hello(name, age):
#     print("Мне", age, "меня зовут", name)
#
#
# hello("Irina", 28)
# hello("Igor", 19)

# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))

# def change(lst):
    # lst[0], lst[-1] = lst[-1], lst[0]
#     end = lst.pop()
#     start = lst.pop(0)
#
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def check_password(password):
#     has_lower = False
#     has_upper = False
#     has_num = False
#
#     for ch in password:
#         if "a" <= ch <= "z":  # 97 <= 107 <= 122
#             has_lower = True
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_lower and has_upper and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b +c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def set_param(c=20, s="-"):
#     print(s * c, end="")
#     print()
#
#
# set_param()
# set_param(7)
# set_param(20, "#")
# set_param(15, "+")
# set_param(10, "*")
# set_param( s="*", c=10)


# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))



# def display_info(name, age):
#     print("Name: ", name, "\nAge", age)
#
#
# display_info("Irina", 23)
# display_info(age=23, name="Irina")
# display_info("Igor", age=23, name="Irina")


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
#
#
# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)


# lt1 = [1, 20, 3]
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))
# lt1[1] = 50
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))

# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = ()
# print(a, type(a))
#
# b = ()
# print(b, type(b))

# a = (5, 9, 7, 3, 4)
# print(a[1:3])
# print(a[-1])
# print(a[4])

# tpl = tuple(input("=> ") for i in range(5))
# print(tpl)
# tpl = tuple(randint(1, 100) for i in range(5))
# print(tpl)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# print(t3 * 2)
# t3.
# sym = "e"
# if sym in t3:
# # print(t3.count("l"))
#     print(t3.index(sym))
# else:
#     print("Такого символа нет")

# try:
#         print(t3.index(sym, 4, -2))
# except ValueError:
#         print("Такого символа нет в заданном диапазоне")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()

# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "hi"
# t[4].append("new")
# print(t, id(t))

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married

# first_name, year, married = get_user()
# first_name, year, married = user
# print(user[0])
# print(user[1])
# print(user[2])
# print(first_name, year, married)


# from random import randint
#
#
# def ren(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ren(0, 5)
# tpl2 = ren(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))


# name = "Igor"
#
# if name:
#     print("Name: ", name)
#     name = "Marina"
# else:
#     print("ELSE")
#
# print(name)

# for i in range(5):
#     print(i, end=" ")
#     name = "Marina"
#
# print()
# print(name)


# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst2 = list(tpl)
# print(lst2)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep=" ")


# Множество (set) - неупорядоченная коллекция, которая хранит только уникальные значения (изменяемый тип данных)

# s = {"red", "green", "blue"}
# print(type(s))
# print(s)
# print(len(s))
#
# for i in s:
#     print(i)

# a = set("hello")
# print(a, type(a))

# s = {x * x for x in range(10)}
# s = {input("-> ") for x in range(5)}
# s = {randint(20, 50) for x in range(10)}
# print(s)

# s = {"red", "green", "blue"}
# print("green" in s)
# print("green" not in s)

# lst = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# lt = [i for i in lst if 'a' in i]
# lt = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst]
# lt = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst
#       if i[1] == 'c']
# print(lt)

# s = {"red", "green", "blue"}
# print(s)
# s.add("black")
# print(s)
# s.remove("black")
# print(s)
# s.remove("pink")
# print(s)
# color = "pink"
# s.remove("pink")
# print(s)
# s.discard("blue")
# print(s)
# color = s.pop()
# print(s)
# print(color)
# s.clear()
# print(s)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a & b
# c = a - b
# c = a ^ b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobbies = drawing & music
# print(both_hobbies)
# drawing = drawing - both_hobbies
# print(drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)

# a = [1, 2, 5, 7, 9, 3, 2, 0, 6, 4, 2, 1, 8, 9, 4]
# print(a)
# s = set(a)
# print(s)
# a1 = list(s)
# print(a1)

# s = frozenset("Hello")
# print(s)

# Словари (dict)

# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# lst[1] = 200
# d["two"] = 200
# print(lst)
# print(d["two"])

# d = {}
# print(d, type(d))

# s1 = "test"
# s2 = "string"
# a = set(s1) | set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")


# d = {0: "text", "one": 45, (1, 2, 3): "Кортеж",
#      "список": [2, 3, 6, 7], True: 1, False: 0
#      }
# print(d)
#
# key = 45
#
# try:
#    del d[key]
# except KeyError:
#      print("Элемента с ключом " + str(key) + " нет в словаре")
#
#
# print(d)
# d["ne"] = "Новое значение"
# print(d)
#
# for key in d:
#      print(key, ":", d[key])
# print(d[(1, 2, 3)])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# a = 1
# for key in d:
#      a *= d[key]
# print(a)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#      '1': ['Core-i3-4330', 9, 4500],
#      '2': ['Core-i5-4670', 3, 8500],
#      '3': ['AMD FX-6300', 6, 3700],
#      '4': ['Pentium G3220', 8, 2100],
#      '5': ['Core-i5-3450', 5, 6400]
# }
#
# for i in goods:
#      print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ",
#            goods[i][2], " руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] = count
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
#
# for i in goods:
#      print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ",
#            goods[i][2], " руб.", sep="")

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# for key, value in d.items():
#      print(key, "=>", value)
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
#
# print("D =", d)
# print("D2 =", d2)
#
# d['b'] = 5
# d2['e'] = 7
# print("D =", d, id(d))
# print("D2 =", d2, id(d2))

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('b1', 'Такого ключа нет')
# print(value)
# item = d.setdefault('c')
# print(item)
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.pop('b')
# print(item)
# print(d)
# item2 = d.popitem()
# print(item2)
# print(d)
# d.clear()
# print(d)

# d = dict.fromkeys(['a', 'b'], 100)
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = [('r', 7), ('q', 9)]
# d2 = {'r': 7, 'q': 9}
# print(list(d2.items()))
# d.update(d2)
# d3 = d.copy()
# d3.update(d2)
# d |= d2
# print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
#
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
#
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print(d)
#
# d['location'] = d.pop('city')
#
# print(d)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# new_d = {key: value for key, value in d.items() if value <= 2}
# print(new_d)

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }
# print(sales)
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y])
#
# person = input("Имя продавца: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение:"))
# sales[person][region] = new_data
# print(sales[person])

# d = {
#     "emp1": {"name": "John", "salary":  7500},
#     "emp2": {"name": "Emma", "salary":  8000},
#     "emp3": {"name": "Brad", "salary":  6500},
# }
#
# print(d['emp3'])
# print(d['emp3']['salary'])
# d['emp3']['salary'] = 8500
#
#
# for i in d:
#     print(i)
#     for j in d[i]:
#         print("\t", j, ":", d[i][j])

# zip
# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = (2.9, 3.7, 9.2)
# # d = dict(zip(a, b))
# d = list(zip(a, b))
# print(d)
# one = {'name': "Igor", 'surname': 'Doe', 'job': 'Consul'}
# two = {'name': "Irina", 'surname': 'Smith', 'job':
#     'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

#
# a = (1, 2, 3)
# b = [*a, 4, 55, 6]
# print(len(b))
# print(b)

# first = {'one': 1, 'two': 2}
# second = {'three': 3, 'four': 4}
# print({**first, **second})
# for k, v in {**first, **second}.items():
#     print(k, "=>", v)

# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
# print()
# for num, val in enumerate(colors, 1):
#     print(num, ") ", val, sep="")

# studs = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[name] = point
#     # s += point
#
# s = sum(studs.values())
# avg = s / n
# print(studs)
# print(s)
# print("Средний балл: ", avg)
#
# for i in studs:
#     if studs[i] > avg:
#         print(i)

# def func(args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7, 8, "abc"))
# print(func())

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3))
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))

# def ch(*args):
#     avg = sum(args) / len(args)
#     print(avg)
#     res = []
#     for num in args:
#         if num < avg:
#             res.append(num)
#     return avg
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(1, 2, 3, 5, "abc"))

# def print_scores(student, *scores):
#     print("Student name: ", student, end=", Оценки: ")
#     for score in scores:
#         print(score, end=" ")
#         print()
#
#
# print_scores("Jon", 10, 2, 56, 78, 95)
# print_scores("Rick", 10, 22, 65, 87, 59)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(one="один"))

# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name="Irina", surname="Sharma", age=22)
# intro(name="Igor", surname="Wood", email="igor@mail.ru",
#       country="Russia", age=22)

# def func(a, b, *args, **kwargs):
#     return a, b, args, kwargs
#
#
# print(func(5, 1, 2, 3, 4, 5, 6, 7))

# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
# print("my_dict =", my_dict)
# db(k1=22, r2=31, k3=11, k4=91)
# print("my_dict =", my_dict)
# db(namt='Bob', age=31, weight=61, eyes_color='grey')
# print("my_dict =", my_dict)

# name = "Tom"


# def hi():
#     global name
#     name = "Sam"
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)


# hi()
# bye()
# print(name)

# sum = 5
#
# lst = [7, 8, 9, 3]
# print(sum(lst))

# def add(a):
#     x = 2
#
#     def outer():
#         x = 3
#         print("x =", x)
#         return a + x
#
#     return outer()
#     print(x)

# print(add(5))

# x = 25
# t = 0

# def fn():
#     global t
#     a = 38
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('a =', a)
#
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#
#         def fn3():
#             x = 55
#
#         fn3()
#          print("fn2.x", x)
#     fn2()
#     print("fn1.x", x)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))

# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# item1 = outer(5)
# print(item1(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a += 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
# func = func1()
# print(func())

# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
#
# res1()
# res1()
# res1()

# lambda - выражение

# print((lambda x, y: x + y)(1, 2))

# def func(x, y):
#     return x + y
#
# print(func(1, 2))

# print((lambda *args:args)(1, 2, 3, 4, 5, 6, 7, 8))
# print((lambda *args:args)(1, 2, 3))
# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
#
# print((lambda *args: args)(1, 2, 3, 4, 5, 6, 7, 8))
# print((lambda *args: args)(1, 2, 3))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for t in c:
#     print(t("abc_"))

# def inc1(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# func = inc1(10)
# print(func(5))
#
# def inc2(n):
#     return lambda x: n + x
#
# func2 = inc2(10)
# print(func2(5))
#
# inc3 = (lambda n: (lambda x: n + x))
# func3 = inc3(10)
# print(func3(5))
#
# print((lambda n: (lambda x: n + x))(10)(5))

# print((lambda n: (lambda x: (lambda z: n + x + z)))(2)(4)(6))

# def func(i):
#     return i[1]


# d = {'a': 15, 'c': 10, 'b': 5}
# # lst = sorted(d.items(), key=lambda i: i[1])  # [('a', 15), ('b', 5), ('c', 10)]
# lst = list(d.items())
# # print(lst)
# # lst.sort(key=lambda i: i[1])
# lst.sort(key=func)
# print(lst)
# print(dict(lst))

# players = [
#     {"name": "Антон", "last_name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last_name": "Бодня", "rating": 10},
#     {"name": "Федор", "last_name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last_name": "Семенов", "rating": 6},
# ]
#
# res = sorted(players, key=lambda item: item["last_name"])
# print(res)
# res1 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res1)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]
# print(a[1](8, 3))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[6]()
# from math import pi
#
# area = {
#     "Circle": lambda radius: pi * radius * radius,
#     "Rectangle": lambda a, b: a * b,
#     "Trapezoid": lambda a, b, h: (a + b) * h / 2
# }
# print("Площадь окружности:", area["Circle"](2))
# print("Площадь прямоугольника:", area["Rectangle"](10, 13))
# print("Площадь трапеции:", area["Trapezoid"](7, 5, 3))

# print((lambda a, b: a if a > b else b)(5, 13))

# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

print("Вносим изменения")





