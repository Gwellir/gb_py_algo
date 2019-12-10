# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

numbers = {}
for i in range(0, SIZE):
    numbers[array[i]] = numbers.get(array[i], 0) + 1
max_amount = 1
top_number = array[0]
for key in numbers.keys():
    if numbers[key] > max_amount:
        max_amount = numbers[key]
        top_number = key

print(f'Наиболее часто встречающееся в массиве число: {top_number}, встречается {max_amount} раз.')
