# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

WIDTH = 4
HEIGHT = 5

matrix = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

cell_size = 0
for k in range(len(matrix)):
    row_sum = 0
    for i in range(WIDTH - 1):
        matrix[k][i] = value = int(input(f'Введите целое значение для ячейки [{k}][{i}]: '))
        row_sum += value
        if cell_size < len(str(value)):
            cell_size = len(str(value))
    matrix[k][WIDTH - 1] = row_sum
    if cell_size < len(str(row_sum)):
        cell_size = len(str(row_sum))

for row in matrix:
    for entry in row:
        print(f'{entry:>{cell_size + 1}}', end='')
    print()
