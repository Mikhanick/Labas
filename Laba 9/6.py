matrixA = []  # инициализируем матрицу
print('Для ввода матрицы А напишите через пробел значения строк, затем нажмите Enter. По окончании ввода строк нажмите '
      'Enter')
while True:
    line = [int(i) for i in input().split()]  # ввод строки в матрицу
    if matrixA == [] and len(line) != 0:
        matrixA.append(line)  # Если матрица еще пустая, то просто добавляем любую строку
    elif not line:  # если введена пустая строка, то завершаем ввод матрицы
        if len(matrixA) != 0:
            print('Ввод матрицы завершен.')
            break
        else:
            print('Матрица должна быть не пустая!')
    elif len(matrixA[0]) == len(line):  # если длина строки равна длине первой строке, иначе выводим ошибку и просим
        # повторить ввод
        matrixA.append(line)
    else:
        print(
            f'Ошибка. Длина строк в матрице должна совпадать, и должна быть равна {len(matrixA[0])}.\nПовторите ввод!')

matrixB = []  # инициализируем матрицу
print('Для ввода матрицы В напишите через пробел значения строк, затем нажмите Enter. Ввод окончится, когда'
      ' количество строк в матрицах А и В станет равным')
while True:
    line = [int(i) for i in input().split()]  # ввод строки в матрицу

    if len(matrixA[0]) == len(
            line):  # если длина строки равна длине первой строке матрицы А, иначе выводим ошибку и просим
        # повторить ввод
        matrixB.append(line)
    else:
        print(
            f'Ошибка. Длина строк в матрице должна совпадать c длиной строк в матрице А, и должна быть равна '
            f'{len(matrixA[0])}.\nПовторите ввод!')
    if len(matrixB) == len(matrixA):  # если матрицы становятся одинакового размера завершаем ввод
        print('Ввод матрицы завершен.')
        break

matrixC = []

for i in range(len(matrixA)):  # создаем матрицу С
    matrixC.append([])
    for j in range(len(matrixA[0])):
        matrixC[-1].append(matrixA[i][j] * matrixB[i][j])
# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 9, задание 6
arrayV = [0] * (len(matrixA[0]))  # создаем массив V
for i in range(len(matrixA)):  # считаем и записываем сумму столбцов в массив V
    for j in range(len(matrixA[0])):
        arrayV[j] += matrixC[i][j]

print('Матрица А:')
for line in matrixA:  # вывод
    for el in line:
        print(f'{el:5.5g}', end='')
    print()

print('Матрица В:')
for line in matrixB:  # вывод
    for el in line:
        print(f'{el:5.5g}', end='')
    print()

print('Матрица С:')
for line in matrixC:  # вывод
    for el in line:
        print(f'{el:5.5g}', end='')
    print()

print('\nМассив V:', *arrayV)
