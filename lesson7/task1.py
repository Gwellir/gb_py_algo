# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):  # последние элементы уже отсортированы
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
sa = sorted(array, reverse=True)
bubble_sort(array)
print(array)
assert sa == array, 'Сортировка работает неверно!'
