n = int(input("Введите число от 1 до 99: "))
if 1 <= n <= 99:
    if 5 <= n <= 20 or 25 <= n <= 30 or 35 <= n <= 40 or 45 <= n <= 50 or 55 <= n <= 60 or 65 <= n <= 70 or 75 <= n <= 80 or 85 <= n <= 90 or 95 <= n <= 99:
        print(n, "копеек", end=" ")
    elif n == 1 or n == 21 or n == 31 or n == 41 or n == 51 or n == 61 or n == 71 or n == 81 or n == 91:
        print(n, "копейка")
    else:
        print(n, "копейки")
else:
    print(" Ошибка ввода данных")

