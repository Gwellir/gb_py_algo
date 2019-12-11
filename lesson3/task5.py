# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

index = -1
start = len(array)
max_negative = 0
for i in range(len(array)):
    if array[i] < 0:
        max_negative = array[i]
        index = start = i
        break
else:
    print('В массиве нет отрицательных элементов!')

for i in range(start + 1, len(array)):
    if 0 > array[i] > max_negative:
        index = i
        max_negative = array[i]

if index > 0:
    print(f'Максимальный отрицательный элемент: {max_negative},\n                        на позиции: {index}')
