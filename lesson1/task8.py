year = int(input('Введите год в формате YYYY: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'Год {year} - високосный')
        else:
            print(f'Год {year} - не високосный')
    else:
        print(f'Год {year} - високосный')
else:
    print(f'Год {year} - не високосный')