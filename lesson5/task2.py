# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как структура данных модуля collections, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque, defaultdict, Counter


# построение таблицы сложения
def make_sum_table(digit_str):
    spam_dq = deque(digit_str)
    sum_table = defaultdict(dict)
    for d1 in digit_str:
        sub_dict = {}
        for d2 in digit_str:
            sub_dict[d2] = spam_dq.popleft()
            spam_dq.append(sub_dict[d2])
        spam_dq.append(spam_dq.popleft())  # сдвиг очереди между строками
        sum_table[d1] = sub_dict

    return sum_table


# построение таблицы умножения
def make_mult_table(digit_str):
    spam_dq = deque([deque(base_str[0]) for _ in base_str])
    mult_table = defaultdict(dict)
    for d1 in base_str:
        sub_dict = {}
        for d2 in base_str:
            sub_dict[d2] = spam_dq.popleft()
            spam_dq.append(dq_sum(sub_dict[d2], d2))  # модификация очереди между строками
        mult_table[d1] = sub_dict

    return mult_table


# функция поразрядного сложения
def dq_sum(num1, num2):
    dq1 = deque(base_str[0])
    dq2 = deque(base_str[0])
    # неоптимально, но не хочется писать ветвление под разные варианты длин, сложность все равно O(len)
    l1, l2 = len(num1), len(num2)
    if l1 < l2:
        dq1.extend(base_str[0] * (l2 - l1))
    elif l2 < l1:
        dq2.extend(base_str[0] * (l1 - l2))
    dq1.extend(num1)
    dq2.extend(num2)

    base_sum = deque()
    shift = False

    while dq1:
        shifted = False
        d1 = dq1.pop()
        d2 = dq2.pop()
        sum_digit = base_sum_table[d1][d2]
        if shift:
            shifted = True
            sum_digit = base_sum_table[sum_digit][base_str[1]]
        shift = False
        if base_dict[sum_digit] < base_dict[d1] or (shifted and base_dict[sum_digit] == base_dict[d1]):
            shift = True
        base_sum.appendleft(sum_digit)

    while base_sum and base_sum[0] == base_str[0]:
        base_sum.popleft()
    if not base_sum:
        base_sum.append(base_str[0])

    return base_sum


# функция поразрядного умножения
def dq_mult(dq1, dq2):
    dq1.reverse()
    dq2.reverse()

    mult = deque()
    prefix1 = deque()
    for d1 in dq1:
        prefix2 = deque()
        for d2 in dq2:
            addition = deque(base_mult_table[d1][d2])
            addition.extend(prefix2)
            addition.extend(prefix1)
            mult = dq_sum(addition, mult)
            prefix2.append(base_str[0])
        prefix1.append(base_str[0])
    dq1.reverse()
    dq2.reverse()

    return mult


HEX_STR = '0123456789ABCDEF'

# поиск символа по номеру
base_str = HEX_STR
base_count = Counter(HEX_STR)  # ну в общем-то и преобразования в сет хватило бы, но пусть будет
assert base_count.most_common(1)[0][1] == 1, 'Символы невозможно использовать как базу числовой записи!'
base_len = len(base_str)
print(f'Используется базовый набор символов "{base_str}",\nразрядность: {base_len}\n')
# поиск номера по символу
base_dict = {}
for i in range(len(base_str)):
    base_dict[base_str[i]] = i

base_sum_table = make_sum_table(base_str)

print('-'*15, 'Таблица сложения', '-'*15)
for x in base_sum_table:
    print(f'{x}:', end=' ')
    for y in base_sum_table[x]:
        print(base_sum_table[x][y], ' ', end='')
    print()

base_mult_table = make_mult_table(base_str)

print('\n', '-'*22, 'Таблица умножения', '-'*22)
for x in base_mult_table:
    print(f'{x}:', end=' ')
    for y in base_mult_table[x]:
        print(f"{''.join(base_mult_table[x][y]):>2}", ' ', end='')
    print()
print()

# Основной цикл
while True:
    op = input('Введите тип операции - "+" или "*" (иное для завершения): ')
    if op == '+':
        n1 = deque(input('Введите первое слагаемое: '))
        n2 = deque(input('Введите второе слагаемое: '))
        sum_ = dq_sum(n1, n2)
        print(f'Результат:\n{n1}\n+\n{n2}\n=\n{sum_}')
        if base_str == HEX_STR:
            assert ''.join(sum_) == hex(int(''.join(n1), 16) + int(''.join(n2), 16))[2:].upper(), 'Не сходится!'
    elif op == '*':
        n1 = deque(input('Введите первый множитель: '))
        n2 = deque(input('Введите второй множитель: '))
        mult_ = dq_mult(n1, n2)
        print(f"Результат: {''.join(mult_)}\n{n1}\n*\n{n2}\n=\n{mult_}")
        if base_str == HEX_STR:
            assert ''.join(mult_) == hex(int(''.join(n1), 16) * int(''.join(n2), 16))[2:].upper(), 'Не сходится!'
    else:
        break
