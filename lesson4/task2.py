# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Выводы:
# Похоже, что для решета Эратосфена скорость работы в основном определяется изначально заданным размером решета
# Если мы с высокой точностью предполагаем верхнюю границу prime(n), то Решето может быть самым эффективным алгоритмом

# Поиск имеющихся делителей числа перебором до квадратного корня использует слишком много повторных лишних операций,
# оптимизация с применением только найденных простых потенциальных делителей выглядит рациональной.

import math
import timeit

LIMIT = 300000


def make_sieve_up_to(n):
    sieve = [True for _ in range(LIMIT + 1)]
    current = 2
    prime_count = 1
    while current < LIMIT and prime_count < n:
        for i in range(2, LIMIT // current + 1):
            sieve[i*current] = False
        while current < LIMIT and not sieve[current + 1]:
            current += 1
        current += 1
        prime_count += 1
    if prime_count == n:
        return current
    else:
        return 0


def find_prime(n):
    count = 1
    current = 2
    while count < n:
        current += 1
        for i in range(2, int(math.sqrt(current)) + 1):
            if current % i == 0:
                break
        else:
            count += 1
    if count == n:
         return current
    else:
        return 0


def find_prime_array(n):
    count = 1
    current = 2
    primes = [2]
    while count < n:
        current += 1
        for i in primes:
            if i * i > current:
                count += 1
                primes.append(current)
                break
            if current % i == 0:
                break
    if count == n:
         return current
    else:
        return 0


print(find_prime_array(100000))
assert make_sieve_up_to(10000) == find_prime(10000) == find_prime_array(10000) == 104729

num_tries = 30

s1 = """
def make_sieve_up_to(n):
    LIMIT = %d
    sieve = [True for _ in range(LIMIT + 1)]
    current = 2
    prime_count = 1
    while current < LIMIT and prime_count < n:
        for i in range(2, LIMIT // current + 1):
            sieve[i*current] = False
        while current < LIMIT and not sieve[current + 1]:
            current += 1
        current += 1
        prime_count += 1
    if prime_count == n:
        return current
    else:
        return 0

make_sieve_up_to(%d)
"""

# размер решета - 300000
#    100 - 3.1873761
#   1000 - 3.7171217
#  10000 - 4.821120199999999
print("   100 -", timeit.timeit(s1 % (300000, 100), number=num_tries))
print("  1000 -", timeit.timeit(s1 % (300000, 1000), number=num_tries))
print(" 10000 -", timeit.timeit(s1 % (300000, 10000), number=num_tries))
# размер решета - 105000 (близко к пределу для n=10000)
#    100 - 1.0423869000000003
#   1000 - 1.2431915999999994
#  10000 - 2.1739677000000004
print("   100 -", timeit.timeit(s1 % (105000, 100), number=num_tries))
print("  1000 -", timeit.timeit(s1 % (105000, 1000), number=num_tries))
print(" 10000 -", timeit.timeit(s1 % (105000, 10000), number=num_tries))
# 100000 ~ 32 при оптимальном размере
# print("100000 -", timeit.timeit(s1 % (1300000, 100000), number=num_tries))

s2 = """
def find_prime(n):
    count = 1
    current = 2
    while count < n:
        current += 1
        for i in range(2, int(math.sqrt(current)) + 1):
            if current % i == 0:
                break
        else:
            count += 1
    if count == n:
         return current
    else:
        return 0

find_prime({num})
"""

#    100 - 0.01924529999999791
#   1000 - 0.37429429999999897
#  10000 - 11.2184582
print("   100 -", timeit.timeit(s2.format(num=100), number=num_tries, globals=globals()))
print("  1000 -", timeit.timeit(s2.format(num=1000), number=num_tries, globals=globals()))
print(" 10000 -", timeit.timeit(s2.format(num=10000), number=num_tries, globals=globals()))
# 100000 - ожидается ~400 секунд
# print("100000 -", timeit.timeit(s2.format(num=100000), number=num_tries, globals=globals()))


s3 = """
def find_prime_array(n):
    count = 1
    current = 2
    primes = [2]
    while count < n:
        current += 1
        for i in primes:
            if i * i > current:
                count += 1
                primes.append(current)
                break
            if current % i == 0:
                break
    if count == n:
         return current
    else:
        return 0
        
find_prime_array({num})
"""

#    100 - 0.01135539999999935
#   1000 - 0.2260965999999982
#  10000 - 5.514904800000004
print("   100 -", timeit.timeit(s3.format(num=100), number=num_tries, globals=globals()))
print("  1000 -", timeit.timeit(s3.format(num=1000), number=num_tries, globals=globals()))
print(" 10000 -", timeit.timeit(s3.format(num=10000), number=num_tries, globals=globals()))
# 100000 ~ 140 секунд
print("100000 -", timeit.timeit(s3.format(num=100000), number=num_tries, globals=globals()))
