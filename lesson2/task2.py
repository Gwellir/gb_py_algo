# 2. Посчитать четные и нечетные цифры введенного натурального числа.

odd = 0
even = 0

x = int(input('Введите натуральное число: '))

while True:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    x = x // 10
    if x == 0:
        print(f'Чётных цифр: {even},\nнечётных: {odd}.')
        break