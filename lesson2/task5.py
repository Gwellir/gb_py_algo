# 5. Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

S_START = 32
S_END = 127
ROW_LENGTH = 10

row_position = 0
for i in range(S_START, S_END + 1):
    print('{:4}'.format(i), chr(i), end='')
    row_position += 1
    if row_position == ROW_LENGTH:
        row_position = 0
        print()
