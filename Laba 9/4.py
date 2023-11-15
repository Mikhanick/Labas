# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 9, задание 4
matrixD = []  # инициализируем матрицу
print('Для ввода матрицы напишите через пробел значения строк, затем нажмите Enter. По окончании ввода строк нажмите '
      'Enter')
while True:
    line = [int(i) for i in input().split()]  # ввод строки в матрицу
    if not matrixD:
        matrixD.append(line)  # Если матрица еще пустая, то просто добавляем любую строку
    elif not line:  # если введена пустая строка, то завершаем ввод матрицы
        print('Ввод матрицы завершен.')
        break
    elif len(matrixD[0]) == len(line):  # если длина строки равна длине первой строке, иначе выводим ошибку и просим
        # повторить ввод
        matrixD.append(line)
    else:
        print(f'Ошибка. Длина строк в матрице должна совпадать, и должна быть равна '
              f'{len(matrixD[0])}.\nПовторите ввод!')
if len(matrixD) == 0:
    print("Ошибка. Вы ввели пустую матрицу. Работа программы завершена с ошибкой!")  # выводим ошибку, что не совпадает
    # количество элементов в строке с остальной матрицей
else:
    while True:
        print("Введите массив I со строками ")  # вводим массив, если элемента под индексом из массива нет,
        # то будем пропускать дальше
        arrayI = [int(i) for i in input().split()]
        if arrayI:
            break
        print('Ошибка. Вы ввели пустой массив. Повторите ввод!')

arrayR = []
print()

for line in arrayI:
    if line >= len(matrixD):  # пропуск элемента если нет такого в массиве
        print(f"Строчка {line} не находится в матрице D, длиной {len(matrixD)}")
        print('Пропуск итерации.')
    else:
        arrayR.append(matrixD[line][0])  # добавляем в массив R по индексу из массива
        for col in range(1, len(matrixD[line])):
            if matrixD[line][col] > arrayR[-1]:
                arrayR[-1] = matrixD[line][col]

print()

if arrayR:  # если хоть один индекс существовал в массиве, то есть элемент в массиве R значит он
    # не пустой иначе не выводим
    AV = 0
    for i in arrayR:
        AV += i
    AV /= len(arrayR)
    print("Изначальная матрица:")
    for line in matrixD:  # вывод
        for el in line:
            print(f'{el:5.5g}', end='')
        print()

    print('Массив I:', *arrayI)
    print('Массив R:', *arrayR)
    print('Среднее арифметическое максимумов:', AV)
else:
    print(
        'Нет значений максимумов строчек R и, соответственно, значения среднего арифметического.')  # вывод если пустой
    print("Изначальная матрица:")
    for line in matrixD:  # вывод
        for el in line:
            print(f'{el:5.5g}', end='')
        print()

    print('Массив I:', *arrayI)
