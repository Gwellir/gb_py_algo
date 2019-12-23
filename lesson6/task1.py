# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# (Варианты изначальной решённой в трёх экземплярах задачи не особо отличались по потреблению памяти, взял другую)
# урок 3 задача 6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.


import random
import sys
from collections import Counter
import inspect  # для красоты

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100


# не особо аккуратно, вполне возможны варианты, где потребуется дополнительная фильтрация среди locals()
def get_vars_size(func_name, func_vars):
    delim = '-'*30
    total_memory = Counter()
    print(f'\nПотребление памяти переменными в функции {func_name}:')
    for arg in func_vars:
        print(f'{get_size(func_vars[arg]):<8}: {arg} {type(func_vars[arg])}')
        total_memory += {type(func_vars[arg]): get_size(func_vars[arg])}
    for type_ in total_memory:
        print(f'Тип {str(type_):<15}: {total_memory[type_]}')
    print(f"Полное потребление памяти: {sum(total_memory.values())}\n{delim}")


#  размеры iterables считаются в сумме с содержимым
def get_size(x):
    sum_size = 0
    sum_size += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                sum_size += get_size(key)
                sum_size += get_size(value)
        elif not isinstance(x, str):
            for item in x:
                sum_size += get_size(item)
    return sum_size


def max_min_1(arr):
    min_elem = (0, arr[0],)
    max_elem = (0, arr[0],)
    for i in range(1, SIZE):
        if arr[i] < min_elem[1]:
            min_elem = (i, arr[i],)
        elif arr[i] > max_elem[1]:
            max_elem = (i, arr[i],)

    start, end = min_elem[0], max_elem[0]
    if start > end:
        start, end = end, start

    elem_sum = 0
    for i in range(start + 1, end):
        elem_sum += arr[i]

    get_vars_size(inspect.currentframe().f_code.co_name, locals())

    return start, end, elem_sum,


def max_min_2(arr):
    storage = []
    for i in range(len(arr) - 1):
        storage.append([])
        for j in range(len(arr)):
            if j > i:
                storage[i].append(sum(arr[i+1:j]))
            else:
                storage[i].append([])
    minimum = min(arr)
    maximum = max(arr)
    min_elem = -1
    max_elem = -1
    for i in range(len(arr)):
        if arr[i] == minimum:
            min_elem = i
            break
    for i in range(len(arr)):
        if arr[i] == maximum:
            max_elem = i
            break
    start, end = (max_elem, min_elem) if max_elem <= min_elem else (min_elem, max_elem)
    if start >= end - 1:
        elem_sum = 0
    else:
        elem_sum = storage[start][end]

    get_vars_size(inspect.currentframe().f_code.co_name, locals())

    return start, end, elem_sum


def max_min_3(arr):
    storage = []
    for i in range(len(arr) - 1):
        storage.append([])
        for j in range(len(arr)):
            if j > i:
                storage[i].append(arr[i+1:j])
            else:
                storage[i].append([])
    minimum = min(arr)
    maximum = max(arr)
    min_elem = -1
    max_elem = -1
    for i in range(len(arr)):
        if arr[i] == minimum:
            min_elem = i
            break
    for i in range(len(arr)):
        if arr[i] == maximum:
            max_elem = i
            break
    start, end = (max_elem, min_elem) if max_elem <= min_elem else (min_elem, max_elem)
    if start >= end - 1:
        elem_sum = 0
    else:
        elem_sum = sum(storage[start][end])

    get_vars_size(inspect.currentframe().f_code.co_name, locals())

    return start, end, elem_sum


array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
print()

result1 = max_min_1(array)
result2 = max_min_2(array)
result3 = max_min_3(array)

# Python 3.7 32-bit
print('Сумма элементов от №%d до №%d: %d\n' % result1)
# Полное потребление памяти: 2036 (пример)
print('Сумма элементов от №%d до №%d: %d\n' % result2)
# Полное потребление памяти: 295274 (пример)
print('Сумма элементов от №%d до №%d: %d\n' % result3)
# Полное потребление памяти: 3302846 (пример)
assert result1 == result2 == result3, 'функции возвращают разные значения'

# По результатам получаем вывод, что изначальный вариант и был наилучшим, а заводить многомерные списки срезов
# конечно, не стоило (duh)
