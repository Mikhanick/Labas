# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 9, задание 2
matrix = []  # инициализируем матрицу
print(
    'Для ввода матрицы напишите через пробел значения строк, затем нажмите Enter. Ввод окончится, когда матрица '
    'станет квадратной')
while True:
    line = [int(i) for i in input().split()]  # ввод строки в матрицу
    if matrix == [] and len(line) != 0:
        matrix.append(line)  # Если матрица еще пустая, то просто добавляем любую строку

    elif len(matrix[0]) == len(line):  # если длина строки равна длине первой строке, иначе выводим ошибку и просим
        # повторить ввод
        matrix.append(line)
    else:
        print(f'Ошибка. Длина строк в матрице должна совпадать, и должна быть равна {len(matrix[0])}.\nПовторите ввод!')
    if len(matrix) == len(matrix[0]):
        print('Ввод квадратной матрицы завершён.')
        break
# matrix = [[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35],[41,42,43,44,45],[51,52,53,54,55]]

for line in matrix:  # вывод
    for el in line:
        print(f'{el:5.5g}', end='')
    print()

n = len(matrix)
needed_n = n // 2
# print(needed_n)
for i in range(needed_n):
    for j in range(needed_n):  # в четверти матрицы меняем все элементы на аналогичные из других трех четвертей
        # путем замены по 4 элемента
        # при этом элементы на средних линиях (если длина квадратной матрицы не четная) остаются
        matrix[j][i], matrix[n - 1 - i][j], matrix[n - 1 - j][n - 1 - i], matrix[i][n - 1 - j] = matrix[n - 1 - i][j], \
            matrix[n - 1 - j][n - 1 - i], matrix[i][n - 1 - j], matrix[j][i]

    if n % 2 != 0:  # если длина матрицы не четная, то меняем местоположение элементов на "центральном кресте"
        matrix[i][needed_n], matrix[needed_n][i], matrix[n - 1 - i][needed_n], matrix[needed_n][n - 1 - i] = \
            matrix[needed_n][i], matrix[n - 1 - i][needed_n], matrix[needed_n][n - 1 - i], matrix[i][needed_n]

print('Матрица после поворота на 90 градусов по часовой стрелке: ')

for line in matrix:  # вывод
    for el in line:
        print(f'{el:5.5g}', end='')
    print()

for i in range(needed_n):
    for j in range(needed_n):  # аналогично первому повороту, но поменял местами элементы в равенстве,
        # чтобы повернуть в противоположную сторону
        matrix[n - 1 - i][j], matrix[n - 1 - j][n - 1 - i], matrix[i][n - 1 - j], matrix[j][i] = matrix[j][i], \
            matrix[n - 1 - i][j], matrix[n - 1 - j][n - 1 - i], matrix[i][n - 1 - j]

    if n % 2 != 0:
        matrix[needed_n][i], matrix[n - 1 - i][needed_n], matrix[needed_n][n - 1 - i], matrix[i][needed_n] = matrix[i][
            needed_n], matrix[needed_n][i], matrix[n - 1 - i][needed_n], matrix[needed_n][n - 1 - i]

print('Матрица после поворота на 90 градусов против часовой стрелки: ')

for line in matrix:  # вывод
    for el in line:
        print(f'{el:5.5g}', end='')
    print()
