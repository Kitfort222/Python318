a = int(input("Введите пятизначное число: "))
res1 = 0
res2 = 1
res3 = 0
while a > 0:
    i = a % 10
    res1 += i
    res2 *= i
    res3 = res1 / 5
    a //= 10
print("Сумма цифр числа:", res1)
print("Произведение цифр числа: ", res2)
print("Среднее арифметическое цифр числа: ", res3)



