import math
import itertools

# Завдання 1: Обчислення кількості розміщень без повторень
n = 12
r = 6

# Обчислення кількості розміщень без повторень
arrangements = math.perm(n, r)

# Виведення результату
print("Кількість розміщень без повторень:", arrangements)

# Завдання 2: Побудова таблиці для чисел Стірлінга другого роду та числа Белла
i = 9
n = i + 5

# Побудова таблиці для чисел Стірлінга другого роду
stirling_table = []
for k in range(n + 1):
    row = []
    for j in range(i + 1):
        if j == 0 or j > k:
            row.append(0)
        elif j == 1 or j == k:
            row.append(1)
        else:
            row.append(j * stirling_table[k - 1][j] + stirling_table[k - 1][j - 1])
    stirling_table.append(row)

# Обчислення числа Белла
bell_number = sum(stirling_table[n])

# Виведення результатів
print("Таблиця чисел Стірлінга другого роду:")
for row in stirling_table:
    print(row)
print("Число Белла для n =", n, ":", bell_number)
