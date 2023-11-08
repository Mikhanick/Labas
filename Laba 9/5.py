matrix = []  # инициализируем матрицу
print('Для ввода матрицы D напишите через пробел значения строк, затем нажмите Enter. По окончании ввода строк нажмите '
      'Enter')
while True:
    line = [i for i in input().split()]  # ввод строки в матрицу
    if matrix == [] and len(line) != 0:
        matrix.append(line)  # Если матрица еще пустая, то просто добавляем любую строку
    elif not line:  # если введена пустая строка, то завершаем ввод матрицы
        if len(matrix) != 0:
            print('Ввод матрицы завершен.')
            break
        else:
            print('Матрица должна быть не пустая!')
    elif len(matrix[0]) == len(line):  # если длина строки равна длине первой строке, иначе выводим ошибку и просим
        # повторить ввод
        matrix.append(line)
    else:
        print(f'Ошибка. Длина строк в матрице должна совпадать, и должна быть равна {len(matrix[0])}.\nПовторите ввод!')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        for letter in 'AUYOIEauyoie':
            if letter in matrix[i][j]:
                matrix[i][j] = matrix[i][j].replace(letter, '.')
for line in matrix:  # вывод
    for el in line:
        print(f'{el}  ', end='')
    print()
