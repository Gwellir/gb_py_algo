# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def digit_count(num, digit):
    if num == 0:
        return 0
    else:
        count = digit_count(num // 10, digit)
        if num % 10 == digit:
            count += 1
        return count


def get_total_count(amount, digit):
    if amount == 0:
        return 0
    else:
        total = get_total_count(amount - 1, digit)
        num = int(input(f'Натуральное число {amount}: '))
        return total + digit_count(num, digit)


amount = int(input('Введите натуральное количество чисел: '))
digit = int(input('Введите цифру для подсчёта: '))
total = get_total_count(amount, digit)
print(total)
