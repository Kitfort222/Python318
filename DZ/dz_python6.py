from random import randint

w, h = 3, 4
count = 0
matrix = [[randint(-20, 10) for y in range(w)] for x in range(h)]
for row in matrix:
    for x in row:
        print(x, end="\t\t")
        if x < 0:
           count += 1
    print()
print(count)