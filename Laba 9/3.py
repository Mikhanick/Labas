matrixD = []  # инициализируем матрицу
print('Для ввода матрицы D напишите через пробел значения строк, затем нажмите Enter. По окончании ввода строк нажмите '
      'Enter')
while True:
    line = [int(i) for i in input().split()]  # ввод строки в матрицу
    if matrixD == [] and len(line) != 0:
        matrixD.append(line)  # Если матрица еще пустая, то просто добавляем любую строку
    elif not line:  # если введена пустая строка, то завершаем ввод матрицы
        if len(matrixD) != 0:
            print('Ввод матрицы завершен.')
            break
        else:
            print('Матрица должна быть не пустая!')
    elif len(matrixD[0]) == len(line):  # если длина строки равна длине первой строке, иначе выводим ошибку и просим
        # повторить ввод
        matrixD.append(line)
    else:
        print(f'Ошибка. Длина строк в матрице должна совпадать, и должна быть равна '
              f'{len(matrixD[0])}.\nПовторите ввод!')

matrixZ = []  # инициализируем матрицу
print('Для ввода матрицы Z напишите через пробел значения строк, затем нажмите Enter. Ввод окончится, когда'
      ' количество строк в матрицах D и Z станет равным')
while True:
    line = [int(i) for i in input().split()]  # ввод строки в матрицу
    if not matrixZ:
        matrixZ.append(line)  # Если матрица еще пустая, то просто добавляем любую строку

    elif len(matrixZ[0]) == len(line):  # если длина строки равна длине первой строке, иначе выводим ошибку и просим
        # повторить ввод
        matrixZ.append(line)
    else:
        print(f'Ошибка. Длина строк в матрице должна совпадать, и должна быть равна '
              f'{len(matrixZ[0])}.\nПовторите ввод!')
    if len(matrixZ) == len(matrixD):  # если введена пустая строка, то завершаем ввод матрицы
        print('Ввод матрицы завершен.')
        break

G = []

for i in range(len(matrixZ)):  # находим значения элементов массива G
    sum_line_Z = sum(matrixZ[i])
    cnt = 0
    for el in matrixD[i]:
        if el > sum_line_Z:
            cnt += 1
    G.append(cnt)

g_max = max(G)

print('Матрица D перед преобразованием: ')
for line in matrixD:  # вывод
    for el in line:
        print(f'{el:5.5g}', end='')
    print()

for i in range(len(matrixD)):  # умножаем каждый элемент матрицы D на максимальное значение массива G
    for j in range(len(matrixD[i])):
        matrixD[i][j] *= g_max

print('Матрица Z:')
for line in matrixZ:  # вывод
    for el in line:
        print(f'{el:5.5g}', end='')
    print()

print('Матрица D после преобразования: ')
for line in matrixD:  # вывод
    for el in line:
        print(f'{el:5.5g}', end='')
    print()

print('Массив G:', *G)
