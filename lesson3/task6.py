# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_elem = (0, array[0],)
max_elem = (0, array[0],)
for i in range(1, SIZE):
    if array[i] < min_elem[1]:
        min_elem = (i, array[i],)
    elif array[i] > max_elem[1]:
        max_elem = (i, array[i],)

start, end = min_elem[0], max_elem[0]
if start > end:
    start, end = end, start

elem_sum = 0
for i in range(start + 1, end):
    elem_sum += array[i]

print(f'Сумма элементов от №{start}({array[start]}) до №{end}({array[end]}): {elem_sum}')


