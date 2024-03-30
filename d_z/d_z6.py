def func(lst):
    if lst:
        if lst[0] < 0:
            print(lst, lst[0])
        return (lst[0] < 0) + func(lst[1:])
    return 0


lst = [-2, 3, 8, -11, -4, 6]
print(func(lst))

