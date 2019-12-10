# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

WIDTH = 5
HEIGHT = 10
MIN_ITEM = 0
MAX_ITEM = 100

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, WIDTH)] for _ in range(0, HEIGHT)]
print(*matrix, sep='\n')
print()

minimums = [matrix[0][col] for col in range(0, WIDTH)]
for c in range(0, WIDTH):
    for r in range(1, HEIGHT):
        if matrix[r][c] < minimums[c]:
            minimums[c] = matrix[r][c]
print(minimums)

max_min = minimums[0]
for i in range(1, WIDTH):
    if minimums[i] > max_min:
        max_min = minimums[i]

print(f'Максимум из минимальных элементов столбцов: {max_min}')
