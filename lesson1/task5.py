# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

char1, char2 = input('Введите две буквы латинского алфавита через пробел: ').split()

offset = ord('a') - 1
place1 = ord(char1) - offset
place2 = ord(char2) - offset
difference = abs(place1 - place2)
if difference == 0:
    interval = 0
else:
    interval = difference - 1

print(f'Номер первой буквы: {place1}.')
print(f'Номер второй буквы: {place2}.')
print(f'Между ними в алфавите {interval} букв.')