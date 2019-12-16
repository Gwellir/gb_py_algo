# Реализация эмпирического тестирования времени работы алгоритмов.
# Задача:
# Определить, какое число в массиве встречается чаще всего. (№4 урок 3)

# Выводы:
# Оптимальным алгоритмом для выполнения задания в общем случае представляется решение через словарь,
# так как его работа должна производиться за O(N), хотя тут могут быть нюансы с реализацией (наблюдаемое
# время исполнения растёт быстрее N).
# Алгоритм c count, очевидно, наихудший, так как для каждого элемента перебирается весь массив, то есть O(N^2)
# Sort достаточно быстрый на малых N, скорее всего засчёт реализации, но всё же имеет сложность O(N * logN).
# Рост времени исполнения более заметен при заполнении массива более разнообразными элементами.


import random
import timeit
import cProfile

def make_array(num):
    return [random.randint(0, num) for _ in range(num)]


# конвертируем массив в строку для передачи в строковые переменные под timeit
# эмпирическим путём выяснено, что не стоит передавать строковое отображение массива на 10М элементов...
def stringify(array):
    return ','.join(str(x) for x in array)


# обычное решение через словарь
def most_frequent_dict(num_array):
    numbers = {}
    size = len(num_array)
    for i in range(size):
        numbers[num_array[i]] = numbers.get(num_array[i], 0) + 1
    max_count = 1
    top_number = num_array[0]
    for key in numbers:
        if numbers[key] > max_count:
            max_count = numbers[key]
            top_number = key
    return top_number, max_count


# сортировка и прямой подсчёт элементов подряд
def most_frequent_sort(num_array):
    size = len(num_array)
    num_array.sort()
    top_number = current = num_array[0]
    max_count = count = 1
    for i in range(1, size):
        if num_array[i] != current:
            if count > max_count:
                max_count = count
                top_number = current
            current = num_array[i]
            count = 1
        else:
            count += 1
    if count > max_count:
        top_number = current
        max_count = count
    return top_number, max_count


# подсчёт всех элементов по очереди через .count() ;)
def most_frequent_count(num_array):
    max_count = 1
    top_number = num_array[0]
    for x in num_array:
        x_count = num_array.count(x)
        if x_count > max_count:
            max_count = x_count
            top_number = x
    return top_number, max_count


# только для тестов
SIZE = 100

test_array = make_array(SIZE)
print(test_array)
print(sorted(test_array))
dct = most_frequent_dict(test_array)
srt = most_frequent_sort(test_array)
cnt = most_frequent_count(test_array)
print('dict: ', dct)
print('sort: ', srt)
print('sort: ', cnt)
assert test_array.count(dct[1]) == test_array.count(srt[1]) == test_array.count(cnt[1])
print('Test passed.\n')
# print(array_as_str)


# всё ещё достаточно точно, позволяет за адекватное время проверить dict и sort на 1М элементов
num_tests = 30


s1 = """
def most_frequent_dict(num_array):
    numbers = {}
    size = len(array)
    for i in range(size):
        numbers[num_array[i]] = numbers.get(num_array[i], 0) + 1
    max_count = 1
    top_number = num_array[0]
    for key in numbers:
        if numbers[key] > max_count:
            max_count = numbers[key]
            top_number = key
    return top_number

array = [%s]    
most_frequent_dict(array)
"""

# elems    timing
#    100 - 0.0011427000000000034
#   1000 - 0.011951199999999995
#  10000 - 0.12519059999999999
# 100000 - 1.4646911
#     1M - 17.8151249
print(f"Testing dict func for {num_tests} runs.")
print("   100 -", timeit.timeit(s1 % stringify(make_array(100)), number=num_tests))
print("  1000 -", timeit.timeit(s1 % stringify(make_array(1000)), number=num_tests))
print(" 10000 -", timeit.timeit(s1 % stringify(make_array(10000)), number=num_tests))
print("100000 -", timeit.timeit(s1 % stringify(make_array(100000)), number=num_tests))
# print("    1M -", timeit.timeit(s1 % stringify(make_array(1000000)), number=num_tests))

s2 = """
def most_frequent_sort(num_array):
    size = len(num_array)
    num_array.sort()
    top_number = current = num_array[0]
    max_count = count = 1
    for i in range(1, size):
        if num_array[i] != current:
            if count > max_count:
                max_count = count
                top_number = current
            current = num_array[i]
            count = 1
        else:
            count += 1
    if count > max_count:
        top_number = current
    return top_number

array = [%s]    
most_frequent_sort(array)
"""

# elems     timing
#    100 - 0.0006851000000018814
#   1000 - 0.009411700000001133
#  10000 - 0.10114980000000173
# 100000 - 1.6488220000000027
#     1M - 23.360897100000003
print(f"Testing sort func for {num_tests} runs.")
print("   100 -", timeit.timeit(s2 % stringify(make_array(100)), number=num_tests))
print("  1000 -", timeit.timeit(s2 % stringify(make_array(1000)), number=num_tests))
print(" 10000 -", timeit.timeit(s2 % stringify(make_array(10000)), number=num_tests))
print("100000 -", timeit.timeit(s2 % stringify(make_array(100000)), number=num_tests))
# print("    1M -", timeit.timeit(s2 % stringify(make_array(1000000)), number=num_tests))

s3 = """
def most_frequent_count(num_array):
    size = len(num_array)
    max_count = 1
    max_x = num_array[0]
    for x in num_array:
        x_count = num_array.count(x)  
        if x_count > max_count:
            max_count = x_count
    return max_count

array = [%s]
most_frequent_count(array)
"""

# elems     timing
#    100 - 0.005663300000001925
#   1000 - 0.48477469999999556
#  10000 - 48.152837600000005
# 100000 - ожидание ~80 минут, выглядит как квадратичное время
print(f"Testing count func for {num_tests} runs.")
print("   100 -", timeit.timeit(s3 % stringify(make_array(100)), number=num_tests))
print("  1000 -", timeit.timeit(s3 % stringify(make_array(1000)), number=num_tests))
print("  3000 -", timeit.timeit(s3 % stringify(make_array(3000)), number=num_tests))
# print(" 10000 -", timeit.timeit(s3 % stringify(make_array(10000)), number=num_tests))
# print("100000 -", timeit.timeit(s3 % stringify(make_array(100000)), number=num_tests))
# print("    1M -", timeit.timeit(s3 % stringify(make_array(1000000)), number=num_tests))

