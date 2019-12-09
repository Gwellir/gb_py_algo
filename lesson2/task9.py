# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

answer = 0
max_sum = 0

while True:
    num = int(input('Введите натуральное число или ноль для завершения: '))

    if num == 0:
        break
    else:
        digit_sum = 0
        var = num
        while True:
            digit_sum += var % 10
            var = var // 10
            if var == 0:
                break
        if digit_sum > max_sum:
            max_sum = digit_sum
            answer = num

print(f'Число: {answer}; сумма цифр: {max_sum}')