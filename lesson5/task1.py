# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартала (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter

INTERVALS = 4  # кварталы

factories = Counter()
amount = int(input('Количество предприятий? '))
for i in range(amount):
    name = input(f'Введите название предприятия {i+1}: ')
    for k in range(INTERVALS):
        profit = int(input(f'Введите прибыль "{name}" за квартал {k+1}: '))
        factories[name] += profit

sum_profits = 0
for val in factories.values():
    sum_profits += val
avg = sum_profits/amount
print(f'\nСредняя годовая прибыль - {avg}.')

avg_factories = Counter()
for name in factories:
    avg_factories[name] = avg
print('\nПредприятия с прибылью выше средней: ')
for name in (factories - avg_factories):
    print(name)
print('\nПредприятия с прибылью ниже средней: ')
for name in (avg_factories - factories):
    print(name)
