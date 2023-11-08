import math

print('Введите массив D разделяя элементы пробелом.')  # ввод первого массива
while True:
    arrayD = [int(i) for i in input().split()]
    if arrayD:
        break
    print('Ошибка. Вы ввели пустой массив. Повторите ввод!')
print('Введите массив F разделяя элементы пробелом.')  # ввод второго массива
while True:
    arrayF = [int(i) for i in input().split()]
    if arrayF:
        break
    print('Ошибка. Вы ввели пустой массив. Повторите ввод!')

matrixA = []
for j in range(len(arrayD)):  # создание массива А из элементов массива
    matrixA.append([])
    for k in range(len(arrayF)):
        matrixA[-1].append(math.sin(arrayD[j] + arrayF[k]))

AV = []  # инициализация переменных
L = []
for j in range(len(arrayD)):
    AV.append(0)
    L.append(0)
    cnt = 0
    for k in range(len(arrayF)):  # перебираем массив
        if matrixA[j][k] > 0:
            cnt += 1
            AV[-1] += matrixA[j][k]
    if cnt > 0:  # если был положительный элемент
        AV[-1] /= cnt
        for k in range(len(arrayF)):
            if matrixA[j][k] < AV[-1]:
                L[-1] += 1
    else:  # если не встретили удовлетворяющее значение, то присваиваем особое значение
        L[-1] = None
        AV[-1] = None

for line in range(len(matrixA)):  # вывод
    for el in matrixA[line]:
        print(f'{el:11.6g}', end='')
    if AV[line] is not None:  # если числовое значение, то выводим, если особое, то выводим особое
        print(f' | {AV[line]:11.6g} {L[line]:<11.6g}')
    else:
        print(' |        None None')
